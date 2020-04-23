import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import glob
import plotly.graph_objs as go

globalCountries = pd.read_csv('../Datasets/countries-aggregated.csv')
usConfirmed = pd.read_csv('../Datasets/us_confirmed.csv')
usDeaths = pd.read_csv('../Datasets/us_deaths.csv')

app = dash.Dash()

# GRAPH FUNCTIONS ED & SAM WORKSPACE -------------------------------------------------------------


def barchart_global():
    barchart_df = globalCountries[globalCountries['Date'] == '2020/04/21']
    barchart_df = barchart_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    data_barchart = [go.Bar(x=barchart_df['Country'], y=barchart_df['Confirmed'])]

    # Preparing layout
    layout = go.Layout(title='Total Corona Virus Confirmed Cases in The World to Date', xaxis_title="Countries",
                       yaxis_title="Number of confirmed cases")

    # Plot the figure and saving in a html file
    data_barchart_global = go.Figure(data=data_barchart, layout=layout)
    return data_barchart_global
    # TODO: Add some sort of checkbox to select global data or just include it as default on the page


def stackbarchart_global():
    pass


def multilinechart_global():
    pass


def bubblechart_global():
    pass


def barchart_US():
    pass


def stackbarchart_US():
    pass


def multilinechart_US():
    pass


def bubblechart_US():
    pass


# WEBSITE LAYOUT JINQUAN WORKSPACE ---------------------------------------------------------------
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

# UPDATE FIGURE FUNCTION ED & SAM WORKSPACE ---------------------------------------------------------


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value'),
               Input('select-figure', 'value')])
def update_figure(selected_continent, selected_figure):
    # TODO: THIS WILL NEED TO BE REWRITTEN
    mainFig = {}
    if selected_continent == 'US' and selected_figure == 'graph1':
        return barchart_global()
    # if selected_figure == 'graph1':
    #     mainFig['data'] = barchart(selected_continent)
    #     mainFig['layout'] = go.Layout(title='Corona Virus Confirmed Cases in {}'.format(selected_continent),
    #                                   xaxis={'title': 'States'}, yaxis={'title': 'Number of confirmed cases'})
    # elif selected_figure == 'graph2':
    #     mainFig['data'] = stackbarchart(selected_continent)
    #     mainFig['layout'] = go.Layout(title='Corona Virus Cases in the first 20 country except China',
    #                                   xaxis={'title': 'Country'}, yaxis={'title': 'Number of cases'},
    #                                   barmode='stack')
    # elif selected_figure == 'graph3':
    #     mainFig['data'] = linechart(selected_continent)
    #     mainFig['layout'] = go.Layout(title='Corona Virus Cases in the first 20 country expect China',
    #                                   xaxis={'title': 'Country'}, yaxis={'title': 'Number of cases'},
    #                                   barmode='stack')
    # elif selected_figure == 'graph4':
    #     mainFig['data'] = multilinechart(selected_continent)
    #     mainFig['layout'] = go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17',
    #                                   xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
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
