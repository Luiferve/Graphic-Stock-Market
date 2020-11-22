import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

# Funcionalidad mínima: REQUISITO

# 1
# 2
# 3
# 4


wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/AMZN.csv")
wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/GOOGLE.csv")

# Grafico a entregar: REQUISITO

google_file = pd.read_csv("GOOGLE.csv")
amazon_file = pd.read_csv("AMZN.csv")
google = google_file.to_dict("list")
amazon = amazon_file.to_dict("list")

# print(google['Open'])
# print(amazon['Open'])

plt.figure(figsize=(16, 8))

# Empiezan con el valor del primer dia
gx = [google["Date"][0]]
gy = [google["Open"][0]]
ax = [amazon["Date"][0]]
ay = [amazon["Open"][0]]

cruce_x = []
cruce_y = []

# range empieza desde 1 en vez de 0
for i in range(1, len(google["Date"])):
    gx.append(google["Date"][i])
    gy.append(google["Open"][i])
    ax.append(amazon["Date"][i])
    ay.append(amazon["Open"][i])

    # Condicional de cruce (son iguales o invirtieron su orden)
    if (ay[i] == gy[i]) or (ay[i] > gy[i] and ay[i-1] < gy[i-1]) or (ay[i] < gy[i] and ay[i-1] > gy[i-1]):
        cruce_x.append(gx[i])
        cruce_y.append(gy[i])

plt.plot(gx, gy)
plt.plot(ax, ay)
plt.plot(cruce_x, cruce_y, 'k.')
plt.xticks(gx[::100], rotation=60)

plt.show()

# Funcionalidad Opcional
