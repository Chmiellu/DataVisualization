import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('dane.csv', sep=';', decimal=',', index_col=0)
dane['Sprzedaz całkowita'] = dane['prodA'] + dane['prodB']
dane_luty = dane[dane['Miesiac'] == 'luty']
sprzedaz = dane_luty

plt.figure(figsize=(10, 6))
plt.plot(sprzedaz.index, sprzedaz['Sprzedaz całkowita'], marker='o', linestyle='-')
plt.title('Sprzedaż całkowita w kolejnych dniach miesiąca lutego')
plt.xlabel('Dzień')
plt.ylabel('Sprzedaż w tysiącach')
plt.grid(True)
plt.xticks(rotation=45)
plt.yticks(plt.yticks()[0], labels=[f"{int(i)} tyś." for i in plt.yticks()[0]])  
plt.tight_layout()
plt.show()
