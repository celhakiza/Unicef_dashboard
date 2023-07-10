#import useful libraries
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash import callback
from dash.dependencies import Output, Input
import plotly.express as px

# Create the Dash app
dash.register_page(__name__,order=5)
# Import dataset
df_child_poverty = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\children_poverty.csv')
df_child_moda_4 = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\moda_4.csv')
df_child_moda_7 = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\moda_7.csv')

# Layout
layout = dbc.Container([
    dbc.Row(html.H2('Trend in Child poverty in Rwanda', className="text-center text-primary mb-4 font-weight-bold")),
    dbc.Row([
        dbc.Col([
            html.H4('Children Monetary Poverty', style={'color': 'blue'}),
            html.Div('Select gender:', className="text-primary mb-4 font-weight-bold"),
            dcc.Checklist(
                id='pov',
                value=['Male'],
                options=[{'label': x, 'value': x} for x in df_child_poverty['Sex'].unique()]
            ),
            dcc.Graph(id='pove-graph', style={'width': '500px', 'height': '300px'}),
            html.P([
                'Children poverty trends shows at which percentage are the population under the age of 18 who are below the ',
                html.Mark("poverty line"), ' as the data from', html.Mark("EICV"),
                ' shows. The data are available for two EICV: one conducted in', html.Mark("2013/2014"),
                ' and the other conducted in', html.Mark("2016/2017"), '.']
            )
        ], width=5, style={'margin-right': '20px'}),
        dbc.Col([
            html.H4('Multidimensional Overlapping Deprivation Analysis (MODA)', style={'color': 'blue'}),
            dcc.Dropdown(
                id='moda',
                value='Multidimensional Child poverty for children aged 5 - 14',
                options=[
                    'Multidimensional Child poverty for children aged 5 - 14',
                    'Multidimensional Child poverty for children aged 15 - 17'
                ],
                style={
                    'width': '85%',
                    'font-size': '15px',
                    'margin-bottom': '20px',
                    'font-weight': 'lighter'
                }
            ),
            dcc.Graph(id='moda-graph', figure={}),
            html.P(
                'The graph shows the comparison of MODA for the dimensions of Housing, Health, Sanitation, Education, and Water. '
                'It compares data between EICV 2013/2014 and 2016/2017',
                style={
                    'font-family': 'Times New Roman',
                    'font-size': '15px',
                    'font-style': 'italic'
                }
            )
        ], width=6)
    ])
])


@callback(
    Output(component_id='pove-graph', component_property='figure'),
    Input(component_id='pov', component_property='value')
)
def pov(selesex):
    if len(selesex) == 0:
        return dash.no_update
    else:
        dff_poverty = df_child_poverty[df_child_poverty['Sex'].isin(selesex)]
        fig = px.line(dff_poverty, x='year', y='percentage', color='Sex')
        fig.update_layout(
            xaxis_title='Year',
            yaxis_title='Percentage',
            title='Trend in Children poverty',
            title_font_color='blue',
            yaxis_range=[44, 49],
            font_color='blue',
            font_family='Times New Roman',
            legend_title_font_color='blue',
            title_font_family='Arial',
            showlegend=False,
            plot_bgcolor='white'
        )
        return fig


@callback(
    Output('moda-graph', 'figure'),
    Input('moda', 'value')
)
def moda_pov(slctind):
    if len(slctind) == 0:
        return dash.no_update
    elif slctind == 'Multidimensional Child poverty for children aged 5 - 14':
        fig = px.bar(df_child_moda_4, x='deprivation', y='percentage', barmode='group',color='year')
        return fig
    elif slctind == 'Multidimensional Child poverty for children aged 15 - 17':
        fig = px.bar(df_child_moda_7, x='deprivation', y='percentage', barmode='group',color='year')
        return fig

#
# if __name__ == '__main__':
#     app.run_server(debug=True)
