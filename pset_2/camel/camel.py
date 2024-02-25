import re

def main():
    strng = input("Name a variable: ")
    snake_case = convert_to_snake_case(strng)
    print(snake_case)

def convert_to_snake_case(strng):
    """Initialize a function to convert camelCase to snake_case"""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', strng).lower()


if __name__ == "__main__":
    main()


