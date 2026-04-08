from datetime import datetime

def log_interaction(user_id, user_input, response, status):
    with open("logs.txt", "a", encoding="utf-8") as file:
        file.write(f"\n[{datetime.now()}]\n")
        file.write(f"User ID: {user_id}\n")
        file.write(f"Type: {status}\n")
        file.write(f"Input: {user_input}\n")
        file.write(f"Output: {response}\n")