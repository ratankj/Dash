from dash import Dash, html, dcc, callback, Output, Input,dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Dash', style={'textAlign':'center', 'color': 'Red', 'fontSize': 50} ),

    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),

    dash_table.DataTable(data=df.to_dict('records'), page_size=10),

    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='pop', id='controls-and-radio-item'), 
    dcc.Graph(figure={}, id='controls-and-graph'),


    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)


def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

if __name__ == '__main__':
    app.run(debug=True)


