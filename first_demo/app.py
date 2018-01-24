# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
    'background': '#ffc0cb',
    'text': '#ffffff'
}

app.layout = html.Div(children=[
    html.H1(children='你好，Dash！'),

    html.H3('''
        汝等乃地中之盐，汝若非盐，当以何物盐之。
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': '沃特而我'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'title': '非一般'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)