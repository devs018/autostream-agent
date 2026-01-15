# intent.py

def detect_intent(user_message):
    msg = user_message.lower()

    # 🔥 HIGH INTENT FIRST (VERY IMPORTANT)
    high_intent_keywords = [
        "sign up", "signup", "register",
        "buy", "purchase", "subscribe",
        "i want", "i want to try", "start",
        "pro plan", "get pro", "try pro"
    ]

    pricing_keywords = [
        "price", "pricing", "cost", "plan", "plans", "features"
    ]

    greetings = ["hi", "hello", "hey"]

    if any(k in msg for k in high_intent_keywords):
        return "high_intent"

    elif any(k in msg for k in pricing_keywords):
        return "pricing_inquiry"

    elif any(k in msg for k in greetings):
        return "greeting"

    else:
        return "unknown"
