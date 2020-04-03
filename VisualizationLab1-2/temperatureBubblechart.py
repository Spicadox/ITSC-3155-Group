import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Creating sum of number of cases group by Country Column
new_df = df.groupby(['month']).max().reset_index()
new_df2 = df.groupby(['month']).min().reset_index()



trace1 = go.Scatter(x=new_df['month'], y=new_df2['average_min_temp'], text='Minimum Average Temperature', showlegend=False,
                    name='', mode='markers',
                    marker=dict(size=new_df['average_min_temp'], color=new_df['average_min_temp'], showscale=True))
trace2 = go.Scatter(x=new_df['month'], y=new_df['average_max_temp'], text='Maximum Average Temperature', showlegend=False,
                    name='', mode='markers',
                    marker=dict(size=new_df['average_max_temp'],color=new_df['average_max_temp'], showscale=True))
data = [trace1, trace2]


# Preparing layout
layout = go.Layout(title='Maximum and Minimum Average Temperature for Each Month ',
                   xaxis_title="Month",
                   yaxis_title="Temperature",
                   hovermode='closest')

# Plot the figure ad saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='temperatureBubblechart.html')

