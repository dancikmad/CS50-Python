from contextlib import contextmanager
from colorama import Fore
import os
import time


class Personalized:
    def __init__(self, sender_name, receiver_name):
        self.sender_name = sender_name
        self.receiver_name = receiver_name
        self.file = f"{self.sender_name}_personalized.txt"

    def __enter__(self):
        try:
            self.opened_file = open(self.file, "w")
            self.opened_file.write(f"Dear {self.receiver_name},\n\n")
            return self.opened_file
        except IOError as e:
            print(f"Error: {e}")
            # Re-raise the exception
            raise

    def __exit__(self, *exec):
        try:
            self.opened_file.write(f"\nSincerely, \n\n{self.sender_name}")
        finally:
            self.opened_file.close()


@contextmanager
def generic(card_type, sender_name, recipient):
    try:
        template_generic_card = open(card_type, "r")
        new_generic_card = open(f"{sender_name}_generic.txt", "w")
        new_generic_card.write(f"Dear {recipient}\n\n")
        new_generic_card.write(f"{template_generic_card.read()}\n")
        new_generic_card.write(f"Sincerely, \n\n{sender_name}")
        yield new_generic_card
    finally:
        template_generic_card.close()
        new_generic_card.close()


def create_generic_card():
    card_types = {
        "Thank You Card": "thankyou_card.txt",
        "Happy Birthday Card": "happy_bday.txt",
        "Encourangement": "encourangement.txt",
        "Sympathy": "sympathy.txt",
        "Mother's/Father's Day": "mothers_fathers_day.txt",
    }

    sender_name = input("Enter your name: ")
    recipient = input("Enter the name of the recipient: ")

    print("\nWe generate cards for the following occassions.\n")
    for i, card in enumerate(card_types.keys()):
        print(f"{i}. {card}")

    while True:
        try:
            user_choice = int(
                input(
                    "\nPlease select a number for the occassion you want to send card: "
                )
            )
            if user_choice in [i for i, _ in enumerate(card_types)]:
                break
            else:
                print("Sorry, the number you entered is not available.")

        except ValueError:
            print("Please enter a number.")

    for i, value in enumerate(card_types.values()):
        if user_choice == i:
            with generic(f"{value}", sender_name, recipient) as generic_card:
                print("\nThe card has been generated!")
                print("Redirecting back to the menu ...")
                time.sleep(2)
                clear_screen


def write_message():
    lines = []
    print("\nEnter your message (press Enter twiceto finish): ")
    while True:
        try:
            line = input()
            if line == "":
                # Check if the user entered an empty line
                if lines:
                    # If there are already lines entered, consider this as the end of input
                    break
                else:
                    # If no lines have been entered yet, continue to next iteration
                    continue
            lines.append(line)
        except KeyboardInterrupt:
            # Handle Ctrl+C to exit without losing entered lines
            break

    return "\n".join(lines)


def display_menu():

    menu = "\nPlease choose one of the following options.\n"
    menu += "1 - Generate a generic card.\n"
    menu += "2 - Generate a personalized card.\n\n"
    menu += 'If you wish to quit enter "quit" or "q":'

    print(Fore.BLUE + menu)


def clear_screen():
    os.system("cls||clear")


def main():
    print(Fore.BLUE + "Welcome to Create Your Card - ASAP")

    while True:

        display_menu()
        user_choice = input().strip().lower()

        if user_choice == "q" or user_choice == "quit":
            print("\nThank you for choosing our services. Good luck 🤗")
            break

        if user_choice == "1":
            # clear_screen()
            print("You have selected to create a generic card.")
            create_generic_card()

        elif user_choice == "2":
            clear_screen()
            print("You have selected to create a personalized card.\n")
            sender_name = input("Please enter your name (Sender): ").title()
            reciver_name = input(
                "Please enter the name of the receiver (Recipient): "
            ).title()
            msg = write_message()
            if msg:
                try:
                    with Personalized(sender_name, reciver_name) as personalized_card:
                        personalized_card.write(msg)
                        print("\bThe personalized card has been generated!\n")
                except IOError as e:
                    print(f"Error: {e}")
                    break
            else:
                print("Message cannot be empty.")
        else:
            clear_screen()
            print("\nWrong choice. Redirectering back to the menu ...")
            time.sleep(2)


if __name__ == "__main__":
    main()
