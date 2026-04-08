from config import UNSAFE_KEYWORDS

def check_input(user_input):
    for word in UNSAFE_KEYWORDS:
        if word in user_input.lower():
            return False, word
    return True, None