def main():
    prompt = input("Greeting: ")
    money = value(prompt)
    print(f"${money}")



def value(greeting, sub='hello', values=("0", "20", "100")):

    greeting = greeting.lower().strip()


    if sub in greeting:
        return int(values[0])
    elif sub[0] == greeting[0]:
        return int(values[1])
    else:
        return int(values[2])

if __name__ == '__main__':
    main()
