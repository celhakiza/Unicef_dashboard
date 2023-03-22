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
df_primary = pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\currently_attending_school_6_11.xlsx') #primary students
df_secondary = pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\currently_attending_school_12_17.xlsx')
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
    ),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div('Select province',className="text-center text-primary mb-4 font-weight-bold"),
            dcc.Dropdown(id='prov',
                         value='City of Kigali',
                         options=[{'label':x,'value':x} for x in df_primary['province'].unique()]),
            html.Div(id='sent-provi')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Div('Select district',className="text-center text-primary mb-4 font-weight-bold"),
            dcc.Dropdown(id='distr-dropdown',
                         multi=True,
                         options=[]),
            dcc.Graph(id='graph-pri',figure={})
        ])
    ])

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

@callback(
    Output('distr-dropdown','options'),
    Input('prov','value')
)

def set_cities_options(choosen_province):
    dff_sel_province=df_primary[df_primary['province']==choosen_province]
    return [{'label':x,'value':x} for x in dff_sel_province['district'][1:].unique()]

@callback(
    Output('distr-dropdown','value'),
    Input('distr-dropdown','options')
)

def set_district_value(available_options):

    return[x['value'] for x in available_options]


@callback(
    Output('graph-pri','figure'),
    Input('prov','value'),
    Input('distr-dropdown','value')
)
def update_graph(selected_pro,selected_distr):
    if len(selected_distr) == 0:
        return dash.no_update
    else:
        dff_pop_prim = df_primary[(df_primary['province'] == selected_pro) & (df_primary['district'].isin(selected_distr))].sum().squeeze()[2:5]
        # convert series into a dataframe
        dff_pop_prim = pd.DataFrame(dff_pop_prim)
        # reset index of a dataframe
        dff_pop_prim = dff_pop_prim.reset_index()
        # rename the columns of a dataframe
        dff_pop_prim = dff_pop_prim.rename(columns={'index': 'Sex', 0: 'percentage'})

        fig = px.bar(dff_pop_prim,
                     x='Sex',
                     y='percentage',
                     color='Sex')
        fig.update_layout(yaxis_title='Percentage',title='Percentage of 6-11 age in primary school in {} district'.format(selected_distr))
        return fig
