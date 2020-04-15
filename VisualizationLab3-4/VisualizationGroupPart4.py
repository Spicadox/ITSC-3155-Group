import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Weather2014-15.csv')
df2 = pd.read_csv('../Datasets/Olympic2016Rio.csv')

app = dash.Dash()

# Bar chart data
new_df = df2.groupby(['NOC'])['Total'].sum().reset_index()

new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)


data_barchart = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]


# Stack bar chart data
new_df = df2.groupby(['NOC']).agg(
    {'Total': 'sum', 'Gold': 'sum', 'Silver': 'sum', 'Bronze': 'sum'}).reset_index()

new_df = new_df.sort_values(by=['Total'],
                            ascending=[False]).head(20).reset_index()

trace1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze',
                marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver',
                marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold',
                marker={'color': '#FFD700'})
data_stackbarchart = [trace1, trace2, trace3]

# Line Chart
df = df1.groupby(["month"]).max()
df = df.reindex(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])
data_linechart = [go.Scatter(x=df.index, y=df["actual_max_temp"], mode="lines+markers", name="Max Temperature")]


# Multi Line Chart
df_max = df1.groupby(["month"]).max()
df_max = df_max.reindex(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])
df_min = df1.groupby(["month"]).min()
df_min = df_min.reindex(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])
df_mean = df1.groupby(["month"]).mean()
df_mean = df_mean.reindex(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])
trace1 = go.Scatter(x=df_max.index, y=df_max["actual_max_temp"], mode="lines+markers", name="Max Temperature")
trace2 = go.Scatter(x=df_min.index, y=df_min["actual_min_temp"], mode="lines+markers", name="Min Temperature")
trace3 = go.Scatter(x=df_mean.index, y=df_mean["actual_mean_temp"], mode="lines+markers", name="Mean Temperature")
data_multiline = [trace1, trace2, trace3]

# Bubble chart
new_df = df1.groupby(['month']).max().reset_index()
new_df2 = df1.groupby(['month']).min().reset_index()

trace1 = go.Scatter(x=new_df['month'], y=new_df2['average_min_temp'], text='Minimum Average Temperature', showlegend=False,
                    name='', mode='markers',
                    marker=dict(size=new_df['average_min_temp'], color=new_df['average_min_temp'], showscale=True))
trace2 = go.Scatter(x=new_df['month'], y=new_df['average_max_temp'], text='Maximum Average Temperature', showlegend=False,
                    name='', mode='markers',
                    marker=dict(size=new_df['average_max_temp'],color=new_df['average_max_temp'], showscale=True))
data_bubblechart = [trace1, trace2]

# Heatmap
new_df = df1.groupby(['day', 'month']).max().reset_index()

data_heatmap = [go.Heatmap(x=new_df['day'],
                  y=new_df['month'],
                  z=new_df['record_max_temp'],
                  colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('2016 Olympic RIO & Weather Statistics  -  2014 to 2015', style={'textAlign': 'center'}),
    html.Br(),

    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the total medals of Olympic 2016 of 20 first top countries'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title=' Total Medals of Olympic 2016 ',
                                      xaxis={'title': 'Countries'}, yaxis={'title': 'Number of medals'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent the Gold, Silver, Bronze medals of Olympic 2016 of 20 first top countries.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Total Number of Bronze, Silver, and Gold Medals of 20 first top countries.',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Number of medals'},
                                      barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the actual max temperature of each month in weather statistics.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Max Temperature of Each Month From 2014 to 2015',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature (F)'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This multi-line chart represent the actual max, min and mean temperature of each month in weather statistics'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='The Max, Min & Mean Temperature of Each Month From 2014 to 2015',
                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature (F)'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart represent the average min and max temperature of each month in weather statistics.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='Maximum and Minimum Average Temperature for Each Month',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature (F)'},
                                      hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the recorded max temperature on day of week and month of year.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='The Maximum Record Temperature',
                                      xaxis={'title': 'Day of Week'}, yaxis={'title': 'Month of the Year'})
              }
              )
])


if __name__ == '__main__':
    app.run_server()