def main():
    prompt = input("Input: ")
    modified_str = shorten(prompt)

    print(f"Output: {modified_str}")


def shorten(word):
    new_word = []
    for char in word:
        if char not in "aeiou":
            new_word.append(char)

    return "".join(new_word)


if __name__ == "__main__":
    main()
