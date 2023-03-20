#import useful libraries
import dash
from dash.dependencies import Output, Input
import pandas as pd
from dash import html,callback
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px

#register page

dash.register_page(__name__,path='/',order=0)

#import datasets into pycharm
df_adolescent_birthrate = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\adolescent_res_melt.csv')
df_birth_attended_res = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\birth_attended_res_melt.csv')
df_birth_attended_province = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\attended_skilled_province_melt.csv')
df_vaccine = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\health_vaccine.csv')
df_malnutrition = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\mal_dataset.csv')
df_neonatal_res = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\neonatal_res_melt.csv')
df_neonatal_sex = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\neonatal_sex_melt.csv')
df_underfive_mort_province = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\underfive_mortality_province_melt.csv')
df_underfive_mort_res = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\underfive_mortality_residence_melt.csv')
df_underfive_mort_sex = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\UNICEF\EICV dash\underfive_mortality_sex_melt.csv')

# app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
#               meta_tags=[{'name': 'viewport',
#                             'content': 'width=device-width, initial-scale=1.0'}]
#                 )
# server=app.server

layout = dbc.Container([

  dbc.Row(
      [
      dbc.Col(html.H2('Health related Children Indicators'),className="text-center text-primary mb-4 font-weight-bold",width=12)
  ]),
    dbc.Row(
        [html.Label('Births',className="text-center text-primary mb-4 font-weight-bold"),
            dbc.Col(
                [
                    html.Label('Adolescent birth rate',className="text-center text-primary mb-4 font-weight-bold"),
                    html.P('This graph shows the adolescent birth rate, that is the percentage of girls who gave birth in the age betwen 15-19.\n'
                       'the data available is only for one year for 2020 which is still valid in 2021 as no new same survey done, it is disagregated by residence '),
                    dcc.Dropdown(id='adol-birth'),
                    #              multi=False,
                    #              value='Both',
                    #              options=[{'label':x,'value':x} for x in df_adolescent_birthrate['residence'].unique()]),
                    dcc.Graph(id='graph-adol',figure={}),
                    dcc.Markdown('Source: DHS 2019/2020')
                ]
            ,width=4),
            dbc.Col(
               [
                 html.Label('birth attended by skilled personel- residence',className="text-center text-primary mb-4 font-weight-bold"),
                   dcc.Dropdown(id='residence-birth',
                                multi=False,
                                value='Both',
                                options=[{'label':x,'value':x} for x in df_birth_attended_res['residence'].unique()]),
                   dcc.Graph(id='skilled-birth-res',figure={})

               ],width=4),
            dbc.Col(
                [
                    html.Label('birth attended by skilled personel-province',className="text-center text-primary mb-4 font-weight-bold"),
                    html.P('Attendance birth rate by Province graph allows us to compare how the attendance varies province by province. \n'
                           'you can compare by selecting provinces in the dropdown box'),
                    dcc.Dropdown(id='residence-province',
                                 multi=True,
                                 value=['Kigali city'],
                                 options=[{'label':x,'value':x} for x in df_birth_attended_province['Province'].unique()]),
                    dcc.Graph(id='skilled-birth-pro',figure={}),
                    dcc.Markdown('Source:DHS 2020')
                ],width=4)

        ]
    ),

    html.Hr(),
    dbc.Row(
        [
        dbc.Col(
            [
                html.Label('Vaccination',className="text-center text-primary mb-4 font-weight-bold"),
                dcc.Dropdown(id='vaccination',
                             value='DTP3',
                             options=[{'label':x,'value':x} for x in df_vaccine['indicator'].unique()]
                             ),
                dcc.Graph(id='out-vaccination',figure={})
            ],width=6),
        dbc.Col(
            [
                html.Label('Malnutrition indicators',className="text-center text-primary mb-4 font-weight-bold"),
                dcc.Dropdown(id='malnutrition',
                         multi=True,
                         value=['stunting'],
                         options=[{'label':x,'value':x} for x in df_malnutrition['indicator'].unique()]),
                dcc.Graph(id='out-malnutrition',figure={})
    ],width=6),

    ]
    ),
    html.Hr(),
    dbc.Row(
        [html.Label('Neonatal mortality rate',className="text-center text-primary mb-4 font-weight-bold"),
            dbc.Col(
                [
                    html.Label('Neonatal mortality rate -sex',className="text-center text-primary mb-4 font-weight-bold"),
                    dcc.Dropdown(id='neonatal-sex',
                                 multi=False,
                                 value='Female',
                                 options=[{'label':x,'value':x} for x in df_neonatal_sex['Sex'].unique()]),
                    dcc.Graph(id='grap-neon-sex',figure={})
                ]
            ,width=6),
         dbc.Col(
             [
                 html.Label('Neonatal mortality rate -residence',className="text-center text-primary mb-4 font-weight-bold"),
                 dcc.Dropdown(id='neonatal-res',
                              multi=False,
                              value='Both',
                              options=[{'label':x,'value':x} for x in df_neonatal_res['residence'].unique()]),
                 dcc.Graph(id='graph-neon-res',figure={})
             ]
         ,width=6)
        ]
    ),

    html.Hr(),
    dbc.Row(
        [html.Label('Under five mortality rate',className="text-center text-primary mb-4 font-weight-bold"),

        dbc.Col(
                [
                  html.Label('Under five mortality- sex',className="text-center text-primary mb-4 font-weight-bold"),
                  dcc.Dropdown(id='underfive-mor-sex',
                               multi=False,
                               value='Both',
                               options=[{'label':x,'value':x} for x in df_underfive_mort_sex['Sex'].unique()]),
                  dcc.Graph(id='underfive-graph-sex',figure={})
                ]
            ,width=4),

        dbc.Col(
                [
                  html.Label('Under five mortality- res',className="text-center text-primary mb-4 font-weight-bold"),
                  dcc.Dropdown(id='underfive-mor-res',
                               multi=True,
                               value=['Urban'],
                               options=[{'label':x,'value':x} for x in df_underfive_mort_res['residence'].unique()]),
                  dcc.Graph(id='underfive-graph-res',figure={})
                ]
            ,width=4),

        dbc.Col(
                [
                  html.Label('Under five mortality- prov',className="text-center text-primary mb-4 font-weight-bold"),
                  dcc.Dropdown(id='underfive-mor-prov',
                               multi=True,
                               value=['Kigali city'],
                               options=[{'label':x,'value':x} for x in df_underfive_mort_province['Province'].unique()]),
                  dcc.Graph(id='underfive-graph-prov',figure={})
                ]
        ,width=4),
        ]
    )
]
)

#creating graph for adolescent birth rate
@callback(
    Output('graph-adol','figure'),
    Input('adol-birth','value')
)
def adole(resid):
    df_adolescent_birthrate_df=df_adolescent_birthrate[df_adolescent_birthrate['residence'] == resid]

    fig=px.bar(df_adolescent_birthrate,
                 x='Year',
                 y='percentage',
               color='residence',
               barmode='group')
    fig.update_layout(xaxis_title='Year',yaxis_title='% adolescent birth rate',title='Adolescent birth rate')
    fig.update_traces(showlegend=False)
    return fig
@callback(
    Output('out-malnutrition','figure'),
    Input('malnutrition','value'))
def mal(mal):
    df_malnutrition_df = df_malnutrition[df_malnutrition['indicator'].isin(mal)]
    fig = px.line(df_malnutrition_df,
                 x='year',
                 y=['Both','Male','Female'],
                  color='indicator')
    fig.update_layout(xaxis_title='Year',yaxis_title='Percentage of malnutrition', title='Trend in malnutrition indicators')
    fig.update_traces(showlegend = False)
    return fig
@callback(
    Output('skilled-birth-res','figure'),
    Input('residence-birth','value')
)
def skilled_res(slctresid):
    df_birth_attended_res_df=df_birth_attended_res[df_birth_attended_res['residence'] == slctresid]
    fig = px.line(df_birth_attended_res_df,
                 x='Year',
                 y='percentage'
                 #barmode='group'
)
    fig.update_layout(xaxis_title='Year', yaxis_title = 'Percentage', title = 'Trend in birth attendance by skilled person for {}'.format(slctresid))
    return fig

@callback(
    Output('skilled-birth-pro','figure'),
    Input('residence-province','value')
)

def skilled_pro(slctpro):
    df_birth_attended_province_df = df_birth_attended_province[df_birth_attended_province['Province'].isin(slctpro)]
    fig = px.line(df_birth_attended_province_df,
                 x='year',
                 y='percentage',
                  color='Province')
    fig.update_layout(xaxis_title = 'Year', yaxis_title = 'percentage', title = 'Trend in birth attendance by Province')
    fig.update_traces(showlegend=False)
    return fig

@callback(
    Output('out-vaccination','figure'),
    Input('vaccination','value')
)
def vaccine(slctvac):
    df_vaccine_df = df_vaccine[df_vaccine['indicator'] == slctvac]
    fig = px.bar(df_vaccine_df,
                 x='year',
                 y=['Both','Male','Female'],
                 barmode='group')
    fig.update_layout(xaxis_title='Year',yaxis_title='Percentage',title='Percentage of vaccine for {}'.format(slctvac))
    return fig

@callback(
    Output('grap-neon-sex','figure'),
    Input('neonatal-sex','value')
)
def neonat_sex(slctsex):
    df_neonatal_sex_df =  df_neonatal_sex[ df_neonatal_sex['Sex'] == slctsex]
    fig = px.line(df_neonatal_sex_df,
                  x='year',
                  y='per_thousand')
    fig.update_layout(xaxis_title='Year',yaxis_title='Per_thousand',title='Neonatal mortality rate for {}'.format(slctsex))
    return fig
@callback(
    Output('graph-neon-res','figure'),
    Input('neonatal-res','value')
)

def neonat_res(slctneres):
    df_neonatal_res_df = df_neonatal_res[df_neonatal_res['residence'] == slctneres]
    fig = px.line(df_neonatal_res_df,
                  x='year',
                  y='per_thousand')
    fig.update_layout(xaxis_title = 'Year', yaxis_title = 'Per_thousand',title = 'Neonatal mortality for {}'.format(slctneres))
    return fig

@callback(
    Output('underfive-graph-sex','figure'),
    Input('underfive-mor-sex','value')
)

def underfive_sex(selctsex):
    df_underfive_mort_sex_df = df_underfive_mort_sex[df_underfive_mort_sex['Sex'] ==selctsex]
    fig = px.scatter(df_underfive_mort_sex_df,
                  x='year',
                  y='per_thousand')
    fig.update_layout(xaxis_title = 'Year', yaxis_title = 'Under five mortality rate (per 1000)',title = 'Under five mortality rate for {}'.format(selctsex))
    return fig

@callback(
    Output('underfive-graph-res','figure'),
    Input('underfive-mor-res','value')
)

def underfive_res(selctres):
    df_underfive_mort_res_df = df_underfive_mort_res[df_underfive_mort_res['residence'].isin(selctres)]
    fig = px.scatter(df_underfive_mort_res_df,
                  x='year',
                  y='per_thousand',
                    color='residence',
                     size='per_thousand')

    fig.update_layout(xaxis_title = 'Year', yaxis_title = 'Under five mortality rate (per 1000)',title = 'Under five mortality rate for {}'.format(selctres))
    fig.update_traces(showlegend=False)
    return fig

@callback(
    Output('underfive-graph-prov','figure'),
    Input('underfive-mor-prov','value')
)


def underfive_pro(selctpro):
    df_underfive_mort_province_df=df_underfive_mort_province[df_underfive_mort_province['Province'].isin(selctpro)]
    fig = px.line(df_underfive_mort_province_df,
                  x='year',
                  y='per_thousand',
                  color='Province')
    fig.update_layout(xaxis_title = 'Year',yaxis_title = 'Under five mortality rate (per 1000)',title = 'Under five mortality rate by Province')
    fig.update_traces(showlegend=False)
    return fig

#app.run_server(debug=True,port=7000)

