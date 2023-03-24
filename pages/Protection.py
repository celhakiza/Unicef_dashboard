#import useful libraries
import dash
from dash.dependencies import Output, Input
import pandas as pd
from dash import html,callback
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px

dash.register_page(__name__,order=2)

#import dataset
df_protection_female_violence = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\protection_female_violence.csv')
df_child_labor = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\child_labor_sex_melt.csv')
df_child_birth_registration = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\child_registration_melt.csv')

df_regist_census = pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\birth_registration_0_17.xlsx')

#print(df_child_birth_registration)

# app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
#               meta_tags=[{'name': 'viewport',
#                             'content': 'width=device-width, initial-scale=1.0'}]
#                 )
# server=app.server

layout = dbc.Container([
    dbc.Row([html.H2('Children Protection related indicators',className="text-center text-primary mb-4 font-weight-bold")
             ]),

    dbc.Row([
        dbc.Col([
            html.Label('Violence against women and girls',className="text-center text-primary mb-4 font-weight-bold"),
            html.P('The graph shows different indicators of violence of women and girls, and \n'
                   'women and girls in their 20-24 ages who were married or in union in their 15s to 18s'),
            dcc.Dropdown(id='women-violence',
                         multi=True,
                         value=['sexual violence'],
                         options=[{'label':x,'value':x} for x in df_protection_female_violence['indicator'].unique()],className='w-50'),
            dcc.Graph(id='graph-violence',figure={}),
            dcc.Markdown('Source: DHS, NISR',className="text-center text-primary mb-4 font-weight-bold")
        ],width=4),
        dbc.Col([
            html.Label('Child Labor',className="text-center text-primary mb-4 font-weight-bold"),
            html.P('The graph shows the comparison of children aged 5-17 engaged in labor.\n'
                   'the data are disagregated by gender (Both sexes, Male and Female). you can compare child labor\n'
                   'between male and female or both.'),
            dcc.Checklist(id='child-labor',
                          value=['Both'],
                          options=[{'label':x,'value':x} for x in df_child_labor['Sex'].unique()],className='w-25'),
            dcc.Graph(id='graph-labor',figure={}),
            dcc.Markdown('Source: EICV, NISR',className="text-center text-primary mb-4 font-weight-bold")
        ],width=4),

        dbc.Col([
            html.Label('Children registered in Civil Authority',className="text-center text-primary mb-4 font-weight-bold"),
            html.P('This graph shows the trend in registration of Children at civil authority.\n'
                   'the data are disaggregated by sex (Both sexes, Male, Female). the disaggregated by Male and Female\n'
                   'are only available from 2021. to select data, we use the same checklist as that of child labor'),
            dcc.Graph(id='registration',figure={}),
            dcc.Markdown('Source: DHS, NISR',className="text-center text-primary mb-4 font-weight-bold")
        ])
    ])

    ])

@callback(
    Output('graph-violence','figure'),
    Input('women-violence','value')
)
def viol(seleviol):
    if len(seleviol) ==0:
        return dash.no_update
    else:
        df_protection_female_violence_df=df_protection_female_violence[df_protection_female_violence['indicator'].isin(seleviol)]
        fig = px.line(df_protection_female_violence_df,
                      x='Year',
                      y='Female',
                      color='indicator')
        fig.update_layout(xaxis_title = 'Year', yaxis_title = 'Percentage (%)',title = 'Violence against women and girls')
        fig.update_traces(showlegend=False)
        fig.update_layout(
            title_font_color='blue',
            font_color='blue',
            font_family='Times New Roman',
            legend_title_font_color='blue',
            title_font_family='Arial',
            showlegend=False,
            plot_bgcolor='white')
        return fig
@callback(
    Output('graph-labor','figure'),
    Input('child-labor','value')
)
def labor(selab):
    if len(selab) ==0:
        return dash.no_update
    else:
        df_child_labor_df=df_child_labor[df_child_labor['Sex'].isin(selab)]
        fig=px.line(df_child_labor_df,
                   x='year',
                   y='value',
                   color='Sex')
                   #barmode='group')
        fig.update_layout(xaxis_title='Year', yaxis_title='Percentage of child labor',title = 'Child Labor')
        fig.update_traces(showlegend=False)
        fig.update_layout(
            title_font_color='blue',
            font_color='blue',
            font_family='Times New Roman',
            legend_title_font_color='blue',
            title_font_family='Arial',
            showlegend=False,
            plot_bgcolor='white')
        return fig
@callback(
    Output('registration','figure'),
    Input('child-labor','value')
)
def regist(selregi):
    if len(selregi)==0:
        return dash.no_update
    else:
        df_child_birth_registration_df = df_child_birth_registration[df_child_birth_registration['Sex'].isin(selregi)]
        fig = px.bar(df_child_birth_registration_df,
                     x='year',
                     y='percentage',
                     color='Sex',
                     barmode='group')
        fig.update_layout(xaxis_title='Year',yaxis_title = 'Percentage', title = 'Birth registration trend')
        fig.update_traces(showlegend=False)
        fig.update_layout(
            title_font_color='blue',
            font_color='blue',
            font_family='Times New Roman',
            legend_title_font_color='blue',
            title_font_family='Arial',
            showlegend=False,
            plot_bgcolor='white')
        return fig


#app.run_server(debug=True, port=8000)


