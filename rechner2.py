def rechner(operator):
    zahl1 = input("Gib eine Zahl ein: ")
    zahl2 = input("Gib eine weitere Zahl ein: ")
    string = zahl1 + operator + zahl2
    return eval(string)


op = input("Gib einen Operator ein: ")
print(rechner(op))
