a = 53782
b = 72534


def collatz(a, b):
    countera = 0
    counterb = 0
    while not a == 1:
        if a % 2 == 0:
            a = a / 2
            countera = countera + 1
            continue
        else:
            a = (a*3) + 1
            countera = countera + 1
            continue
    while not b == 1:
        if b % 2 == 0:
            b = b / 2
            counterb = counterb + 1
            continue
        else:
            b = (b*3) + 1
            counterb = counterb + 1
            continue
    if countera < counterb:
        return "a"
    else:
        return "b"


print(collatz(a, b))
