import matplotlib.pyplot as plt
import numpy as np

xPunkte = np.array([0, 6, 8])
yPunkte = np.array([0, 250, 300])

plt.plot(xPunkte, yPunkte)  # Anweisung zum Plotten
plt.plot(yPunkte, xPunkte)  # Anweisung zum Plotten
plt.show()  # Anweisung zum Zeigen
