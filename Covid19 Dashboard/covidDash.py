import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

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

    # Return the figure
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

    # Return the figure
    data_multibarchart_global = go.Figure(data=data_multibarchart, layout=layout)
    return data_multibarchart_global


def multilinechart_global():
    recentdate = pd.to_datetime(usConfirmed['Date'], format='%Y-%m-%d').max()
    recentdate = str(recentdate).rstrip(' 00:00:00')
    multilinechart_df = globalCountries
    multilinechart_df = multilinechart_df.groupby(['Country', 'Date']).agg(
        {'Confirmed': 'sum'}).reset_index()

    data_multilinechart_global = px.line(multilinechart_df, x='Date', y='Confirmed', color='Country',
                                     line_group="Country", hover_name="Country",
                                     line_shape="spline", render_mode="svg",
                                     title='Corona Virus Confirmed Cases Over Time')
    data_multilinechart_global.update_xaxes(title="Date")
    data_multilinechart_global.update_yaxes(title="Number of confirmed cases")

    return data_multilinechart_global


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

    # Return the figure
    data_barchart_US = go.Figure(data=data_barchart, layout=layout)
    return data_barchart_US


def multibarchart_US():
    recentdate = pd.to_datetime(usConfirmed['Date'], format='%Y-%m-%d').max()
    recentdate = str(recentdate).rstrip(' 00:00:00')
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

    # Return the figure
    data_multibarchart_US = go.Figure(data=data_multibarchart, layout=layout)
    return data_multibarchart_US


def multilinechart_US():
    recentdate = pd.to_datetime(usConfirmed['Date'], format='%Y-%m-%d').max()
    recentdate = str(recentdate).rstrip(' 00:00:00')
    multilinechartconfirmed_df = usConfirmed
    multilinechartdeaths_df = usDeaths
    multilinechartconfirmed_df = multilinechartconfirmed_df.groupby(['Province/State', 'Date']).agg(
        {'Case': 'sum'}).reset_index()

    data_multilinechart_US = px.line(multilinechartconfirmed_df, x='Date', y='Case', color='Province/State', line_group="Province/State",
                                  hover_name="Province/State", line_shape="spline", render_mode="svg",
                                  title='Corona Virus Confirmed Cases Over Time')
    data_multilinechart_US.update_xaxes(title="Date")
    data_multilinechart_US.update_yaxes(title="Number of confirmed cases")

    return data_multilinechart_US


# WEBSITE LAYOUT JINQUAN WORKSPACE ---------------------------------------------------------------
figures = {'global_figures': ['Global bar chart', 'Global multi bar chart', 'Global multi line chart'],
           'local_figures': ['Local bar chart', 'Local multi bar chart', 'Local multi line chart']
}
all_figures = {'Global bar chart', 'Global multi bar chart', 'Global multi line chart',
               'Local bar chart', 'Local multi bar chart', 'Local multi line chart'}


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
    html.H3('Interactive COVID-19 Chart', style={'color': '#df1e56'}),
    dcc.Graph(id='graph1'),
    html.Div('Would you like a global chart or US chart?', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-scope',
        options=[
            {'label': 'Global chart', 'value': 'global_chart'},
            {'label': 'US chart', 'value': 'us_chart'}
        ],
        placeholder='Select a scope'
    ),


    html.Div('Please select a figure', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-figure',
        options=[
            {'label': k, 'value': k} for k in all_figures
        ],
        placeholder='Select a figure',
        disabled=True
    ),
])

# UPDATE FIGURE FUNCTION ED & SAM WORKSPACE ---------------------------------------------------------


# Enable or disable dropdown boxes
# Placeholder set to US if the scope is selected as us chart
# Return a list of figure options based on scope
@app.callback([Output('select-figure', 'options'),
               Output('select-figure','disabled')],
              [Input('select-scope', 'value')])
def placeholder_set_us(select_scope):
    if select_scope == 'us_chart':
        return [{'label': i, 'value': i} for i in figures['local_figures']], False
    elif select_scope == 'global_chart':
        return [{'label': i, 'value': i} for i in figures['global_figures']], False


@app.callback(Output('graph1', 'figure'),
              [Input('select-figure', 'value')])
def update_figure(selected_figure):
    # TODO: THIS WILL NEED TO BE REWRITTEN
    mainFig = {}


    if selected_figure == 'Global bar chart':
        return barchart_global()
    elif selected_figure == 'Local bar chart':
        return barchart_US()
    elif selected_figure == 'Global multi bar chart':
        return multibarchart_global()
    elif selected_figure == 'Local multi bar chart':
        return multibarchart_US()
    elif selected_figure == 'Global multi line chart':
        return multilinechart_global()
    elif selected_figure == 'Local multi line chart':
        return multilinechart_US()
    elif selected_figure == 'Global bubble chart':
        return bubblechart_global()

    return mainFig


if __name__ == '__main__':
    app.run_server()
