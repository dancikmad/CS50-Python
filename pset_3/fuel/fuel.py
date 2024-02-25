while True:
    try:
        x, y = input('Fraction: ').split('/')
        x, y = int(x), int(y)
        if y < x:
            raise Exception
        elif y == 0:
            raise ZeroDivisionError
    except:
        pass
    else:
        break

gauge_tank = (x / y) * 100  # Calculate the percentage in the gauge tank
if gauge_tank <= 1:
    print("E")
elif gauge_tank >= 99:
    print("F")
else:
    print(f"{gauge_tank:.0f}%")
