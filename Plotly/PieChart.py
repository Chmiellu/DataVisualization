import pandas as pd
import plotly.express as px

def create_pie_chart():
    # Tworzenie ramki danych z odpowiedziami quizu
    quiz = pd.DataFrame({'Odpowiedź' : ['Tak','Nie'], 'Wartość' : [4532,2497]})

    # Tworzenie wykresu kołowego
    fig = px.pie(quiz, values='Wartość', names='Odpowiedź', title='Odpowiedzi Quizu')

    # Wyświetlanie wykresu
    fig.show()

if __name__ == "__main__":
    create_pie_chart()