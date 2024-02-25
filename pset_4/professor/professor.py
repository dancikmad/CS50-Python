from random import randint

level_glossary = [{1: [0, 9]}, {2: [10, 99]}, {3: [100, 999]}]

def main():

    selected_level = get_level()
    problem_sets = generate_integer(selected_level)

    solved = 0

    for question in problem_sets:
        attempts = 0

        while True:
            try:
                answer = int(input(f"{question} = "))
                a, b = question.strip(" ").split("+")

                if attempts == 2:
                    print("EEE")
                    print(f"{question} = {(int(a) + int(b))}")
                    break
                elif answer != (int(a) + int(b)):
                    attempts += 1
                    print("EEE")
                else:
                    solved += 1
                    attempts = 0
                    break

            except ValueError:
                print("EEE")
                attempts += 1
                continue

    print("{0}: {1}".format("Score", solved))



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            else:
                return level
                break
        except ValueError:
            continue

def generate_integer(level):
    """Generate 10 randomized problems where each level represents x digits"""
    problem_set = []

    rint_lo = level_glossary[level - 1][level][0]
    rint_hi = level_glossary[level - 1][level][1]


    for _ in range(0, 10):
        problem_set.append(f"{randint(rint_lo, rint_hi)} + {randint(rint_lo, rint_hi)}")

    return problem_set


if __name__== "__main__":
    main()



