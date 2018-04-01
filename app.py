import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import coin_flip_main

app = dash.Dash()
# Stops error from using components spawned by other callbacks
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    html.Div([
        html.H1('Probability of coin toss', style={'text-align': 'center', 'margin-bottom': '-20'}),
        html.Div([
            html.P('Total flips: ', style={'margin-bottom': "-3", 'text-align': 'center', 'font-size': 20}),
            dcc.Slider(
                min=1,
                max=100,
                value=10,
                id='total_slider'
            ),
        ], style={'margin-bottom': -15}),
        html.Div([
            html.P('Number of Heads: ', style={'margin-bottom': "-8", 'text-align': 'center', 'font-size': 20}),
            dcc.Slider(
                min=1,
                max=100,
                value=10,
                id='success_slider'
            ),
        ]),

    ], id='header_div', style={'margin-top': '-13'}),
    html.Div(dcc.Graph(id='graph')),

    #Timer to update the ui
    dcc.Interval(
        id='interval',
        interval=10 * 1000,  # in milliseconds
        n_intervals=0
    )
])


# Callbacks
@app.callback(Output('graph', 'figure'),
              [
                  Input('interval', 'n_intervals'),
                  Input('success_slider', 'value'),
                  Input('total_slider', 'value')
              ])
def spawn_graph(n, successes, total):
    return {
        'data': [
            go.Scatter(
                x=list(range(1, total + 1)),
                y=coin_flip_main.get_probabilities_in_range(successes, total),
                name='Probability'
            )
        ],
        'layout': {
            'title': 'Probability',
            'xaxis': dict(title='Flips'),
            'yaxis': dict(title='Probability')
        }
    }


if __name__ == "__main__":
    print("Starting app!")
    app.run_server(debug=False)
