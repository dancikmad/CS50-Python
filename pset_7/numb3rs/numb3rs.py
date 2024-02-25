# A program that expects an IPv4 address as input as str
# Validates the address for True | False

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    numbers = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if numbers:
        for number in numbers.groups():
            if not (0 <= int(number) <= 255):
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
