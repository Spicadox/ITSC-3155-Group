import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('Datasets/time_series_covid19_confirmed_global.csv')
df2 = pd.read_csv('Datasets/time_series_covid19_deaths_global.csv')
df3 = pd.read_csv('Datasets/time_series_covid19_recovered_global.csv')
df4 = pd.read_csv('Datasets/time_series_covid19_confirmed_US.csv')
df5 = pd.read_csv('Datasets/time_series_covid19_deaths_US.csv')
df7 = pd.read_csv('data/countries-aggregated.csv')

app = dash.Dash()


# Bar chart data
def barchart(selected_continent):
    barchart_df = df1[df1['Country'] == selected_continent]
    barchart_df = barchart_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    barchart_df = barchart_df.groupby(['State'])['Confirmed'].sum().reset_index()
    barchart_df = barchart_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_barchart = [go.Bar(x=barchart_df['State'], y=barchart_df['Confirmed'])]
    return data_barchart

# Bar chart data global
def barchart(selected_continent):
    barchart_df = df7[df7['Date'] == '4/21/2020']
    barchart_df = barchart_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    data_barchart = [go.Bar(x=barchart_df['Country'], y=barchart_df['Confirmed'])]
    return data_barchart

# Stack bar chart data
def stackbarchart(selected_continent):
    stackbarchart_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    stackbarchart_df['Unrecovered'] = stackbarchart_df['Confirmed'] - stackbarchart_df['Deaths'] - stackbarchart_df[
    'Recovered']
    stackbarchart_df = stackbarchart_df[(stackbarchart_df['Country'] == selected_continent)]
    stackbarchart_df = stackbarchart_df.groupby(['State']).agg(
    {'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()
    stackbarchart_df = stackbarchart_df.sort_values(by=['Confirmed'], ascending=[False]).head(20).reset_index()
    trace1_stackbarchart = go.Bar(x=stackbarchart_df['State'], y=stackbarchart_df['Unrecovered'], name='Under Treatment',
                              marker={'color': '#CD7F32'})
    trace2_stackbarchart = go.Bar(x=stackbarchart_df['State'], y=stackbarchart_df['Recovered'], name='Recovered',
                              marker={'color': '#9EA0A1'})
    trace3_stackbarchart = go.Bar(x=stackbarchart_df['State'], y=stackbarchart_df['Deaths'], name='Deaths',
                              marker={'color': '#FFD700'})
    data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]
    return data_stackbarchart


# Line Chart
def linechart(selected_continent):
    line_df = df2
    #line_df = line_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    line_df['Date'] = pd.to_datetime(line_df['Date'])
    data_linechart = [go.Scatter(x=line_df['Date'], y=line_df['Confirmed'], mode='lines', name='Death')]
    return data_linechart

# Multi Line Chart
def multilinechart(selected_continent):
    #multiline_df = df2[df2['Country']]
    multiline_df = df2
    #multiline_df = multiline_df[multiline_df['Country'] == selected_continent]
    multiline_df['Date'] = pd.to_datetime(multiline_df['Date'])
    trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Death'], mode='lines', name='Death')
    trace2_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Recovered'], mode='lines', name='Recovered')
    trace3_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Unrecovered'], mode='lines', name='Under Treatment')
    data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]
    return data_multiline


# Bubble chart
def bubblechart(selected_continent):
    #bubble_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    bubble_df = df1
    bubble_df = bubble_df[bubble_df['Country'] == selected_continent]
    bubble_df = bubble_df.groupby(['State'])
    bubble_df['Unrecovered'] = bubble_df['Confirmed'] - bubble_df['Deaths'] - bubble_df['Recovered']
    bubble_df = bubble_df.groupby(['States']).agg(
        {'Confirmed': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()
    data_bubblechart = [
        go.Scatter(x=bubble_df['Recovered'],
                   y=bubble_df['Unrecovered'],
                   text=bubble_df['States'],
                   mode='markers',
                   marker=dict(size=bubble_df['Confirmed'] / 200, color=bubble_df['Confirmed'] / 200, showscale=True))
    ]
    return data_bubblechart


# Heatmap
def heatmap(selected_continent):
    new_df = df1[df1['Country'] == selected_continent]
    new_df = df1.groupby(['state'])
    data_heatmap = [go.Heatmap(x=new_df['Day'],
                               y=new_df['WeekofMonth'],
                               z=new_df['Recovered'].values.tolist(),
                               colorscale='Jet')]
    return data_heatmap


# Layout
app.layout = html.Div(children=[
    html.H1(children='TEAM J.E.T.S Draft',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Coronavirus COVID-19 Global Cases -  1/22/2020 to 3/17/2020', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Bar chart', style={'color': '#df1e56'}),
    html.Div('TODO: Put Information about Bar chart here'),
    dcc.Graph(id='graph1'),
    html.Div('Please select a country', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-continent',
        options=[
            {'label': 'China', 'value': 'China'},
            {'label': 'Italy', 'value': 'Italy'},
            {'label': 'Japan', 'value': 'Japan'},
            {'label': 'US', 'value': 'US'},
            {'label': 'Canada', 'value': 'Canada'},
            {'label': 'South Korea', 'value': 'South Korea'}
        ],
        value='Europe'
    ),
    html.Div('Please select a figure', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-figure',
        options=[
            {'label': 'Bar chart', 'value': 'graph1'},
            {'label': 'Stack bar chart', 'value': 'graph2'},
            {'label': 'Line chart', 'value': 'graph3'},
            {'label': 'Multi line chart', 'value': 'graph4'},
            # {'label': 'Bubble chart', 'value': 'graph5'},
            # {'label': 'Heat map', 'value': 'graph6'}
        ],
        value='graph6'
    ),

    # html.Br(),
    # html.Hr(style={'color': '#7FDBFF'}),
    # html.H3('Bar chart', style={'color': '#df1e56'}),
    # html.Div('This bar chart represent the number of confirmed cases in the first 20 states of the US.'),
    # dcc.Graph(id='graph2',
    #           figure={
    #               'data': data_barchart,
    #               'layout': go.Layout(title='Corona Virus Confirmed Cases in The US',
    #                                   xaxis={'title': 'States'}, yaxis={'title': 'Number of confirmed cases'})
    #           }
    #           ),
    # html.Hr(style={'color': '#7FDBFF'}),
    # html.H3('Stack bar chart', style={'color': '#df1e56'}),
    # html.Div(
    #     'This stack bar chart represent the CoronaVirus deaths,
    #     recovered and under treatment of all reported first 20 countries except China.'),
    # dcc.Graph(id='graph3',
    #           figure={
    #               'data': data_stackbarchart,
    #               'layout': go.Layout(title='Corona Virus Cases in the first 20 country expect China',
    #                                   xaxis={'title': 'Country'}, yaxis={'title': 'Number of cases'},
    #                                   barmode='stack')
    #           }
    #           ),
    # html.Hr(style={'color': '#7FDBFF'}),
    # html.H3('Line chart', style={'color': '#df1e56'}),
    # html.Div('This line chart represent the Corona Virus confirmed cases of all reported cases in the given period.'),
    # dcc.Graph(id='graph4',
    #           figure={
    #               'data': data_linechart,
    #               'layout': go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17',
    #                                   xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
    #           }
    #           ),
    # html.Hr(style={'color': '#7FDBFF'}),
    # html.H3('Multi Line chart', style={'color': '#df1e56'}),
    # html.Div(
    #     'This line chart represent the CoronaVirus death,
    #     recovered and under treatment cases of all reported cases in the given period.'),
    # dcc.Graph(id='graph5',
    #           figure={
    #               'data': data_multiline,
    #               'layout': go.Layout(
    #                   title='Corona Virus Death, Recovered and under treatment Cases From 2020-01-22 to 2020-03-17',
    #                   xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
    #           }
    #           ),
    # html.Hr(style={'color': '#7FDBFF'}),
    # html.H3('Bubble chart', style={'color': '#df1e56'}),
    # html.Div(
    #     'This bubble chart represent the Corona Virus recovered and under treatment
    #     of all reported countries except China.'),
    # dcc.Graph(id='graph6',
    #           figure={
    #               'data': data_bubblechart,
    #               'layout': go.Layout(title='Corona Virus Confirmed Cases',
    #                                   xaxis={'title': 'Recovered Cases'}, yaxis={'title': 'under Treatment Cases'},
    #                                   hovermode='closest')
    #           }
    #           ),
    # html.Hr(style={'color': '#7FDBFF'}),
    # html.H3('Heat map', style={'color': '#df1e56'}),
    # html.Div(
    #     'This heat map represent the Corona Virus recovered cases of all reported cases
    #     per day of week and week of month.'),
    # dcc.Graph(id='graph7',
    #           figure={
    #               'data': data_heatmap,
    #               'layout': go.Layout(title='Corona Virus Recovered Cases',
    #                                   xaxis={'title': 'Day of Week'}, yaxis={'title': 'Week of Month'})
    #           }
    #           )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value'),
               Input('select-figure', 'value')])
def update_figure(selected_continent, selected_figure):
    mainFig = {}
    if selected_figure == 'graph1':
        mainFig['data'] = barchart(selected_continent)
        mainFig['layout'] = go.Layout(title='Corona Virus Confirmed Cases in {}'.format(selected_continent),
                                      xaxis={'title': 'States'}, yaxis={'title': 'Number of confirmed cases'})
    elif selected_figure == 'graph2':
        mainFig['data'] = stackbarchart(selected_continent)
        mainFig['layout'] = go.Layout(title='Corona Virus Cases in the first 20 country except China',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Number of cases'},
                                      barmode='stack')
    elif selected_figure == 'graph3':
        mainFig['data'] = linechart(selected_continent)
        mainFig['layout'] = go.Layout(title='Corona Virus Cases in the first 20 country expect China',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Number of cases'},
                                      barmode='stack')
    elif selected_figure == 'graph4':
        mainFig['data'] = multilinechart(selected_continent)
        mainFig['layout'] = go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
    # elif selected_figure == 'graph5':
    #     mainFig['data'] = bubblechart(selected_continent)
    #     mainFig['layout'] = go.Layout(title='Corona Virus Confirmed Cases',
    #                                   xaxis={'title': 'Recovered Cases'}, yaxis={'title': 'under Treatment Cases'},
    #                                   hovermode='closest')
    # elif selected_figure == 'graph6':
    #     mainFig['data'] = heatmap(selected_continent)
    #     mainFig['layout'] = go.Layout(title='Corona Virus Recovered Cases',
    #                                   xaxis={'title': 'Day of Week'}, yaxis={'title': 'Week of Month'})
    return mainFig


if __name__ == '__main__':
    app.run_server()
