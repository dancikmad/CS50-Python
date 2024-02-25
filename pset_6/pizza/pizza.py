from sys import argv, exit
import csv
from tabulate import tabulate


if len(argv) != 2:
    if len(argv) < 2:
        exit("Too few command-line arguments")
    else:
        exit("Too many command-line arguments")


filename = argv[1]

dot = filename.find(".")
if filename[dot:] != ".csv":
    exit("Not a CSV file")


try:

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        table = []
        headers = list(next(reader))
        for row in reader:
            table.append([row[0], row[1], row[2]])

    print(tabulate(table, headers, tablefmt="grid"))

except FileNotFoundError:
    exit('File does not exist')
except Exception as arg:
    exit(arg)



