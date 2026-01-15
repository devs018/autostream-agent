# agent.py
from intent import detect_intent
from rag import get_answer
from tools import mock_lead_capture

# agent.py
from intent import detect_intent
from rag import get_answer
from tools import mock_lead_capture

class AutoStreamAgent:
    def __init__(self):
        self.memory = []

    def respond(self, user_message):
        self.memory.append(user_message)
        if len(self.memory) > 6:
            self.memory.pop(0)

        intent = detect_intent(user_message)

        # 🔥 HIGH INTENT FLOW
        if intent == "high_intent":
            print("Agent: Great! I just need a few details to get you started.")
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            platform = input("Your platform (YouTube/Instagram/etc.): ")
            mock_lead_capture(name, email, platform)
            return "Thank you! Your lead has been captured successfully."

        # NORMAL FLOW
        return get_answer(intent)


