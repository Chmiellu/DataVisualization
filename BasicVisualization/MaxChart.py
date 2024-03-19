import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('dane.csv', sep=';', decimal=',', index_col=0)
kwartal_1 = dane[dane['Miesiac'].isin(['styczen', 'luty', 'marzec'])]

plt.figure(figsize=(10, 6))
plt.plot(kwartal_1.index, kwartal_1['prodB'], marker='o', color='b', label='Sprzedaż produktu B')
max_sprzedaz = kwartal_1[kwartal_1['prodB'] == kwartal_1['prodB'].max()]
plt.plot(max_sprzedaz.index, max_sprzedaz['prodB'], marker='o', linestyle='None', color='r', label='Maksymalna sprzedaż')
plt.title('Sprzedaż produktu B w kolejnych dniach kwartału 1')
plt.xlabel('Dzień')
plt.ylabel('Sprzedaż w tysiącach')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
