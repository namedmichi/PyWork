import random

g1 = 500


print("Spieler 1 sie haben ", g1, "€")

while g1 > 0:

    black1 = 0

    dealerhatgezogen = 0
    y = 1

    print("")
    print("----------------------------------------------------")
    print("")

    pp = 0
    if g1 > 0:
        while pp == 0:

            ein1 = int(input("Spieler 1 wie viel möchten sie stetzen "))
            if ein1 > g1 or ein1 <= 0:
                print("Bitte einen richtigen Betrag eingeben")
                continue
            pp = 1
    pp = 0

    p1 = [random.randrange(2, 12), random.randrange(2, 12)]

    d = [random.randrange(2, 12), random.randrange(2, 12)]
    dsum = sum(d)
    print("Der dealer hat[", d[0], "]")
    print("")

    if g1 > 0:
        print("Spieler 1 du hast", p1, "=", "[", sum(p1), "]")
        if 11 in p1:
            a3 = input("Wollen sie eine 11(Ass) zu einer 1 machen ")

            if a3 == 1:
                p1[p1.index(11)] = 1
                print("11 wurde zu 1", p1, "= ", "[", sum(p1), "]")

    if g1 > 0:
        if sum(p1) == 21:
            print("BlackJack!!!3x")
            black1 = 1
            g1 = g1 + (ein1 * 3)
        else:
            while sum(p1) < 21:
                a1 = int(input("Wollen sie noch eine Karte Spieler1 "))

                if a1 == 1:
                    p1 = p1 + [random.randrange(2, 12), ]
                    print(p1, "= ", "[", sum(p1), "]")
                elif a1 == 0:
                    if 11 in p1:
                        a3 = input(
                            "Wollen sie eine 11(Ass) zu einer 1 machen ")
                        if a3 == 1:
                            p1[p1.index(11)] = 1
                            print("11 wurde zu 1", p1, "= ", "[", sum(p1), "]")
                            continue

                    break

                else:
                    print("bitte auf eingabe achten")
            else:
                if 11 in p1:

                    p1[p1.index(11)] = 1
                    print("11 wurde zu 1", p1, "= ", "[", sum(p1), "]")

    print("")
    print("Der dealer hat eigentlich", d, "= ", "[", sum(d), "]")
    while dsum <= 17:
        d = d + [random.randrange(2, 12), ]
        dealerhatgezogen = 1
        dsum = sum(d)
    if dealerhatgezogen == y:
        print("Er zieht nochmal und hat jetzt", d, "= ", "[", sum(d), "]")
    if black1 != 1:
        if sum(p1) <= 21:
            if sum(d) <= 21:
                if sum(p1) > sum(d):
                    g1 = g1 + ein1
                elif sum(p1) == sum(d):
                    g1 = g1
                else:
                    g1 = g1 - ein1
            elif sum(p1) <= 21:
                g1 = g1 + ein1
            else:
                g1 = g1 - ein1
        else:
            g1 = g1 - ein1
    print("")
    print("Spieler1 sie haben jetzt", g1, "€")

else:
    print("Ende")
