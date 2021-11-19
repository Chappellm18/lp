# Ackermann function
def ackermann(x, y):
    if x == 0:
        return y + 1
    elif y == 0 and x > 0:
        return ackermann(x-1, 1)
    elif y > 0 and x > 0:
        return ackermann(x-1, ackermann(x, y-1))
    else:
        return "Error"


def main():
    x = 0
    while True:
        print("In: " + str(x))
        print("Out: " + str(ackermann(x, x)))
        x += 1


main()
