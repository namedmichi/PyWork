import numpy as np

beine = [4, 4, 4, 4, 2]
groesse = [35.6, 28.4, 55.9, 46.1, 5.2]
breite = [32.2, 18.5, 42.8, 39.3, 4.1]
label = [1, 1, 1, 1, 0]

rohdaten = {
    'beine': beine,
    'groesse': groesse,
    'breite': breite,
    'label': label
}


groesse = np.array(rohdaten['beine'])
zusammen = np.array(rohdaten)


feature = np.array(
    [rohdaten['beine'], rohdaten['groesse'], rohdaten['breite']])


print(feature.T)
print("Durchschnittswert der Beine: ", np.mean(rohdaten['beinef']))

print("Durchschnittswert der Groesse: ", np.mean(rohdaten['groesse']))

print("Durchschnittswert der Breite: ", np.mean(rohdaten['beine']))

print("Durchschnittswert der Label: ", np.mean(rohdaten['label']))
