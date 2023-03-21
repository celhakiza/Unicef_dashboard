#import useful libraries
import dash
from dash.dependencies import Output, Input
import pandas as pd
from dash import html,callback
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px

#import datasets

df_enviro_water = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\environ_drinking_water.csv') #water data
df_enviro_sanitation = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\environment_sanitation.csv')

dash.register_page(__name__,order=3)

layout = dbc.Container([
    dbc.Row([
        html.H2('Environment related Indicators',className="text-center text-primary mb-4 font-weight-bold")
    ]),

    dbc.Row([
        dbc.Col([
            html.Label('drinking water services',className="text-center text-primary mb-4 font-weight-bold"),
            dcc.Dropdown(id='water-services',
                         value=2020,
                         multi=False,
                         options=[{'label':x,'value':x } for x in df_enviro_water['year'].unique()]),
            dcc.Graph(id='graph-water',figure={}),
            dcc.Markdown('Source: EICV, NISR',className="text-center text-primary mb-4 font-weight-bold")
        ],width=6),

        dbc.Col([
            html.Label('Sanitation services',className="text-center text-primary mb-4 font-weight-bold"),
            dcc.Graph(id='graph-sanitation',figure={}),
            dcc.Markdown('Source: EICV, NISR',className="text-center text-primary mb-4 font-weight-bold")
        ],width=6)
    ])
])
@callback(
    Output('graph-water','figure'),
    Input('water-services','value')
)

def water(slcyear):
    df_enviro_water_df=df_enviro_water[df_enviro_water['year']==slcyear]
    fig = px.pie(df_enviro_water_df,
                 names='indicator',
                 values='percentage',
                 hover_name='indicator',
                 hole=0.3)
    fig.update(layout_title_text='Access to drinking water services in {}'.format(slcyear),
               layout_showlegend=False)

    return fig

@callback(
    Output('graph-sanitation','figure'),
    Input('water-services','value')
)

def sanitation(sanityear):
    df_enviro_san_df=df_enviro_sanitation[df_enviro_sanitation['year']==sanityear]
    fig = px.pie(df_enviro_san_df,
                 names='indicator',
                 values='percentage',
                 hover_name='indicator',
                 hole=0.3)
    fig.update(layout_title_text='Access to sanitation services in {}'.format(sanityear),
               layout_showlegend=False)

    return fig

