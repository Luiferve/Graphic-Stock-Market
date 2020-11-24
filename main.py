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


# Diccionario de empresas disponibles.
stock = ['AAPL', 'AIG', 'AMZN', 'AXP', 'BA', 'BAC', 'CAJ', 'CAT', 'CL', 'CMCSA',
         'COP', 'CSCO', 'CVC', 'CVS', 'CVX', 'DD', 'DELL', 'F', 'GD', 'GE', 'GS',
         'GSK', 'HD', 'HMC', 'HPQ', 'IBM', 'JPM', 'K', 'KMB', 'KO', 'MAR', 'MCD',
         'MMM', 'MSFT', 'NAV', 'NOC', 'NVS', 'PEP', 'PFE', 'PG', 'R', 'RTN', 'SAP',
         'SNE', 'SNY', 'TM', 'TOT', 'TWX', 'TXN', 'UN', 'VLO', 'WFC', 'WMT',
         'XOM', 'XRX', 'YHOO']

for accion in stock:
    print(accion)

print('Ingrese las acciones que desea comparar: ')

ea = input(str('Accion A. ej:(AAPL): '))
while not (ea in stock):  # Condicional para seleccion de empresa (Solo entre las disponibles).
    ea = input(str('Intente nuevamente con una accion existente. ej:(AAPL): '))

eb = input(str('Accion B. ej:(BAC): '))
while not (eb in stock) or (eb == ea):
    eb = input(str('Intente nuevamente con una accion existente. ej:(BAC): '))

# Agregamos la extension del archivo para cuando lo busque en el sistema.
ea = ea + ".csv"
eb = eb + ".csv"

ea_file = pd.read_csv(ea)
eb_file = pd.read_csv(eb)
ea_list = ea_file.to_dict("list")
eb_list = eb_file.to_dict("list")

# Empiezan con el valor del primer dia.
ea_x = [ea_list["date"][0]]
ea_y = [ea_list["open"][0]]
eb_x = [eb_list["date"][0]]
eb_y = [eb_list["open"][0]]

cruce_x = []
cruce_y = []

# Empiezan vacias para poder calcular la Derivada Diferencial entre el primer y segundo valor.
dif_ea_x = []
dif_eb_x = []
dif_ea_y = []
dif_eb_y = []

data_intercepcion = {}  # Diccionario vacio para los valores comunes entres las acciones a guardar en excel.

ea_sep_done = False # Boolean para medir el mes.
ea_oct_done = False
ea_nov_done = False
ea_jan_done = False
ea_year_opening = 0
ea_year_closing = ea_list["close"][len(ea_list["close"]) - 1] # Ultimo valor de la accion.
ea_sep_opening = 0
ea_sep_closing = 0
ea_oct_opening = 0
ea_oct_closing = 0
data_ea = {}

eb_sep_done = False
eb_oct_done = False
eb_nov_done = False
eb_jan_done = False
eb_year_opening = 0
eb_year_closing = eb_list["close"][len(eb_list["close"]) - 1]
eb_sep_opening = 0
eb_sep_closing = 0
eb_oct_opening = 0
eb_oct_closing = 0
data_eb = {}

plt.figure(figsize=(16, 8))

# range empieza desde 1 en vez de 0 para comparar con el primer valor.
for i in range(1, len(ea_list["date"])):
    ea_temp_date = ea_list["date"][i]
    eb_temp_date = eb_list["date"][i]
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
    if (eb_y[i] == ea_y[i]) or (eb_y[i] > ea_y[i] and eb_y[i-1] < ea_y[i-1]) or (eb_y[i] < ea_y[i] and eb_y[i-1] > ea_y[i-1]):
        cruce_x.append(ea_x[i])
        cruce_y.append(ea_y[i])

    # Condicional de valor de la accion por fechas.
    if not ea_jan_done and (ea_temp_date >= '2007-01-01'):
        ea_year_opening = ea_list["open"][i]
        ea_jan_done = True
    if not ea_sep_done and (ea_temp_date >= '2007-09-01'):
        ea_sep_opening = ea_list["open"][i]
        ea_sep_done = True
    if not ea_oct_done and (ea_temp_date >= '2007-10-01'):
        ea_oct_opening = ea_list["open"][i]
        ea_sep_closing = ea_oct_opening
        ea_oct_done = True
    if not ea_nov_done and (ea_temp_date >= '2007-11-01'):
        ea_nov_opening = ea_list["open"][i]
        ea_oct_closing = ea_nov_opening
        ea_nov_done = True

    # Condicional de valor de la accion por fechas.
    if not eb_jan_done and (eb_temp_date >= '2007-01-01'):
        eb_year_opening = eb_list["open"][i]
        eb_jan_done = True
    if not eb_sep_done and (eb_temp_date >= '2007-09-01'):
        eb_sep_opening = eb_list["open"][i]
        eb_sep_done = True
    if not eb_oct_done and (eb_temp_date >= '2007-10-01'):
        eb_oct_opening = eb_list["open"][i]
        eb_sep_closing = eb_oct_opening
        eb_oct_done = True
    if not eb_nov_done and (eb_temp_date >= '2007-11-01'):
        eb_nov_opening = eb_list["open"][i]
        eb_oct_closing = eb_nov_opening
        eb_nov_done = True

# Calculo del porcentaje de crecimiento de la accion A.
ea_year_grow = ((ea_year_closing/ea_year_opening) - 1) * 100
ea_sep_grow = ((ea_sep_closing/ea_sep_opening) - 1) * 100
ea_oct_grow = ((ea_oct_closing/ea_oct_opening) - 1) * 100

# Guardamos los valores de las intercepciones en el Diccionario
data_ea["% de Crecimiento Anual"] = ea_year_grow
data_ea["% de Crecimiento en el ultimo mes"] = ea_sep_grow
data_ea["% de Crecimiento en el penultimo mes"] = ea_oct_grow

# Guardamos la informacion en una tabla
dataFrame = pd.DataFrame({'Valor':data_ea})

# Exportamos la información a un archivo
dataFrame.to_excel("Porcentaje-Crecimiento-"+ea+".xlsx")

# Calculo del porcentaje de crecimiento de la accion B.
eb_year_grow = ((eb_year_closing/eb_year_opening) - 1) * 100
eb_sep_grow = ((eb_sep_closing/eb_sep_opening) - 1) * 100
eb_oct_grow = ((eb_oct_closing/eb_oct_opening) - 1) * 100

# Guardamos los valores de las intercepciones en el Diccionario
data_eb["% de Crecimiento Anual"] = eb_year_grow
data_eb["% de Crecimiento en el ultimo mes"] = eb_sep_grow
data_eb["% de Crecimiento en el penultimo mes"] = eb_oct_grow

# Guardamos la informacion en una tabla
dataFrame = pd.DataFrame({'Valor':data_eb})

# Exportamos la información a un archivo
dataFrame.to_excel("Porcentaje-Crecimiento-"+eb+".xlsx")

# Guardamos los valores de las intercepciones en el Diccionario
data_intercepcion["Fecha"] = cruce_x
data_intercepcion["Valor"] = cruce_y

# Guardamos la informacion en una tabla
dataFrame = pd.DataFrame(data_intercepcion)

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
