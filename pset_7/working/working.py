import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d?\d)(?::(\d\d))? (AM|PM) to (\d?\d)(?::(\d\d))? (PM|AM)"
    if matches := re.search(pattern, s):
        hr1, min1, am_pm1, hr2, min2, am_pm2 = matches.groups()

        if am_pm1 == "AM":
            if hr1 == "12":
                hr1 = "00"
            elif am_pm1 == "PM":
                hr1 = str(int(hr1) + 12)

        elif am_pm1 == "PM":
            hr1 = str(int(hr1) + 12)

        if am_pm2 == "AM":
            if hr2 == "12":
                hr2 = "00"
        elif am_pm2 == "PM":
            if hr2 == "12":
                hr2 == "00"
            else:
                hr2 = str(int(hr2) + 12)

        if min1 is not None and (int(min1) > 59 or int(hr1) > 23):
            raise ValueError

        if min2 is not None and (int(min2) > 59 or int(hr2) > 23):
            raise ValueError

        return f"{hr1.zfill(2)}:{min1.zfill(2) if min1 else '00'} to {hr2.zfill(2)}:{min2.zfill(2) if min2 else '00'}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
