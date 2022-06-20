import dash
import dash_cytoscape as cyto
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from sys import argv
from help_functions import get_colorscale
import read_data


cyto.load_extra_layouts()

app = dash.Dash(__name__)


colors = get_colorscale('green', 'yellow', 'red')
nodes, edges = read_data.main(argv[1], argv[2], argv[3], argv[4]) # expression_path, fas_path, sample_path, gene_id


#nodes = {'Big1': {
#         'A': [
#               {
#                   'data': {'id': '1', 'label': '1', 'size': 10, 'color': str(colors[int(round(0.0, 2)*50)]), 'blacken': 0},
#                   'position': {'x': 0, 'y': 0},
#               },
#               {
#                   'data': {'id': '2', 'label': '2', 'size': 20, 'color': str(colors[int(round(0.1, 2)*50)]), 'blacken': 0.5},
#                   'position': {'x': 10, 'y': 10},
#               },
#               {
#                   'data': {'id': '3', 'label': '3', 'size': 40, 'color': str(colors[int(round(0.5, 2)*50)]), 'blacken': 1},
#                   'position': {'x': 20, 'y': 20},
#               },
#               {
#                   'data': {'id': '4', 'label': '4', 'size': 50, 'color': str(colors[int(round(0.7, 2)*50)])},
#                   'position': {'x': 40, 'y': 40},
#               },
#               {
#                   'data': {'id': '5', 'label': '5', 'size': 60, 'color': str(colors[int(round(1.0, 2)*50)])},
#                   'position': {'x': 70, 'y': 70},
#               }
#              ],
#         'B': [
#               {
#                   'data': {'id': '1', 'label': '1', 'size': 10, 'color': 'green'},
#                   'position': {'x': 0, 'y': 0},
#               },
#               {
#                   'data': {'id': '2', 'label': '2', 'size': 10, 'color': 'green'},
#                   'position': {'x': 10, 'y': 10},
#               },
#               {
#                   'data': {'id': '3', 'label': '3', 'size': 10, 'color': 'green'},
#                   'position': {'x': 20, 'y': 20},
#               },
#               {
#                   'data': {'id': '4', 'label': '4', 'size': 10, 'color': 'green'},
#                   'position': {'x': 40, 'y': 40},
#               },
#               {
#                   'data': {'id': '5', 'label': '5', 'size': 10, 'color': 'green'},
#                   'position': {'x': 70, 'y': 70},
#               }
#              ]
#        },
#        'Big2': {
#         'c': [
#               {
#                   'data': {'id': '1', 'label': '1', 'size': 10, 'color': str(colors[int(round(0.0, 2)*50)]), 'blacken': 0},
#                   'position': {'x': 0, 'y': 0},
#               },
#               {
#                   'data': {'id': '2', 'label': '2', 'size': 20, 'color': str(colors[int(round(0.1, 2)*50)]), 'blacken': 0.5},
#                   'position': {'x': 10, 'y': 10},
#               },
#               {
#                   'data': {'id': '3', 'label': '3', 'size': 40, 'color': str(colors[int(round(0.5, 2)*50)]), 'blacken': 1},
#                   'position': {'x': 20, 'y': 20},
#               },
#               {
#                   'data': {'id': '4', 'label': '4', 'size': 50, 'color': str(colors[int(round(0.7, 2)*50)])},
#                   'position': {'x': 40, 'y': 40},
#               },
#               {
#                   'data': {'id': '5', 'label': '5', 'size': 60, 'color': str(colors[int(round(1.0, 2)*50)])},
#                   'position': {'x': 70, 'y': 70},
#               }
#              ],
#         'D': [
#               {
#                   'data': {'id': '1', 'label': '1', 'size': 10, 'color': 'green'},
#                   'position': {'x': 0, 'y': 0},
#               },
#               {
#                   'data': {'id': '2', 'label': '2', 'size': 10, 'color': 'green'},
#                   'position': {'x': 10, 'y': 10},
#               },
#               {
#                   'data': {'id': '3', 'label': '3', 'size': 10, 'color': 'green'},
#                   'position': {'x': 20, 'y': 20},
#               },
#               {
#                   'data': {'id': '4', 'label': '4', 'size': 10, 'color': 'green'},
#                   'position': {'x': 40, 'y': 40},
#               },
#               {
#                   'data': {'id': '5', 'label': '5', 'size': 10, 'color': 'green'},
#                   'position': {'x': 70, 'y': 70},
#               }
#              ]
#        }
#        }
         



#edges = {'1': [
#               {
#                   'data': {'source': '1', 'target': '2', 'weight': 1}
#               },
#               {
#                   'data': {'source': '1', 'target': '5', 'weight': 10.0}
#               },
#               {
#                   'data': {'source': '1', 'target': '3', 'weight': 3}
#               },
#               {
#                   'data': {'source': '2', 'target': '5', 'weight': 4}
#               },
#               {
#                   'data': {'source': '3', 'target': '4', 'weight': 20}
#               }
#              ],
#         '2': [
#               {
#                   'data': {'source': '1', 'target': '4', 'weight': 1}
#               },
#               {
#                   'data': {'source': '3', 'target': '5', 'weight': 1}
#               },
#               {
#                   'data': {'source': '2', 'target': '3', 'weight': 1}
#               },
#               {
#                   'data': {'source': '4', 'target': '5', 'weight': 1}
#               },
#               {
#                   'data': {'source': '2', 'target': '4', 'weight': 1}
#               }
#             ]
#        }

l_condition = list(nodes.keys())
l_samples = {}
for condition in nodes:
    l_samples[condition] = []
    for sample in nodes[condition]:
        l_samples[condition].append(sample)
l_edges = list(edges.keys())


styles = {
    'output': {
        'overflow-y': 'scroll',
        'overflow-wrap': 'break-word',
        'height': 'calc(100% - 25px)',
        'border': 'thin lightgrey solid'
    },
    'tab': {'height': 'calc(98vh - 115px)'}
}


app.layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.H1("Transcript Expression"),
            width={'size':6, 'offset':4}
            )
       ),
    dcc.Tabs([
        dcc.Tab(label='Expression Graph', children=[
            dbc.Row([
                dbc.Col([
                    html.Div("Condition"),
                    dcc.Dropdown(
                        id='dropdown-condition-A',
                        value=l_condition[0],
                        clearable=False,
                        options=[
                            {'label': name.capitalize(), 'value': name}
                            for name in l_condition
                            ]
                        ),
                        html.Div("Sample"),
                        dcc.Dropdown(
                            id='dropdown-sample-A',
                            value=l_samples[l_condition[0]][0],
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in l_samples[l_condition[0]]
                                ]
                            ),
                        html.Div("Edge weighting"),
                        dcc.Dropdown(
                            id='dropdown-edges-A',
                            value=l_edges[0],
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in l_edges
                                ]
                            ),
                        html.Button("Download .png", id="btn-get-png-A"),
                        html.Button("Download .svg", id="btn-get-svg-A")
                        ], width={'size':2}
                    ),
                dbc.Col(
                    cyto.Cytoscape(
                        id='cytoscape-A',
                        layout={'name': 'circle'},
                        style={'width': '100%', 'height': '300px'},
                        stylesheet = [
                            {
                                'selector': 'node',
                                'style': {
                                    'label': 'data(label)',
                                    'width': 'data(size)',
                                    'height': 'data(size)',
                                    'background-color': 'data(color)',
                                    'background-blacken': 'data(blacken)'
                                }
                            },
                            {
                                'selector': 'edge',
                                'style': {
                                    'label': 'data(label)',
                                    'width': 'data(weight)',
                                }
                            }
                        ],
                        elements=nodes[l_condition[0]][l_samples[l_condition[0]][0]] + edges[l_edges[0]]
                        ), width={'size':4}
                    ),
                dbc.Col(
                    cyto.Cytoscape(
                        id='cytoscape-B',
                        layout={'name': 'circle'},
                        style={'width': '100%', 'height': '300px'},
                        stylesheet = [
                            {
                                'selector': 'node',
                                'style': {
                                    'label': 'data(label)',
                                    'width': 'data(size)',
                                    'height': 'data(size)',
                                    'background-color': 'data(color)',
                                    'background-blacken': 'data(blacken)'
                                }
                            },
                            {
                                'selector': 'edge',
                                'style': {
                                    'label': 'data(label)',
                                    'width': 'data(weight)'
                                }
                            }
                        ],
                        elements=nodes[l_condition[0]][l_samples[l_condition[0]][0]] + edges[l_edges[0]]
                        ), width={'size':4}
                    ),
                dbc.Col([
                    html.Div("Condition"),
                    dcc.Dropdown(
                        id='dropdown-condition-B',
                        value=l_condition[0],
                        clearable=False,
                        options=[
                            {'label': name.capitalize(), 'value': name}
                            for name in l_condition
                            ]
                        ),
                        html.Div("Sample"),
                        dcc.Dropdown(
                            id='dropdown-sample-B',
                            value=l_samples[l_condition[0]][0],
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in l_samples[l_condition[0]]
                                ]
                            ),
                        html.Div("Edge weighting"),
                        dcc.Dropdown(
                            id='dropdown-edges-B',
                            value=l_edges[0],
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in l_edges
                                ]
                            ),
                        html.Button("Download .png", id="btn-get-png-B"),
                        html.Button("Download .svg", id="btn-get-svg-B")
                        ], width={'size':2}
                    )
                ]),
            dbc.Row([
                dbc.Col([
                    html.Div("Condition"),
                    dcc.Dropdown(
                        id='dropdown-condition-C',
                        value=l_condition[0],
                        clearable=False,
                        options=[
                            {'label': name.capitalize(), 'value': name}
                            for name in l_condition
                            ]
                        ),
                        html.Div("Sample"),
                        dcc.Dropdown(
                            id='dropdown-sample-C',
                            value=l_samples[l_condition[0]][0],
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in l_samples[l_condition[0]]
                                ]
                            ),
                        html.Div("Edge weighting"),
                        dcc.Dropdown(
                            id='dropdown-edges-C',
                            value=l_edges[0],
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in l_edges
                                ]
                            ),
                        html.Button("Download .png", id="btn-get-png-C"),
                        html.Button("Download .svg", id="btn-get-svg-C")
                        ], width={'size':2}
                    ),
                dbc.Col(
                    cyto.Cytoscape(
                        id='cytoscape-C',
                        layout={'name': 'circle'},
                        style={'width': '100%', 'height': '300px'},
                        stylesheet = [
                            {
                                'selector': 'node',
                                'style': {
                                    'label': 'data(label)',
                                    'width': 'data(size)',
                                    'height': 'data(size)',
                                    'background-color': 'data(color)',
                                    'background-blacken': 'data(blacken)'
                                }
                            },
                            {
                                'selector': 'edge',
                                'style': {
                                    'label': 'data(label)',
                                    'width': 'data(weight)'
                                }
                            }
                        ],
                        elements=nodes[l_condition[0]][l_samples[l_condition[0]][0]] + edges[l_edges[0]]
                        ), width={'size':4}
                    ),
                dbc.Col(
                    cyto.Cytoscape(
                        id='cytoscape-D',
                        layout={'name': 'circle'},
                        style={'width': '100%', 'height': '300px'},
                        stylesheet = [
                            {
                                'selector': 'node',
                                'style': {
                                    'label': 'data(label)',
                                    'width': 'data(size)',
                                    'height': 'data(size)',
                                    'background-color': 'data(color)',
                                    'background-blacken': 'data(blacken)'
                                }
                            },
                            {
                                'selector': 'edge',
                                'style': {
                                    'label': 'data(label)',
                                    'width': 'data(weight)',
                                }
                            }
                        ],
                        elements=nodes[l_condition[0]][l_samples[l_condition[0]][0]] + edges[l_edges[0]]
                        ), width={'size':4}
                    ),
                dbc.Col([
                    html.Div("Condition"),
                    dcc.Dropdown(
                        id='dropdown-condition-D',
                        value=l_condition[0],
                        clearable=False,
                        options=[
                            {'label': name.capitalize(), 'value': name}
                            for name in l_condition
                            ]
                        ),
                        html.Div("Sample"),
                        dcc.Dropdown(
                            id='dropdown-sample-D',
                            value=l_samples[l_condition[0]][0],
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in l_samples[l_condition[0]]
                                ]
                            ),
                        html.Div("Edge weighting"),
                        dcc.Dropdown(
                            id='dropdown-edges-D',
                            value=l_edges[0],
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in l_edges
                                ]
                            ),
                        html.Button("Download .png", id="btn-get-png-D"),
                        html.Button("Download .svg", id="btn-get-svg-D")
                        ], width={'size':2}
                    )
                ])
            ]),
            dcc.Tab(label='Tab two', children=[])
        ]),
        html.Div(id="hidden-data-value", style=dict(display="none"), **{
          "data-value-1": "hello",
          "data-value-2": "false"
        })
    ])


# Choose Condition Callbacks
@app.callback([Output('dropdown-sample-A', 'options'), 
               Output('dropdown-sample-A', 'value')],
              Input('dropdown-condition-A', 'value'))
def update_samples(value):
    options=[
            {'label': name.capitalize(), 'value': name}
            for name in l_samples[value]
            ]
    new_value = l_samples[value][0]
    return options, new_value

@app.callback([Output('dropdown-sample-B', 'options'), 
               Output('dropdown-sample-B', 'value')],
              Input('dropdown-condition-B', 'value'))
def update_samples(value):
    options=[
            {'label': name.capitalize(), 'value': name}
            for name in l_samples[value]
            ]
    new_value = l_samples[value][0]
    return options, new_value

@app.callback([Output('dropdown-sample-C', 'options'), 
               Output('dropdown-sample-C', 'value')],
              Input('dropdown-condition-C', 'value'))
def update_samples(value):
    options=[
            {'label': name.capitalize(), 'value': name}
            for name in l_samples[value]
            ]
    new_value = l_samples[value][0]
    return options, new_value

@app.callback([Output('dropdown-sample-D', 'options'), 
               Output('dropdown-sample-D', 'value')],
              Input('dropdown-condition-D', 'value'))
def update_samples(value):
    options=[
            {'label': name.capitalize(), 'value': name}
            for name in l_samples[value]
            ]
    new_value = l_samples[value][0]
    return options, new_value


# Choose update graph Callbacks
@app.callback(Output('cytoscape-A', 'elements'),
              [Input('dropdown-sample-A', 'value'),
               Input('dropdown-edges-A', 'value')],
              State('dropdown-condition-A', 'value'))
def update_samples(sample, edge, condition):
    elements = nodes[condition][sample] + edges[edge]
    return elements

@app.callback(Output('cytoscape-B', 'elements'),
              [Input('dropdown-sample-B', 'value'),
               Input('dropdown-edges-B', 'value')],
              State('dropdown-condition-B', 'value'))
def update_samples(sample, edge, condition):
    elements = nodes[condition][sample] + edges[edge]
    return elements

@app.callback(Output('cytoscape-C', 'elements'),
              [Input('dropdown-sample-C', 'value'),
               Input('dropdown-edges-C', 'value')],
              State('dropdown-condition-C', 'value'))
def update_samples(sample, edge, condition):
    elements = nodes[condition][sample] + edges[edge]
    return elements

@app.callback(Output('cytoscape-D', 'elements'),
              [Input('dropdown-sample-D', 'value'),
               Input('dropdown-edges-D', 'value')],
              State('dropdown-condition-D', 'value'))
def update_samples(sample, edge, condition):
    elements = nodes[condition][sample] + edges[edge]
    return elements


# Download Callbacks
@app.callback(
    Output("cytoscape-A", "generateImage"),
    [
        Input("btn-get-png-A", "n_clicks"),
        Input("btn-get-svg-A", "n_clicks"),
    ])
def get_image(get_png_clicks, get_svg_clicks):
    ftype = 'png'
    action = 'store'
    ctx = dash.callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        action = "download"
        ftype = input_id.split("-")[2]

    return {
        'type': ftype,
        'action': action
        }

@app.callback(
    Output("cytoscape-B", "generateImage"),
    [
        Input("btn-get-png-B", "n_clicks"),
        Input("btn-get-svg-B", "n_clicks"),
    ])
def get_image(get_png_clicks, get_svg_clicks):
    ftype = 'png'
    action = 'store'
    ctx = dash.callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        action = "download"
        ftype = input_id.split("-")[2]

    return {
        'type': ftype,
        'action': action
        }

@app.callback(
    Output("cytoscape-C", "generateImage"),
    [
        Input("btn-get-png-C", "n_clicks"),
        Input("btn-get-svg-C", "n_clicks"),
    ])
def get_image(get_png_clicks, get_svg_clicks):
    ftype = 'png'
    action = 'store'
    ctx = dash.callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        action = "download"
        ftype = input_id.split("-")[2]

    return {
        'type': ftype,
        'action': action
        }

@app.callback(
    Output("cytoscape-D", "generateImage"),
    [
        Input("btn-get-png-D", "n_clicks"),
        Input("btn-get-svg-D", "n_clicks"),
    ])
def get_image(get_png_clicks, get_svg_clicks):
    ftype = 'png'
    action = 'store'
    ctx = dash.callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        action = "download"
        ftype = input_id.split("-")[2]

    return {
        'type': ftype,
        'action': action
        }


def main():
    app.run_server(debug=True)


if __name__ == '__main__':
    app.run_server(debug=True)
