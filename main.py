from trust.validator import check_input
from trust.logger import log_interaction
from config import MAX_REQUESTS

# Simulated user
user_id = "user_1"

# Rate limiting
request_count = 0


def generate_response(user_input):
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "Hello! How can I assist you today?"
    elif "help" in text:
        return "You can ask me to analyze or process safe requests."
    elif "status" in text:
        return "System is running normally and securely."
    elif "show files" in text:
        return "Simulated Files: file1.txt, report.pdf, data.csv"
    elif "check disk" in text:
        return "Disk usage is at 45% (simulated)."
    else:
        return f"I received your request: '{user_input}'"


def get_trust_score(is_safe):
    return 100 if is_safe else 0


def agent():
    global request_count

    print("🤖 Trusted AI Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("\nSession ended. All interactions logged securely.")
            break

        # Rate limiting check
        request_count += 1
        if request_count > MAX_REQUESTS:
            response = "⚠️ Too many requests. Please try later."
            print("Agent:", response)
            log_interaction(user_id, user_input, response, "RATE_LIMIT")
            break

        # Validate input
        is_safe, keyword = check_input(user_input)

        if not is_safe:
            response = f"⚠️ Action blocked: contains restricted keyword '{keyword}'"
            print("Agent:", response)

            score = get_trust_score(False)
            print(f"Trust Score: {score}")

            log_interaction(user_id, user_input, response, "SECURITY_BLOCK")
            continue

        # Generate response
        response = generate_response(user_input)
        print("Agent:", response)

        score = get_trust_score(True)
        print(f"Trust Score: {score}")

        log_interaction(user_id, user_input, response, "USER_ACTION")


if __name__ == "__main__":
    agent()