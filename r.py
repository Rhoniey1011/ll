import requests
import random
import string
import os
from art import text2art

GREEN = "\033[32;1m"
YELLOW = "\033[33;1m"
RED = "\033[31;1m"
CYAN = "\033[36;1m"
MAGENTA = "\033[35;1m"
BOLD = "\033[1m"
RESET = "\033[0m"

def log_green(message):
    print(GREEN + BOLD + message + RESET)

def log_yellow(message):
    print(YELLOW + BOLD + message + RESET)

def log_red(message):
    print(RED + BOLD + message + RESET)

def log_cyan(message):
    print(CYAN + BOLD + message + RESET)

def log_magenta(message):
    print(MAGENTA + BOLD + message + RESET)

def generate_random_string(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_email():
    return f"user_{generate_random_string(8)}@example.com"

def generate_password():
    return generate_random_string(12)

def perform_signup(email, password, display_name, referral_code):
    url = "https://example.com/api/signup"
    payload = {
        "email": email,
        "password": password,
        "display_name": display_name,
        "referral_code": referral_code
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.status_code == 200
    except Exception:
        return False

def main():
    os.system("clear" if os.name != "nt" else "cls")
    print(text2art("Python Bot"))

    log_cyan("Enter referral code:")
    referral_code = input().strip()

    log_cyan("Enter number of accounts to register:")
    count = int(input().strip())

    index = 1
    for _ in range(count):
        email = generate_email()
        password = generate_password()
        display_name = "User" + generate_random_string(4)

        log_yellow(f"Registering account number {index}")
        success = perform_signup(email, password, display_name, referral_code)

        if success:
            log_green(f"Account number {index} registration finished with successful result")
        else:
            log_red(f"Account number {index} registration finished with failure result")

        index += 1

    log_green("All planned registration tasks have been processed")

if __name__ == "__main__":
    main()
