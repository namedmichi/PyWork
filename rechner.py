running = True

while running:

    try:
        n1 = int(input("Geben sie die erste Zahl ein: "))
        n2 = int(input("Geben sie die zweite Zahl ein: "))

    except ValueError:
        print('Keine Zahl!')
        continue

    op = input("Geben sie einen Operator ein(a, s, m , d): ")

    match op.lower():
        case "a":
            res = n1 + n2
        case "s":
            res = n1 - n2
        case "m":
            res = n1 * n2
        case "d":
            res = n1 / n2
        case other:
            print("Ungültiger Operator!!! Neu eingeben")
            continue
    print(res)

    while True:
        con = input("Willst du weiter machen(j/n): ")
        if con == "j":
            break
        elif con == "n":
            running = False
            break
        else:
            print("Falsche eingabe!")
            continue
