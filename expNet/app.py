import dash
import dash_cytoscape as cyto
from dash import html
from dash import dcc
from dash import dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from sys import argv
from expNet.help_functions import get_colorscale
from expNet import read_data


cyto.load_extra_layouts()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])


colors = get_colorscale('green', 'yellow', 'red')
exp, sample_dict, gene_ids = read_data.read_expression_data(argv[1], argv[2], argv[3]) # expression_path, sample_path, gene_id_path

l_condition = list(sample_dict.keys())
l_samples = {}
mock_nodes = {}
mock_edges = {}
for condition in sample_dict:
    l_samples[condition] = ['mean']
    mock_nodes[condition] = {'mean': []}
    for sample in sample_dict[condition]:
        mock_nodes[condition][sample] = []
        l_samples[condition].append(sample)
l_edges = ['normal', 'transmembrane']

for edge in l_edges:
    mock_edges[edge] = []


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
        dbc.Col([
            html.H1("ExpNet", style={'textAlign': 'center'}),
            dcc.Dropdown(
                id='dropdown-genes',
                clearable=False,
                value=gene_ids[0],
                options=[
                    {'label': name.capitalize(), 'value': name}
                    for name in gene_ids
                    ]
            )],
            width={'size':12}
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
                        style={'width': '100%', 'height': '40vh'},
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
                        elements=[]
                        ), width={'size':4}
                    ),
                dbc.Col(
                    cyto.Cytoscape(
                        id='cytoscape-B',
                        layout={'name': 'circle'},
                        style={'width': '100%', 'height': '40vh'},
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
                        elements=[]
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
                        style={'width': '100%', 'height': '40vh'},
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
                        elements=[]
                        ), width={'size':4}
                    ),
                dbc.Col(
                    cyto.Cytoscape(
                        id='cytoscape-D',
                        layout={'name': 'circle'},
                        style={'width': '100%', 'height': '40vh'},
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
                        elements=[]
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
            dcc.Tab(label='Gene Expression [FPKM]', children=[
                dbc.Row(
                    dbc.Col(
                        html.H3("Gene Expression", style={'textAlign': 'center'}),
                        width={'size':12}
                        )
                   ),
                dbc.Row(
                    dbc.Col(
                        dash_table.DataTable(
                                             id='expression-table',
                                             data={},
                                             columns=[],
                                             style_cell={'textAlign': 'left'},
                                             style_as_list_view=True,
                                            )
                        )
                   ),
            ])
        ]),
        html.Div(id="hidden-data-value", style=dict(display="none"), **{
          "data-value-1": "hello",
          "data-value-2": "false"
        }),
        dcc.Store(id='nodes-store', data=mock_nodes),
        dcc.Store(id='edges-store', data=mock_edges)
    ])


# Choose Gene Callback
@app.callback([Output('nodes-store', 'data'), 
               Output('edges-store', 'data'),
               Output('expression-table', 'data'),
               Output('expression-table', 'columns'),
               Output('dropdown-condition-A', 'value'),
               Output('dropdown-condition-B', 'value'),
               Output('dropdown-condition-C', 'value'),
               Output('dropdown-condition-D', 'value')],
              Input('dropdown-genes', 'value'))
def update_gene(gene_id):
    nodes, edges, gene_expression = read_data.prepare_gene_data(argv[4], gene_id, exp[gene_id], sample_dict, colors) # fas_path
    x = l_condition
    while len(x) < 4:
        x = x + x
    return nodes, edges, gene_expression.to_dict('records'), [{'id': c, 'name': c} for c in gene_expression.columns], x[0], x[1], x[2], x[3]


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
              [State('dropdown-condition-A', 'value'),
               State('nodes-store', 'data'),
               State('edges-store', 'data')])
def update_samples(sample, edge, condition, nodes, edges):
    elements = nodes[condition][sample] + edges[edge]
    return elements

@app.callback(Output('cytoscape-B', 'elements'),
              [Input('dropdown-sample-B', 'value'),
               Input('dropdown-edges-B', 'value')],
              [State('dropdown-condition-B', 'value'),
               State('nodes-store', 'data'),
               State('edges-store', 'data')])
def update_samples(sample, edge, condition, nodes, edges):
    elements = nodes[condition][sample] + edges[edge]
    return elements

@app.callback(Output('cytoscape-C', 'elements'),
              [Input('dropdown-sample-C', 'value'),
               Input('dropdown-edges-C', 'value')],
              [State('dropdown-condition-C', 'value'),
               State('nodes-store', 'data'),
               State('edges-store', 'data')])
def update_samples(sample, edge, condition, nodes, edges):
    elements = nodes[condition][sample] + edges[edge]
    return elements

@app.callback(Output('cytoscape-D', 'elements'),
              [Input('dropdown-sample-D', 'value'),
               Input('dropdown-edges-D', 'value')],
              [State('dropdown-condition-D', 'value'),
               State('nodes-store', 'data'),
               State('edges-store', 'data')])
def update_samples(sample, edge, condition, nodes, edges):
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
    main() # expression_path, sample_path, gene_id_path, fas_path

