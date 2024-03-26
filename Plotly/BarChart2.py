import pandas as pd
import plotly.express as px

def create_bar_chart(data):
    # Przekształcenie danych za pomocą melt, aby mieć Desktop i Laptop w jednej kolumnie
    melted_data = data.melt(id_vars=['Miasto'], var_name='Produkt', value_name='Sprzedaż')

    # Tworzenie wykresu kolumnowego
    fig = px.bar(melted_data, x='Produkt', y='Sprzedaż', color='Miasto', title='Rozkład sprzedaży produktów w miastach')

    # Wyświetlanie wykresu
    fig.show()

# Dane sprzedaży produktów w miastach
sprzedaz_data = pd.DataFrame({'Miasto': ['Katowice', 'Kraków', 'Wrocław'],
                              'Desktop': [2, 7, 3],
                              'Laptop': [12, 7, 13]})

if __name__ == "__main__":
    create_bar_chart(sprzedaz_data)
