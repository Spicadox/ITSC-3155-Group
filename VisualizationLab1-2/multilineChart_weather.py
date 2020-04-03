import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("../Datasets/Weather2014-15.csv")
df_max = df.groupby(["month"]).max()
df_max = df_max.reindex(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])
df_min = df.groupby(["month"]).min()
df_min = df_min.reindex(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])
df_mean = df.groupby(["month"]).mean()
df_mean = df_mean.reindex(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])
trace1 = go.Scatter(x=df_max.index, y=df_max["actual_max_temp"], mode="lines+markers", name="Max Temperature")
trace2 = go.Scatter(x=df_min.index, y=df_min["actual_min_temp"], mode="lines+markers", name="Min Temperature")
trace3 = go.Scatter(x=df_mean.index, y=df_mean["actual_mean_temp"], mode="lines+markers", name="Mean Temperature")
data = [trace1, trace2, trace3]

layout = go.Layout(title="Actual max, min, and mean temperature of each month 2014-2015", xaxis_title="Month",
                   yaxis_title="Temperature (F)")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="multilinechart_weather.html")
