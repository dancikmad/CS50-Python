import inflect

def main():
    p = inflect.engine()
    my_list = []

    while True:

        try:
            user_input = str(input("Name: ")).strip()
            my_list.append(user_input)
        except (EOFError, KeyError):
            print(f"Adieu, adieu, to {p.join(my_list)}", end="\n")
            quit()


if __name__ == '__main__':
    main()
