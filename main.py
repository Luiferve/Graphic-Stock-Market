import requests
import pandas as pd
import matplotlib.pyplot as plt


def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

# Funcionalidad mínima: REQUISITO
# Datos de empresas


wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/AAPL.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/AIG.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/AMZN.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/AXP.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/BA.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/BAC.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CAJ.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CAT.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CL.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CMCSA.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/COP.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CSCO.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CVC.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CVS.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CVX.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/DD.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/DELL.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/F.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/GD.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/GE.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/GS.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/GSK.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/HD.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/HMC.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/HPQ.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/IBM.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/JPM.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/K.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/KMB.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/KO.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/MAR.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/MCD.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/MMM.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/MSFT.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/NAV.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/NOC.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/NVS.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/PEP.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/PFE.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/PG.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/R.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/RTN.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/SAP.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/SNE.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/SNY.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/TM.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/TOT.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/TWX.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/TXN.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/UN.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/VLO.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/WFC.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/WMT.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/XOM.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/XRX.csv")
wget("https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/YHOO.csv")


print('Ingrese las empresas que desea comparar: ')
ea = str(input('Empresa A. ej:(AAPL): ')) + ".csv"
eb = str(input('Empresa B. ej:(BAC): ')) + ".csv"

ea_file = pd.read_csv(ea)
eb_file = pd.read_csv(eb)
ea_list = ea_file.to_dict("list")
eb_list = eb_file.to_dict("list")

# print(ea_list)
# print(eb_list)

plt.figure(figsize=(16, 8))

# Empiezan con el valor del primer dia
ea_x = [ea_list["date"][0]]
ea_y = [ea_list["open"][0]]
eb_x = [eb_list["date"][0]]
eb_y = [eb_list["open"][0]]

cruce_x = []
cruce_y = []

dif_ea_x = []
dif_eb_x = []
dif_ea_y = []
dif_eb_y = []

data = {}

# range empieza desde 1 en vez de 0
for i in range(1, len(ea_list["date"])):
    ea_x.append(ea_list["date"][i])
    ea_y.append(ea_list["open"][i])
    eb_x.append(eb_list["date"][i])
    eb_y.append(eb_list["open"][i])

    # Para Derivada Discreta
    dif_ea_x.append(ea_list["date"][i])
    dif_eb_x.append(eb_list["date"][i])
    dif_ea_y.append(ea_list["open"][i] - ea_list["open"][i-1])
    dif_eb_y.append(eb_list["open"][i] - eb_list["open"][i-1])

    # Condicional de cruce (son iguales o invirtieron su orden)
    if (eb_y[i] == ea_y[i]) or (eb_y[i] > ea_y[i] and eb_y[i-1] < ea_y[i-1]) or (
            eb_y[i] < ea_y[i] and eb_y[i-1] > ea_y[i-1]):
        cruce_x.append(ea_x[i])
        cruce_y.append(ea_y[i])

# Guardamos los valores de las intercepciones en el Diccionario
data["Fecha"] = cruce_x
data["Valor"] = cruce_y

# Guardamos la informacion en una tabla
dataFrame = pd.DataFrame(data)
# print(dataFrame)

# Exportamos la información a un archivo
dataFrame.to_excel("intercepciones-"+ea+"-"+eb+".xlsx")

plt.subplot(1, 2, 1)
plt.title("Gráfico Comparativo")
plt.plot(ea_x, ea_y, 'g-', label=ea)
plt.plot(eb_x, eb_y, 'r-.', label=eb)
plt.plot(cruce_x, cruce_y, 'k.', label='Puntos de cruce')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.xticks(ea_x[::100], rotation=60)
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Deriva Discreta")
plt.plot(dif_ea_x, dif_ea_y, 'g-', label=ea)
plt.plot(dif_eb_x, dif_eb_y, 'r-.', label=eb)
plt.xlabel('Fecha')
plt.xticks(dif_ea_x[::100], rotation=60)
plt.legend()

plt.show()

# Grafico a entregar: REQUISITO


wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/AMZN.csv")
wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/GOOGLE.csv")

google_file = pd.read_csv("GOOGLE.csv")
amazon_file = pd.read_csv("AMZN.csv")
google = google_file.to_dict("list")
amazon = amazon_file.to_dict("list")

print('Ingrese el intervalo de tiempo: ')
go_date = str(input('Ingrese la fecha inicio (yyyy-mm-dd): '))
gc_date = str(input('Ingrese la fecha cierre (yyyy-mm-dd): '))

plt.figure(figsize=(16, 8))

# Empiezan con el valor del primer dia asignado por el usuario
gx = []
gy = []
ax = []
ay = []
cruce_x = []
cruce_y = []

# range empieza desde un dia despues del asignado
for i in range(0, len(google["Date"])):
    temp_date = google["Date"][i]
    if temp_date < go_date or temp_date > gc_date:
        continue
    gx.append(google["Date"][i])
    gy.append(google["Open"][i])
    ax.append(amazon["Date"][i])
    ay.append(amazon["Open"][i])

    # Condicional de cruce (son iguales o invirtieron su orden)
    previous = len(ay) - 2
    current = len(ay) - 1
    if (ay[current] == gy[current]) or (
            previous >= 0 and (ay[current] > gy[current] and ay[previous] < gy[previous]) or (
            ay[current] < gy[current] and ay[previous] > gy[previous])):
        cruce_x.append(gx[current])
        cruce_y.append(gy[current])

plt.plot(gx, gy, 'g', label='Google')
plt.plot(ax, ay, 'r-.', label='Amazon')
plt.plot(cruce_x, cruce_y, 'k.', label='Puntos de cruce')
plt.xticks(gx[::100], rotation=60)
plt.legend()
plt.savefig('Grafico-comparativo.png')
plt.show()
