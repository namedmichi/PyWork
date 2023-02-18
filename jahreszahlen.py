jahreszahl = int(input("geben sie eine jahreszahl ein: "))


def my_mod(j, o):
    if j % o == 0:
        return True


if my_mod(jahreszahl, 4):
    if my_mod(jahreszahl, 100):
        if my_mod(jahreszahl, 400):
            print("Schaltjahr")
            exit()
        print("Kein Schaltjahr")
        exit()
    print("Schaltjahr")
    exit()
print("Kein Schaltjahr")
