import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("../Datasets/Weather2014-15.csv")
df = df.groupby(["month"]).max()
df = df.reindex(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])
data = [go.Scatter(x=df.index, y=df["actual_max_temp"], mode="lines+markers", name="Max Temperature")]
layout = go.Layout(title="Actual max temperature of each month 2014-2015", xaxis_title="Month",
                   yaxis_title="Temperature (F)")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="linechart_weather.html")
