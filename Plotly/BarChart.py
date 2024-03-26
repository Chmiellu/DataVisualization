import plotly.express as px
import pandas as pd
def create_grouped_bar_chart(data):
    # Tworzenie wykresu kolumnowego grupowanego
    fig = px.bar(data, x='Miasto', y=['Desktop', 'Laptop'], title='Rozkład sprzedaży produktów w miastach',
                 barmode='group')

    # Wyświetlanie wykresu
    fig.show()

# Dane sprzedaży produktów w miastach
sprzedaz_data = pd.DataFrame({'Miasto': ['Katowice', 'Kraków', 'Wrocław'],
                              'Desktop': [2, 7, 3],
                              'Laptop': [12, 7, 13]})

if __name__ == "__main__":
    create_grouped_bar_chart(sprzedaz_data)
