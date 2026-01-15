# main.py
from agent import AutoStreamAgent

def main():
    print("Welcome to AutoStream Agent!")
    agent = AutoStreamAgent()

    while True:
        user_msg = input("\nUser: ")
        if user_msg.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break
        response = agent.respond(user_msg)
        print("Agent:", response)

if __name__ == "__main__":
    main()
