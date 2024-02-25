def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif not s.isalnum():
        return False
    elif not s[:2].isalpha():
        return False
    first_num = len(s) - 1
    for char in s:
        if char.isnumeric():
            if char == '0':
                return False
            first_num = s.index(char)
            break
    for char in s:
        if s.index(char) <= first_num:
            pass
        else:
            if char.isalpha():
                return False
    return True


if __name__ == "__main__":
    main()
