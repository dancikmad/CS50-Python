str = input()

def convert(str):
    if ":)" in str and ":(" in str:
        str = str.replace(":)", "\U0001F642")
        str = str.replace(":(", "\U0001F641")

    elif ":)" in str:
        str = str.replace(":)", "\U0001F642")
    elif ":(" in str:
        str = str.replace(":(", "\U0001F641")

    return str

print(convert(str))

