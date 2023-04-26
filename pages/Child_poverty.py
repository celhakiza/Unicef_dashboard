#import useful libraries
import dash
from dash.dependencies import Output, Input
import pandas as pd
from dash import html,callback
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px

#import dataset
dash.register_page(__name__,order=5)
df_child_poverty = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\children_poverty.csv')
layout = dbc.Container([
    dbc.Row(html.H2('Trend in Child poverty in Rwanda',className="text-center text-primary mb-4 font-weight-bold")),

    dbc.Row([
        dbc.Col([
            html.H4('Children Monetary Poverty',
                    style={'color':'blue'}),
            html.Div('Select gender:',className="text-primary mb-4 font-weight-bold"),
            dcc.Checklist(id='pov',
                          value=['Male'],
                          options=[{'label':x,'value':x} for x in df_child_poverty['Sex'].unique()]),

            dcc.Graph(id='pove-graph',
                      style = {'width':'500px',
                               'height':'300px'}),
            html.P(['Children poverty trends shows at which percentage are the population under the age of 18 who are below the \n'
                   'poverty line as the data from', html.Mark("EICV"), 'shows. the data are available for two EICV: one conducted in', html.Mark("2013/2014"), 'and the \n'
                   'other conducted in', html.Mark("2016/2017"),'.'])
        ], width=6),

        dbc.Col([
            html.H4('Multidimensional Overlapping Deprivation Analysis (MODA)',
                    style={'color':'blue'})
        ],width=6)
    ])
])
@callback(
    Output(component_id='pove-graph',component_property='figure'),
    Input(component_id='pov',component_property='value')
)
def pov(selesex):
    if len(selesex)==0:
        return dash.no_update
    else:
        dff_poverty = df_child_poverty[df_child_poverty['Sex'].isin(selesex)]
        fig = px.line(dff_poverty,
                      x='year',
                      y='percentage',
                      color='Sex')
        fig.update_layout(xaxis_title='Year', yaxis_title='Percentage',title='Trend in Children poverty')
        fig.update_traces(showlegend=True)
        fig.update_layout(
            title_font_color='blue',
            yaxis_range=[44, 49],
            font_color='blue',
            font_family='Times New Roman',
            legend_title_font_color='blue',
            title_font_family='Arial',
            showlegend=False,
            plot_bgcolor='white')
        return fig
