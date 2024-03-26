import pandas as pd
import plotly.express as px

names_col = ['Count','Percentage', 'dummy']
dat = [['Matching', 63, 0],['Mismatching', 37, 0]]
plot_df = pd.DataFrame(data=dat,columns=names_col)

# Tworzenie osobnych kolumn dla desktopów i laptopów
plot_df['Desktop'] = plot_df['Percentage'] * 0.6  # 60% dla desktopów
plot_df['Laptop'] = plot_df['Percentage'] * 0.4   # 40% dla laptopów

# Tworzenie stacked bar chart
fig = px.bar(plot_df, x='dummy', y=['Desktop', 'Laptop'], title='My plot',
             labels={'value': 'Procentowy udział miast', 'variable': ''}, barmode='stack')
fig.update_layout(showlegend=True)  # Pokazanie legendy
fig.show()
