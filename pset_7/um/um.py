import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(s):
    # Using \b to match "um" as a whole word and making it case-insensitive with re.IGNORECASE flag
    pattern = re.compile(r'\bum\b', re.IGNORECASE)
    result = pattern.findall(s)

    return len(result)


if __name__ == "__main__":
    main()
