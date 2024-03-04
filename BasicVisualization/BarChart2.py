import pandas as pd
import matplotlib.pyplot as plt

# Read the data from CSV
dane = pd.read_csv('dane.csv', sep=';', decimal=',', index_col=0)
dane['Sprzedaz całkowita'] = dane['prodA'] + dane['prodB']
dane_styczen = dane[dane['Miesiac'] == 'styczen']
dane_marzec = dane[dane['Miesiac'] == 'marzec']

plt.figure(figsize=(6, 2))  # Adjust figure size as needed

# Plot the first part (Marzec) in green
plt.barh(y=0, width=dane_marzec['Sprzedaz całkowita'].sum(), color='green', height=0.1, label='Marzec')

# Plot the second part (Styczeń) in blue
plt.barh(y=0, width=dane_styczen['Sprzedaz całkowita'].sum(), left=dane_marzec['Sprzedaz całkowita'].sum(), color='blue', height=0.1, label='Styczeń')
plt.yticks([0], ['MarzecStyczeń'])
plt.title('Porównanie sprzedaży za styczeń i marzec')
plt.xlabel('Sprzedaż całkowita w tysiącach')
plt.legend()
plt.tight_layout()  # Adjust layout to fit bars properly
plt.show()
