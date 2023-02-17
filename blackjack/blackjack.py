import random

g1 = 500
g2 = 500


print("Spieler(1) sie haben ", g1, "€")
print("Spieler(2) sie haben ", g2, "€")
while g1 or g2 > 0:

    black1 = 0
    black2 = 0
    dealer_gezogen = 0
    y = 1

    print("")
    print("----------------------------------------------------")
    print("")

    spieler_gezogen = 0
    if g1 > 0:
        while spieler_gezogen == 0:

            ein1 = int(input("Spieler(1) wie viel möchten sie stetzen: "))
            if ein1 > g1 or ein1 <= 0:
                print("Bitte einen richtigen Betrag eingeben")
                continue
            spieler_gezogen = 1
    spieler_gezogen = 0
    if g2 > 0:
        while spieler_gezogen == 0:
            ein2 = int(input("Spieler(2) wie viel möchten sie stetzen: "))
            if ein2 > g2 or ein2 <= 0:
                print("Bitte einen richtigen Betrag eingeben")
                continue
            spieler_gezogen = 1

    p1 = [random.randrange(2, 12), random.randrange(2, 12)]
    p2 = [random.randrange(2, 12), random.randrange(2, 12)]
    d = [random.randrange(2, 12), random.randrange(2, 12)]
    dsum = sum(d)
    print("Der dealer hat[", d[0], "]")
    print("")

    if g1 > 0:
        print("Spieler(1) du hast", p1, "=", "[", sum(p1), "]")
        if 11 in p1:
            a3 = int(input("Wollen sie eine 11(Ass) zu einer 1 machen: "))

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
                a1 = int(input("Wollen sie noch eine Karte Spieler(1): "))

                if a1 == 1:
                    p1 = p1 + [random.randrange(2, 12), ]
                    print(p1, "= ", "[", sum(p1), "]")
                elif a1 == 0:
                    if 11 in p1:
                        a3 = int(
                            input("Wollen sie eine 11(Ass) zu einer 1 machen: "))
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

    if g2 > 0:
        print("Spieler(2) du hast", p2, "=", "[", sum(p2), "]")
        if 11 in p2:
            a3 = int(input("Wollen sie eine 11(Ass) zu einer 1 machen: "))
            if a3 == 1:
                p2[p2.index(11)] = 1
                print("11 wurde zu 1", p2, "= ", "[", sum(p2), "]")
    if g2 > 0:
        if sum(p2) == 21:
            print("BlackJack!!!3x")
            black2 = 1
            g2 = g2 + (ein2 * 3)
        else:
            while sum(p2) < 21:
                a1 = int(input("Wollen sie noch eine Karte Spieler(2): "))

                if a1 == 1:
                    p2 = p2 + [random.randrange(2, 12), ]
                    print(p2, "=", "[", sum(p2), "]")
                elif a1 == 0:
                    if 11 in p2:
                        a3 = int(
                            input("Wollen sie eine 11(Ass) zu einer 1 machen: "))
                        if a3 == 1:
                            p2[p2.index(11)] = 1
                            print("11 wurde zu 1", p2, "= ", "[", sum(p2), "]")
                            continue

                    break
                else:
                    print("bitte auf eingabe achten")
            else:
                if 11 in p2:

                    p2[p2.index(11)] = 1
                    print("11 wurde zu 1", p2, "= ", "[", sum(p2), "]")

    print("")
    print("Der dealer hat eigentlich", d, "= ", "[", sum(d), "]")
    while dsum <= 17:
        d = d + [random.randrange(2, 12), ]
        dealer_gezogen = 1
        dsum = sum(d)
    if dealer_gezogen == y:
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
    print("Spieler(1) sie haben jetzt", g1, "€")
    if black2 != 1:
        if sum(p2) <= 21:
            if sum(d) <= 21:
                if sum(p2) > sum(d):
                    g2 = g2 + ein2
                elif sum(p2) == sum(d):
                    g2 = g2
                else:
                    g2 = g2 - ein2
            elif sum(p2) <= 21:
                g2 = g2 + ein2
            else:
                g2 = g2 - ein2
        else:
            g2 = g2 - ein2
    print("Spieler(2) sie haben jetzt", g2, "€")
else:
    print("Ende")
