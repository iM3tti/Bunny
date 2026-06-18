# ======================================================
#  كتالوج الخدمات — غيّر service_id بالأرقام الصحيحة
#  من لوحة SMM Panel الخاصة بك
# ======================================================

PLATFORMS = {
    "instagram": {
        "name": "📸 Instagram",
        "services": [
            {"id": "101", "name": "👥 متابعين عرب حقيقيين",    "price_per_1k": 1.50, "min": 100,  "max": 10000},
            {"id": "102", "name": "❤️ لايكات سريعة",            "price_per_1k": 0.50, "min": 50,   "max": 50000},
            {"id": "103", "name": "👁 مشاهدات ريلز",             "price_per_1k": 0.20, "min": 1000, "max": 500000},
            {"id": "104", "name": "💬 تعليقات عربية",            "price_per_1k": 5.00, "min": 10,   "max": 1000},
        ]
    },
    "tiktok": {
        "name": "🎵 TikTok",
        "services": [
            {"id": "201", "name": "👥 متابعين تيك توك",          "price_per_1k": 2.00, "min": 100,  "max": 10000},
            {"id": "202", "name": "❤️ لايكات تيك توك",           "price_per_1k": 0.30, "min": 100,  "max": 100000},
            {"id": "203", "name": "👁 مشاهدات فيديو",             "price_per_1k": 0.10, "min": 1000, "max": 1000000},
            {"id": "204", "name": "🔗 مشاركات",                   "price_per_1k": 1.00, "min": 100,  "max": 10000},
        ]
    },
    "youtube": {
        "name": "▶️ YouTube",
        "services": [
            {"id": "301", "name": "👥 مشتركين يوتيوب",           "price_per_1k": 5.00, "min": 50,   "max": 5000},
            {"id": "302", "name": "👁 مشاهدات يوتيوب",            "price_per_1k": 1.50, "min": 500,  "max": 100000},
            {"id": "303", "name": "👍 لايكات يوتيوب",             "price_per_1k": 1.00, "min": 50,   "max": 5000},
            {"id": "304", "name": "⏱ ساعات مشاهدة",              "price_per_1k": 8.00, "min": 100,  "max": 5000},
        ]
    },
    "twitter": {
        "name": "🐦 Twitter / X",
        "services": [
            {"id": "401", "name": "👥 متابعين تويتر",             "price_per_1k": 3.00, "min": 100,  "max": 10000},
            {"id": "402", "name": "❤️ لايكات تويتر",              "price_per_1k": 0.80, "min": 50,   "max": 10000},
            {"id": "403", "name": "🔁 ريتويت",                    "price_per_1k": 1.20, "min": 50,   "max": 10000},
        ]
    },
    "facebook": {
        "name": "📘 Facebook",
        "services": [
            {"id": "501", "name": "👥 متابعين صفحة",              "price_per_1k": 2.50, "min": 100,  "max": 10000},
            {"id": "502", "name": "❤️ لايكات صفحة",               "price_per_1k": 1.00, "min": 100,  "max": 10000},
            {"id": "503", "name": "👁 مشاهدات فيديو فيسبوك",      "price_per_1k": 0.50, "min": 1000, "max": 100000},
        ]
    },
    "snapchat": {
        "name": "👻 Snapchat",
        "services": [
            {"id": "601", "name": "👥 متابعين سناب",               "price_per_1k": 4.00, "min": 100,  "max": 5000},
            {"id": "602", "name": "👁 مشاهدات قصص",                "price_per_1k": 0.80, "min": 500,  "max": 50000},
        ]
    },
}

def find_service(service_id: str):
    """البحث عن خدمة بمعرفها"""
    for platform_data in PLATFORMS.values():
        for svc in platform_data["services"]:
            if svc["id"] == service_id:
                return svc
    return None

def calc_price(service: dict, quantity: int) -> float:
    """حساب السعر الإجمالي"""
    return round((service["price_per_1k"] / 1000) * quantity, 4)
