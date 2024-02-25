from validator_collection import validators, checkers


def main():
    print(validate(input("What's your email address? ").strip()))


def validate(s):
    is_email_address = checkers.is_email(s)

    if not is_email_address:
        return "Invalid"
    return "Valid"


if __name__ == "__main__":
    main()
