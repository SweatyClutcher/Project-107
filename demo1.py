import pandas as pd
import csv 
import plotly.graph_objects as go

df = pd.read_csv("C-107/data.csv")
# print(df.groupby("level")["attempt"].mean())
figure = go.Figure(go.Scatter(x = df.groupby("level")["attempt"].mean(), y = ['level1', 'level2', 'level3', 'level4'], orientation = 'h'))
figure.show()