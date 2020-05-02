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
    recentdate = pd.to_datetime(globalCountries['Date'], format='%Y-%m-%d').max()
    recentdate = str(recentdate).rstrip(' 00:00:00')
    barchart_df = globalCountries[globalCountries['Date'] == recentdate]
    barchart_df = barchart_df.sort_values(by=['Confirmed'], ascending=[False]).head(50)
    data_barchart = [go.Bar(x=barchart_df['Country'], y=barchart_df['Confirmed'])]

    # Preparing layout
    layout = go.Layout(title='Total Corona Virus Confirmed Cases in The World to Date', xaxis_title="Countries",
                       yaxis_title="Number of confirmed cases")

    # Plot the figure and saving in a html file
    data_barchart_global = go.Figure(data=data_barchart, layout=layout)
    return data_barchart_global
    # TODO: Add some sort of checkbox to select global data or just include it as default on the page



def multibarchart_global():
    recentdate = pd.to_datetime(globalCountries['Date'], format='%Y-%m-%d').max()
    recentdate = str(recentdate).rstrip(' 00:00:00')
    multibarchart_df = globalCountries
    multibarchart_df = multibarchart_df[multibarchart_df["Date"] == recentdate]
    multibarchart_df = multibarchart_df.groupby(['Country']).agg(
        {'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum'}).reset_index()
    multibarchart_df = multibarchart_df.sort_values(by=['Confirmed'], ascending=[False]).head(20).reset_index()
    trace1_multibarchart = go.Bar(x=multibarchart_df['Country'], y=multibarchart_df['Confirmed'], name='Confirmed',
                                  marker={'color': '#FFA500'})
    trace2_multibarchart = go.Bar(x=multibarchart_df['Country'], y=multibarchart_df['Recovered'], name='Recovered',
                                  marker={'color': '#008000'})
    trace3_multibarchart = go.Bar(x=multibarchart_df['Country'], y=multibarchart_df['Deaths'], name='Deaths',
                                  marker={'color': '#696969'})
    data_multibarchart = [trace1_multibarchart, trace2_multibarchart, trace3_multibarchart]

    # Preparing layout
    layout = go.Layout(title='Total Corona Virus Confirmed Cases, Recovered, and Deaths in The World to Date', xaxis_title="Countries",
                       yaxis_title="Number of confirmed cases")

    # Plot the figure and saving in a html file
    data_multibarchart_global = go.Figure(data=data_multibarchart, layout=layout)
    return data_multibarchart_global



def multilinechart_global():
    pass


def bubblechart_global():
    pass


def barchart_US():
    recentdate = pd.to_datetime(usConfirmed['Date'], format='%Y-%m-%d').max()
    recentdate = str(recentdate).rstrip(' 00:00:00')
    barchart_df = usConfirmed
    barchart_df = barchart_df[barchart_df["Date"] == recentdate]
    barchart_df = barchart_df.groupby(['Province/State'])['Case'].sum().reset_index()
    barchart_df = barchart_df.sort_values(by=['Case'], ascending=[False]).head(50)
    data_barchart = [go.Bar(x=barchart_df['Province/State'], y=barchart_df['Case'])]

    # Preparing layout
    layout = go.Layout(title='Total Corona Virus Confirmed Cases in The United States to Date', xaxis_title="States",
                       yaxis_title="Number of confirmed cases")

    # Plot the figure and saving in a html file
    data_barchart_US = go.Figure(data=data_barchart, layout=layout)
    return data_barchart_US


def multibarchart_US():
    recentdate = pd.to_datetime(usConfirmed['Date'], format='%Y-%m-%d').max()
    recentdate = str(recentdate).rstrip(' 00:00:00')
    print(recentdate)
    multibarchartconfirmed_df = usConfirmed
    multibarchartdeath_df = usDeaths
    multibarchartconfirmed_df = multibarchartconfirmed_df[multibarchartconfirmed_df["Date"] == recentdate]
    multibarchartdeath_df = multibarchartdeath_df[multibarchartdeath_df["Date"] == recentdate]

    multibarchartconfirmed_df = multibarchartconfirmed_df.groupby(['Province/State']).agg(
        {'Case': 'sum'}).reset_index()
    multibarchartdeath_df = multibarchartdeath_df.groupby(['Province/State']).agg(
        {'Case': 'sum'}).reset_index()
    trace1_multibarchart = go.Bar(x=multibarchartconfirmed_df['Province/State'], y=multibarchartconfirmed_df['Case'],
                                  name='Confirmed Cases',
                                  marker={'color': '#CD7F32'})
    trace2_multibarchart = go.Bar(x=multibarchartdeath_df['Province/State'], y=multibarchartdeath_df['Case'],
                                  name='Deaths',
                                  marker={'color': '#9EA0A1'})
    data_multibarchart = [trace1_multibarchart, trace2_multibarchart]

    # Preparing layout
    layout = go.Layout(title='Total Corona Virus Confirmed Cases and Deaths in The United States to Date', xaxis_title="States",
                       yaxis_title="Number of confirmed cases")

    # Plot the figure and saving in a html file
    data_multibarchart_US = go.Figure(data=data_multibarchart, layout=layout)
    return data_multibarchart_US


def multilinechart_US():
    pass


def bubblechart_US():
    pass


# WEBSITE LAYOUT JINQUAN WORKSPACE ---------------------------------------------------------------
figures = {'global_figures': ['Global bar chart', 'Global multi bar chart', 'Global multi line chart', 'Global bubble chart'],
           'local_figures': ['Local bar chart', 'Local multi bar chart', 'Local multi line chart', 'Local bubble chart']
}
global_or_local = 'global_figures'
disable_or_not = True


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
    html.Div('Would you like a global chart or US chart?', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-scope',
        options=[
            {'label': 'Global chart', 'value': 'global_chart'},
            {'label': 'A specific country chart', 'value': 'country_chart'},
            {'label': 'US chart', 'value': 'us_chart'}
        ],
        placeholder='Select a scope'
    ),

    html.Div('Please select a country', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-continent',
        options=[
            {'label': 'US', 'value': 'US'},
            {'label': 'China', 'value': 'China'},
            {'label': 'Italy', 'value': 'Italy'},
            {'label': 'Japan', 'value': 'Japan'},
            {'label': 'Canada', 'value': 'Canada'},
            {'label': 'South Korea', 'value': 'South Korea'}
        ],
        placeholder='Select a country',
        disabled=True
    ),
    html.Div('Please select a figure', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-figure',
        options=[
            # {'label': 'Global Bar chart', 'value': 'graph1'},
            # {'label': 'Local Bar chart', 'value': 'graph2'},
            # {'label': 'Global Multi bar chart', 'value': 'graph3'},
            # {'label': 'Local Multi bar chart', 'value': 'graph4'},
            # {'label': 'Global Multi line chart', 'value': 'graph5'},
            # {'label': 'Local Multi line chart', 'value': 'graph6'},
            # {'label': 'Global Bubble chart', 'value': 'graph7'},
            # {'label': 'Local Bubble chart', 'value': 'graph8'}
            {'label': k, 'value': k} for k in figures.get('global_figures', '')
        ],
        placeholder='Select a figure'
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
# Enable or disable 1st dropdown box(i.e.Selecting country)
@app.callback(Output('select-continent', 'disabled'),
              [Input('select-scope', 'value')])
def disable_local_figures(select_scope):
    if select_scope == 'global_chart':
        return True
    elif select_scope == 'country_chart':
        return False
    elif select_scope == 'us_chart':
        return True

# Placeholder set to US if the scope is selected as us chart
@app.callback(Output('select-continent', 'placeholder'),
              [Input('select-scope', 'value')])
def disable_local_figures(select_scope):
    if select_scope == 'us_chart':
        return 'US'

# Output a list of either global or local figures in last dropdown box
@app.callback(Output('select-figure', 'options'),
              [Input('select-scope', 'value')])
def disable_local_figures(select_scope):
    if select_scope == 'global_chart':
        return [{'label': k, 'value': k} for k in figures['global_figures']]
    if select_scope == 'us_chart':
        return [{'label': k, 'value': k} for k in figures['local_figures']]


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value'),
               Input('select-figure', 'value')])
def update_figure(selected_continent, selected_figure):
    # TODO: THIS WILL NEED TO BE REWRITTEN
    mainFig = {}
    if selected_continent == 'US' and selected_figure == 'graph1':
        return barchart_global()

    # DEMO
    elif selected_figure == 'graph1':
        return barchart_global()
    elif selected_figure == 'graph2':
        return barchart_US()
    elif selected_figure == 'graph3':
        return multibarchart_global()
    elif selected_figure == 'graph4':
        return multibarchart_US()

    # END OF DEMO
    if selected_figure == 'graph1':
        mainFig['data'] = barchart(selected_continent)
        mainFig['layout'] = go.Layout(title='Corona Virus Confirmed Cases in {}'.format(selected_continent),
                                      xaxis={'title': 'States'}, yaxis={'title': 'Number of confirmed cases'})
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
