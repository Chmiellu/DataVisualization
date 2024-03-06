import pandas as pd
import matplotlib.pyplot as plt

# Odczyt danych z pliku CSV
dane = pd.read_csv('dane.csv', sep=';', decimal=',', index_col=0)

# Wyznaczenie ogólnej średniej sprzedaży produktu A dla wszystkich miesięcy
srednia_prodA = dane['prodA'].mean()

# Wybór dni, w których sprzedaż produktu A jest większa od ogólnej średniej
sprzedaz_wieksza_niz_srednia = dane[dane['prodA'] > srednia_prodA]

# Sortowanie wyników po miesiącu, a w obrębie miesiąca po wielkości sprzedaży produktu A
sprzedaz_wieksza_niz_srednia = sprzedaz_wieksza_niz_srednia.sort_values(by=['Miesiac', 'prodA'], ascending=[True, False])

# Wyświetlenie informacji o miesiącu i sprzedaży produktu A
print(sprzedaz_wieksza_niz_srednia[['Miesiac', 'prodA']])

# Zliczenie dni ze sprzedażą produktu A powyżej ogólnej średniej dla każdego miesiąca
dni_powyzsza_srednia = sprzedaz_wieksza_niz_srednia.groupby('Miesiac').size()

# Poprawienie kolejności danych zgodnie z kolejnością miesięcy
dni_powyzsza_srednia = dni_powyzsza_srednia.reindex(['styczen', 'luty', 'marzec'], fill_value=0)

# Wykres kolumnowy z liczbą dni ze sprzedażą powyżej ogólnej średniej dla każdego miesiąca
plt.bar(dni_powyzsza_srednia.index, dni_powyzsza_srednia.values, color='skyblue')
plt.title('Liczba dni ze sprzedażą powyżej średniej.')
plt.ylabel('Liczba dni')
plt.xlabel('Miesiące')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
