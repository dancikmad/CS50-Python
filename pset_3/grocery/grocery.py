grocery_list = {}

while True:
    try:
        item = input()
        if item not in grocery_list:
            grocery_list[item] = 0
        grocery_list[item] += 1
    except EOFError:
        break

for key, value in sorted(grocery_list.items()):
    print("{} {}".format(value, key.upper()))
