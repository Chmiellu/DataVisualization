import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('dane.csv', sep=';', decimal=',', index_col=0)
dane_marzec = dane[dane['Miesiac'] == 'marzec']
dane_marzec = dane_marzec.sort_values(by='prodA', ascending=False)

plt.figure(figsize=(8, 6))
plt.scatter(dane_marzec['prodA'], dane_marzec['prodB'], color='blue', alpha=0.5)
plt.title('Sprzedaż Produktu A vs. Produktu B w Marcu')
plt.xlabel('Sprzedaż Produktu A')
plt.ylabel('Sprzedaż Produktu B')
plt.grid(True)
plt.show()
