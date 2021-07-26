# Teacher POV
import csv
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data.csv')
# Printing score average of each level

levelMean = df.groupby('level')["attempt"].mean()
print(levelMean)

figure = go.Figure(go.Bar(x=levelMean,y=['level1','level2','level3','level4'], orientation="h"))
figure.show()