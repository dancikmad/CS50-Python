from datetime import date
import inflect
import sys
import operator

p = inflect.engine()


def main():

    dob = input("Date of Birth: ")
    time_words = convert_time_in_words(dob)
    print(time_words)


def convert_time_in_words(birthday_date: str) -> str:
    try:
        year, month, day = birthday_date.split("-")
        birthday_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    difference = operator.sub(date.today(), birthday_date)
    difference_mins = difference.days * 24 * 60
    time_in_words = p.number_to_words(difference_mins, andword="")

    return f"{time_in_words.capitalize()} minutes"


if __name__ == "__main__":
    main()
