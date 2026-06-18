# 🚀 بوت تيليغرام لبيع خدمات السوشيال ميديا

## 📋 خطوات الإعداد

### 1️⃣ إنشاء البوت في تيليغرام
1. افتح `@BotFather` في تيليغرام
2. أرسل `/newbot`
3. اختر اسماً للبوت
4. احفظ **التوكن** الذي يعطيك إياه

### 2️⃣ الحصول على معرف حسابك (Admin ID)
- افتح `@userinfobot` في تيليغرام
- أرسل `/start`
- احفظ الرقم الظاهر (هذا هو ADMIN_ID)

### 3️⃣ الحصول على مفتاح SMM API
1. سجّل في [smmcpan.com](https://smmcpan.com) أو أي لوحة SMM
2. اذهب إلى الإعدادات → API
3. انسخ مفتاح API الخاص بك

### 4️⃣ رفع الكود على GitHub
1. أنشئ حساباً على [github.com](https://github.com)
2. اضغط `+` → `New Repository`
3. ارفع جميع ملفات المشروع

### 5️⃣ الاستضافة على Railway (مجاني)
1. اذهب إلى [railway.app](https://railway.app)
2. سجّل دخول بحساب GitHub
3. اضغط `New Project` → `Deploy from GitHub Repo`
4. اختر المستودع الذي رفعت إليه الكود
5. اضغط على المشروع → `Variables` وأضف:

```
BOT_TOKEN     = توكن_البوت_من_BotFather
ADMIN_ID      = معرف_حسابك_في_تيليغرام
SMM_API_KEY   = مفتاح_API_من_لوحة_SMM
SMM_API_URL   = https://smmcpan.com/api/v2
USDT_ADDRESS  = عنوان_محفظة_USDT_الخاصة_بك
BINANCE_ID    = معرف_Binance_Pay_الخاص_بك
SUPPORT_USERNAME = @اسم_حسابك
```

6. اضغط `Deploy` ✅

---

## 🎮 أوامر الأدمن

| الأمر | الوظيفة |
|-------|---------|
| `/stats` | إحصائيات البوت والمستخدمين |
| `/addbal 123456 10` | إضافة رصيد لمستخدم |

---

## ✨ مميزات البوت

- ✅ قائمة خدمات لـ 6 منصات (Instagram, TikTok, YouTube, Twitter, Facebook, Snapchat)
- ✅ نظام رصيد كامل
- ✅ شحن عبر USDT و Binance Pay
- ✅ إشعارات فورية للأدمن
- ✅ قبول/رفض طلبات الشحن بزر واحد
- ✅ متابعة حالة الطلبات
- ✅ قاعدة بيانات SQLite محلية

---

## 📁 هيكل الملفات

```
smm_bot/
├── main.py              # البوت الرئيسي
├── config.py            # الإعدادات
├── database.py          # قاعدة البيانات
├── smm_api.py           # ربط SMM Panel
├── services_catalog.py  # قائمة الخدمات والأسعار
├── requirements.txt     # المكتبات المطلوبة
└── Procfile             # إعداد Railway
```
