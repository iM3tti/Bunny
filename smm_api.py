import requests
from config import SMM_API_URL, SMM_API_KEY

def _post(payload: dict):
    """إرسال طلب إلى SMM Panel"""
    try:
        payload["key"] = SMM_API_KEY
        r = requests.post(SMM_API_URL, data=payload, timeout=15)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def get_services():
    """جلب قائمة الخدمات من اللوحة"""
    return _post({"action": "services"})

def create_order(service_id: str, link: str, quantity: int):
    """إنشاء طلب جديد"""
    return _post({
        "action":   "add",
        "service":  service_id,
        "link":     link,
        "quantity": quantity,
    })

def check_status(smm_order_id: str):
    """فحص حالة طلب موجود"""
    return _post({
        "action": "status",
        "order":  smm_order_id,
    })

def get_balance():
    """فحص الرصيد في لوحة SMM"""
    return _post({"action": "balance"})
