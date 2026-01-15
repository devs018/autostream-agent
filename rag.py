# rag.py
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KB_PATH = os.path.join(BASE_DIR, "knowledge.json")

with open(KB_PATH, "r") as f:
    knowledge = json.load(f)

def get_answer(intent):
    if intent == "greeting":
        return "Hello! How can I help you today?"

    if intent == "pricing_inquiry":
        basic = knowledge["plans"]["Basic"]
        pro = knowledge["plans"]["Pro"]

        return (
            f"Basic Plan:\n"
            f"- Price: {basic['price']}\n"
            f"- Videos: {basic['videos']}\n"
            f"- Resolution: {basic['resolution']}\n\n"
            f"Pro Plan:\n"
            f"- Price: {pro['price']}\n"
            f"- Videos: {pro['videos']}\n"
            f"- Resolution: {pro['resolution']}\n"
            f"- AI Captions: Yes"
        )

    return "I can help you with AutoStream pricing and plans."
