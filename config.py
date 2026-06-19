import os

# ==============================
#  إعدادات البوت - غيّر هذه القيم
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN", "8731640232:AAHMf1J2fPB-xEjHBEMVEMLnELhZwHwx2bM")
ADMIN_ID  = int(os.getenv("ADMIN_ID", "8605635198"))  # معرف حسابك في تيليغرام

# ==============================
#  إعدادات SMM Panel API
# ==============================
SMM_API_URL = os.getenv("SMM_API_URL", "https://beinty.com/api/v2")
SMM_API_KEY = os.getenv("SMM_API_KEY", "bnt_9154209dc5403f2699dddc5abf887aa954be70b0")

# ==============================
#  إعدادات الدفع
# ==============================
ماستر كارد الرافدين   = os.getenv("USDT_ADDRESS", "عنوان_USDT_TRC20_هنا")
BINANCE_ID     = os.getenv("BINANCE_ID", "Binance_Pay_ID_هنا")

# ==============================
#  إعدادات عامة
# ==============================
CURRENCY       = "USD"
MIN_DEPOSIT    = 1.0    # أقل مبلغ شحن بالدولار
SUPPORT_USERNAME = "@aliibunny"
