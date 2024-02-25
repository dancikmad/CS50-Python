def main():
    prompt = input("What time it is? ")
    time = convert(prompt)
    if time >= convert("7:00") and time <= convert("8:00"):
        print("breakfast time")
    elif time >= convert("12:00") and time <= convert("13:00"):
        print("lunch time")
    elif time >= convert("18:00") and time <= convert("19:00"):
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    total_hours = float(hours) + float(minutes) / 60
    return total_hours


if __name__ == "__main__":
    main()

