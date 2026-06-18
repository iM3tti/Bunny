import sqlite3
import os

DB_PATH = "bot_database.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    """إنشاء الجداول عند أول تشغيل"""
    conn = get_conn()
    c = conn.cursor()

    # جدول المستخدمين
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id     INTEGER PRIMARY KEY,
            username    TEXT,
            full_name   TEXT,
            balance     REAL    DEFAULT 0.0,
            total_spent REAL    DEFAULT 0.0,
            joined_at   TEXT    DEFAULT (datetime('now'))
        )
    """)

    # جدول الطلبات
    c.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER,
            service_id  TEXT,
            service_name TEXT,
            link        TEXT,
            quantity    INTEGER,
            price       REAL,
            smm_order_id TEXT,
            status      TEXT    DEFAULT 'pending',
            created_at  TEXT    DEFAULT (datetime('now'))
        )
    """)

    # جدول طلبات الشحن
    c.execute("""
        CREATE TABLE IF NOT EXISTS deposits (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER,
            amount      REAL,
            method      TEXT,
            proof       TEXT,
            status      TEXT    DEFAULT 'pending',
            created_at  TEXT    DEFAULT (datetime('now'))
        )
    """)

    conn.commit()
    conn.close()

# ==============================
#  وظائف المستخدمين
# ==============================

def register_user(user_id, username, full_name):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT OR IGNORE INTO users (user_id, username, full_name)
        VALUES (?, ?, ?)
    """, (user_id, username, full_name))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"user_id": row[0], "username": row[1], "full_name": row[2],
                "balance": row[3], "total_spent": row[4], "joined_at": row[5]}
    return None

def get_balance(user_id):
    user = get_user(user_id)
    return user["balance"] if user else 0.0

def update_balance(user_id, amount):
    """زيادة أو خصم من الرصيد"""
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()

def get_all_users():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT user_id, username, full_name, balance FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

# ==============================
#  وظائف الطلبات
# ==============================

def create_order(user_id, service_id, service_name, link, quantity, price):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO orders (user_id, service_id, service_name, link, quantity, price)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, service_id, service_name, link, quantity, price))
    order_id = c.lastrowid
    conn.commit()
    conn.close()
    return order_id

def update_order_smm_id(order_id, smm_order_id, status="processing"):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE orders SET smm_order_id = ?, status = ? WHERE id = ?",
              (smm_order_id, status, order_id))
    conn.commit()
    conn.close()

def get_user_orders(user_id, limit=10):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT id, service_name, link, quantity, price, status, created_at
        FROM orders WHERE user_id = ?
        ORDER BY created_at DESC LIMIT ?
    """, (user_id, limit))
    rows = c.fetchall()
    conn.close()
    return rows

# ==============================
#  وظائف الشحن
# ==============================

def create_deposit(user_id, amount, method, proof):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO deposits (user_id, amount, method, proof)
        VALUES (?, ?, ?, ?)
    """, (user_id, amount, method, proof))
    dep_id = c.lastrowid
    conn.commit()
    conn.close()
    return dep_id

def approve_deposit(deposit_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT user_id, amount FROM deposits WHERE id = ?", (deposit_id,))
    row = c.fetchone()
    if row:
        user_id, amount = row
        update_balance(user_id, amount)
        c.execute("UPDATE deposits SET status = 'approved' WHERE id = ?", (deposit_id,))
        conn.commit()
        conn.close()
        return user_id, amount
    conn.close()
    return None, None

def reject_deposit(deposit_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE deposits SET status = 'rejected' WHERE id = ?", (deposit_id,))
    conn.commit()
    conn.close()

def get_pending_deposits():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT d.id, d.user_id, u.full_name, d.amount, d.method, d.proof, d.created_at
        FROM deposits d JOIN users u ON d.user_id = u.user_id
        WHERE d.status = 'pending'
        ORDER BY d.created_at DESC
    """)
    rows = c.fetchall()
    conn.close()
    return rows
