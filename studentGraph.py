# Student POV
import csv
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")

student_id = input("Enter Student ID")
studentDF = df.loc[df['student_id']==student_id]
studentMean = studentDF.groupby('level')['attempt'].mean()
figure = go.Figure(go.Bar(x=studentMean, y=['level1','level2','level3','level4'], orientation='h'))
print(studentMean)
figure.show()
