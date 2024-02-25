def main():
    while True:
        try:
            percentage = convert(input('Fraction: '))
        except:
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    X, Y = fraction.split('/')
    X, Y = int(X), int(Y)
    if Y == 0:
        raise ZeroDivisionError
    elif Y < X:
        raise ValueError
    return int(round(X/Y) * 100)




def gauge(percent):
    if percent <= 1:
        return 'E'
    elif percent >= 99:
        return 'F'
    else:
        return str(percent)


if __name__ == "__main__":
    main()
