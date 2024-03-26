import numpy as np
import pandas as pd
import plotly.express as px

x = list(range(1,101))
y2 = np.log2(x)
y10 = np.log10(x)
quiz = pd.DataFrame({'Odpowiedź' : ['Tak','Nie'],
'Wartość' : [4532,2497]})
sprzedaz = pd.DataFrame({'Miasto': ['Katowice', 'Kraków', 'Wrocław'],
'Desktop': [2, 7, 3],
'Laptop': [12, 7, 13]})
gap = px.data.gapminder()
gap = px.data.gapminder()

schematy = ['ggplot2', 'seaborn', 'simple_white', 'plotly',
'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
'ygridoff', 'gridon', 'none']