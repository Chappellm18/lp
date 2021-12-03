# Ackermann function
def acker1(x, y):

    if x == 0:
        return y + 1
    elif y == 0:
        return acker1(x - 1, 1)
    else:
        return acker1(x - 1, acker1(x, y - 1))


def main():
    x = 0
    while True:
        print("In: " + str(x))
        print("Out: " + str(acker1(x, x)))
        x += 1


main()
