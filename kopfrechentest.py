from random import randint


maximum = 20
genug = False
richtig = True
eingabe = True


def rechnen(a, b):
    if a == b:
        return True


def eingeben():
    eingabe = True
    while eingabe == True:
        try:
            global ergebnis
            ergebnis = int(input("Ergebnis: "))
            eingabe = False
        except ValueError:
            print("Das ist keine Zahl...")
            eingabe = True


print('Teste deine Kopfrechenfähigkeiten!')
while richtig and (not genug):
    print("Noch ein Test?")
    antwort = input("Antwort (j/n): ")
    if antwort == "j":
        zahl1 = randint(1, maximum)
        zahl2 = randint(1, maximum)
        produkt = zahl1 * zahl2
        print(zahl1, " * ", zahl2)

        eingeben()

        if ergebnis == produkt:
            print("richtig!")
        else:
            print("falsch!!!")
            richtig = False
    else:
        genug = True


