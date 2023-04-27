beine = [4,4,4,4,2]
groesse= [30,15,30,20,5]
farbe = ['rot', 'braun', 'braun', 'braun', 'rot']
label = ['hund', 'hund', 'hund', 'hund', 'kein hund']



feature = {
 'beine': beine,
 'groesse': groesse,
 'farbe': farbe,
 'label': label
}

print(feature)
print(feature['groesse'])
print(feature['label'][1])