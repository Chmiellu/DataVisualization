import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = pd.read_csv('dane.csv', sep=';', decimal=',', index_col=0)
suma_sprzedazy = dane.groupby('Miesiac')[['prodA', 'prodB']].sum()
suma_sprzedazy = suma_sprzedazy.reindex(['styczen', 'luty', 'marzec'])

plt.figure(figsize=(10, 6))
bar_width = 0.35
x = np.arange(len(suma_sprzedazy.index))
plt.bar(x - bar_width/2, suma_sprzedazy['prodA'], color='blue', width=bar_width, label='prodA')
plt.bar(x + bar_width/2, suma_sprzedazy['prodB'], color='orange', width=bar_width, label='prodB')
plt.xlabel('Miesiąc')
plt.ylabel('Sumaryczna sprzedaż')
plt.title('Sumaryczna sprzedaż produktów A i B w każdym miesiącu')
plt.legend()
plt.xticks(ticks=x, labels=suma_sprzedazy.index, rotation=45)  
plt.tight_layout()
plt.show()
