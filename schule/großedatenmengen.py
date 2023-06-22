# Um das Programm zu trainieren werden große Datenmengen benötigt.
import matplotlib.pyplot as plt
import numpy as np

feature = np.array([[4.0, 37.92655435, 23.90101111],   # Hund
                    [4.0, 35.88942857, 22.73639281],   # Hund
                    [4.0, 29.49674574, 21.42168559],   # Hund
                    [4.0, 32.48016326, 21.7340484],   # Hund
                    [4.0, 38.00676226, 24.37202837],   # Hund
                    [4.0, 30.73073988, 22.69832608],   # Hund
                    [4.0, 35.93672343, 21.07445241],   # Hund
                    [4.0, 38.65212459, 20.57099727],   # Hund
                    [4.0, 35.52041768, 21.74519457],   # Hund
                    [4.0, 37.69535497, 20.33073640],   # Hund
                    [4.0, 33.00699292, 22.57063861],   # Hund
                    [4.0, 33.73140934, 23.81730782],   # Hund
                    [4.0, 43.85053380, 20.05153803],   # Hund
                    [4.0, 32.95555986, 24.12153986],   # Hund
                    [4.0, 36.38192916, 19.20280266],   # Hund
                    [4.0, 36.54270168, 20.45388966],   # Hund
                    [4.0, 33.08246118, 22.20524015],   # Hund
                    [4.0, 31.76866280, 21.01201139],   # Hund
                    [4.0, 42.24260825, 20.44394610],   # Hund
                    [4.0, 29.04450264, 22.46633771],   # Hund
                    [4.0, 30.04284328, 21.54561621],   # Hund
                    [4.0, 18.95626707, 19.66737753],   # Kein Hund
                    [4.0, 18.60176718, 17.74023009],   # Kein Hund
                    [4.0, 12.85314993, 18.42746953],   # Kein Hund
                    [4.0, 28.62450072, 17.94781944],   # Kein Hund
                    [4.0, 21.00655655, 19.33438286],   # Kein Hund
                    [4.0, 17.33580556, 18.81696459],   # Kein Hund
                    [4.0, 31.17129195, 17.23625014],   # Kein Hund
                    [4.0, 19.36176482, 20.67772798],   # Kein Hund
                    [4.0, 27.26581705, 16.71312863],   # Kein Hund
                    [4.0, 21.19107828, 19.00673617],   # Kein Hund
                    [4.0, 19.08131597, 15.24401994],   # Kein Hund
                    [4.0, 26.69761925, 17.05937466],   # Kein Hund
                    [2.0, 4.44136559, 3.52432493],   # Kein Hund
                    [2.0, 10.26395607, 1.07729281],   # Kein Hund
                    [2.0, 7.39058439, 3.44234423],   # Kein Hund
                    [2.0, 4.23565118, 4.28840232],   # Kein Hund
                    [2.0, 3.87875761, 5.12407692],   # Kein Hund
                    [2.0, 15.12959925, 6.26045879],   # Kein Hund
                    [0.0, 5.93041263, 1.70841905],   # Kein Hund
                    [0.0, 4.25054779, 5.01371294],   # Kein Hund
                    [0.0, 2.15139117, 4.16668657],   # Kein Hund
                    [0.0, 2.38283228, 3.83347914]])   # Kein Hund

print(feature.shape)

# Erstellen der Label mit der NumPy "Verketten-Funktion" und den NumPy Funktionen "ones" und "zeros"
label = np.concatenate((np.ones(21), np.zeros(22)))


# Versuch Nr. 2.
plt.title('Trainingsdaten')     # Benennung des Plotts
plt.xlabel('Höhe in cm')  # Benennung der X-Achse
plt.ylabel('Größe in cm')       # Benennung der X-Achse

plt.scatter(feature[:, 2], feature[:, 1], c=label)

plt.show()
