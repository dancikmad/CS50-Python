from sys import argv, exit
import csv


students = []

if len(argv) != 3:
    if len(argv) < 3:
        exit("Too few command-lines arguments")
    else:
        exit("Too many command-line arguments")

try:
    with open(argv[1], 'r') as read_file, open(argv[2], 'w') as write_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            splitted_name = row["name"].split(",")
            students.append({
                "first": splitted_name[1].lstrip(),
                "last": splitted_name[0],
                "house": row["house"]
            })
        writer = csv.DictWriter(write_file, fieldnames=["first", "last", "house"])
        writer.writerow({
            "first": "first",
            "last": "last",
            "house": "house"
        })
        for row in students:
            writer.writerow({
                "first": row["first"],
                "last": row["last"],
                "house": row["house"]
            })

except FileNotFoundError:
    exit(f"Could not read {argv[1]}")
except Exception as arg:
    exit(arg)


    