def evaluate_greeting(greeting, sub='hello', values=("$0", "$20", "$100")):

    greeting = greeting.lower().strip()

    if sub in greeting:
        return values[0]
    elif sub[0] == greeting[0]:
        return values[1]
    else:
        return values[2]


# Test
greeting_input = input("Greeting: ")
print(evaluate_greeting(greeting_input))

