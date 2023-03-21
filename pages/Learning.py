#import useful libraries
import dash
from dash.dependencies import Output, Input
import pandas as pd
from dash import html,callback
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px

dash.register_page(__name__,order=4)

#import datasets
df_organized = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\df_learning.csv') #organized learning
df_school_infr = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\df_schools_infr.csv') #schools infrastructures

layout = dbc.Container([
    dbc.Row([
        html.H2('Education related indicators',className="text-center text-primary mb-4 font-weight-bold")
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Participation rate in organized learning (one year before the official primary entry age)',className="text-center text-primary mb-4 font-weight-bold"),
            dcc.Dropdown(id='learning',
                         value=['Both'],
                         multi=True,
                         options=[{'label':x,'value':x} for x in df_organized['Sex'].unique()]),
            dcc.Graph(id='graph-learning',figure={})
        ],width=6),

        dbc.Col([
            html.Label('Access to infrastructures for Schools',className="text-center text-primary mb-4 font-weight-bold"),
            dcc.Dropdown(id='infr',
                         value=['Proportion of schools with access to electricity - Nursery'],
                         multi=True,
                         options=[{'label':x,'value':x} for x in df_school_infr['indicator'].unique()]),
            dcc.Graph(id='graph-infr',figure={})

        ])
    ,
    dcc.Markdown('Source: MINEDUC',className="text-center text-primary mb-4 font-weight-bold")]
    )
])

@callback(
    Output('graph-learning','figure'),
    Input('learning','value')
)
def learning(slctlearn):
    df_organized_df = df_organized[df_organized['Sex'].isin(slctlearn)]
    fig = px.bar(df_organized_df,
                 x='year',
                 y='percentage',
                 barmode='group',
                 color='Sex')
    fig.update_layout(xaxis_title='Year',yaxis_title='Percentage (%)',title='Participation in organized learning')
    return fig
@callback(
    Output('graph-infr','figure'),
    Input('infr','value')
)
def infr(slctinf):
    df_school_inf_df =df_school_infr[df_school_infr['indicator'].isin(slctinf)]
    fig=px.line(df_school_inf_df,
                x='year',
                y='percentage',
                color='indicator')
    fig.update_layout(xaxis_title='Year',yaxis_title='Percentage (%)',title='Access to infrastructures for Schools')
    fig.update_traces(showlegend=False)
    return fig
