
beine = [4, 4, 4, 4, 2]
groesse = [35.6, 28.4, 55.9, 46.1, 5.2]
breite = [32.2, 18.5, 42.8, 39.3, 4.1]
farbe = ["Braun", "Schwarz", "Beige", "Weiß", "Rot"]
label = ["Hund", "Hund", "Hund", "Hund", "nicht Hund"]

feature = {
    'beine': beine,
    'groesse': groesse,
    'breite': breite,
    'farbe': farbe,
    'label': label
}

print(feature["breite"])
print(feature["farbe"][4])
