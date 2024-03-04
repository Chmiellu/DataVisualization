import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('dane.csv', sep=';', decimal=',', index_col=0)
dane['Sprzedaz całkowita'] = dane['prodA'] + dane['prodB']
dane_styczen = dane[dane['Miesiac'] == 'styczen']
dane_marzec = dane[dane['Miesiac'] == 'marzec']

plt.figure(figsize=(6, 4))
plt.barh(y=0, width=dane_marzec['Sprzedaz całkowita'].sum(), color='green', label='Marzec', height=0.3)
plt.barh(y=1, width=dane_styczen['Sprzedaz całkowita'].sum(), color='blue', label='Styczeń', height=0.3)
plt.yticks([0, 1], ['Marzec', 'Styczeń'])
plt.title('Porównanie sprzedaży za styczeń i marzec')
plt.xlabel('Sprzedaż całkowita w tysiącach')
plt.legend()
plt.show()