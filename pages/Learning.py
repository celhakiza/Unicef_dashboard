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
            html.Label('Early Primary Education)',className="text-center text-primary mb-4 font-weight-bold"),
            dcc.Dropdown(id='learning',
                         value=['Both'],
                         multi=True,
                         options=[{'label':x,'value':x} for x in df_organized['Sex'].unique()],className='w-50'),
            dcc.Graph(id='graph-learning',figure={},
                      style = {'width':'500px','height':'300px'})
        ],width=6),

        dbc.Col([
            html.Label('Access to infrastructures for Schools',className="text-center text-primary mb-4 font-weight-bold"),
            html.Br(),
            html.I('Here you find indicators related to: Access to electricity, computers, \n'
                   'handwashing facilities and internet for nursery, primary and secondary education.'),
            html.Br(),
            dcc.Dropdown(id='infr',
                         value=['Proportion of schools with access to electricity - Nursery'],
                         multi=True,
                         options=[{'label':x,'value':x} for x in df_school_infr['indicator'].unique()]),
            dcc.Graph(id='graph-infr',figure={},
                      style = {'width':'600px','height':'300px'})

        ])
    ,
    dcc.Markdown('Source: MINEDUC',className="text-center text-primary mb-4 font-weight-bold")
    ]),
    html.Hr(),
    dbc.Row([
        html.Div('Education',className='text-center text-success mb-4 font-weight-bold')
    ]),
    dbc.Row([
        dbc.Col([
            html.Div('Select district',className="text-center text-primary mb-4 font-weight-bold"),
            html.Div('Primary Education',className="text-center text-primary mb-4 font-weight-bold"),
            dcc.Dropdown(id='district',
                         value='Bugesera',
                         options=[{'label':x,'value':x} for x in sorted(df_primary['district'].unique())],className='text-primary w-25'),
            html.Div(id='sent-provi'),
            dcc.Graph(id='graph-pr',figure={},
                      style = {'width':'400px','height':'300px'})

        ],width=6),

        dbc.Col([
            html.Div('Secondary Education ',className="text-center text-primary mb-4 font-weight-bold"),
            html.Div(id='sent-sec'),
            dcc.Graph(id='graph-sec',figure={},
                      style = {'width':'400px','height':'300px'}),
            dcc.Markdown('Source: Fifth Rwanda population and Housing census',className="text-center text-primary mb-4 font-weight-bold")
        ],width=6)
    ])

])

@callback(
    Output('graph-learning','figure'),
    Input('learning','value')
)
def learning(slctlearn):
    if len(slctlearn) ==0:
        return dash.no_update
    else:
        df_organized_df = df_organized[df_organized['Sex'].isin(slctlearn)]
        fig = px.bar(df_organized_df,
                     x='year',
                     y='percentage',
                     barmode='group',
                     color='Sex')
        fig.update_layout(xaxis_title='Year',yaxis_title='Percentage (%)',title='Early Primary education')
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
    Output('graph-infr','figure'),
    Input('infr','value')
)
def infr(slctinf):
    if len(slctinf) ==0:
        return dash.no_update
    else:
        df_school_inf_df =df_school_infr[df_school_infr['indicator'].isin(slctinf)]
        fig=px.line(df_school_inf_df,
                    x='year',
                    y='percentage',
                    color='indicator')
        fig.update_layout(xaxis_title='Year',yaxis_title='Percentage (%)',title='Access to infrastructures for Schools')
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
    Output('sent-provi','children'),
    Output('graph-pr','figure'),
    Input('district','value')
)
def update_graph_pri(selected_distr):
    if len(selected_distr) == 0:
        return dash.no_update
    else:
        dff_pop_prim = df_primary[(df_primary['district'] == selected_distr)].sum().squeeze()[2:5]
        # convert series into a dataframe
        dff_pop_prim = pd.DataFrame(dff_pop_prim)
        # reset index of a dataframe
        dff_pop_prim = dff_pop_prim.reset_index()
        # rename the columns of a dataframe
        dff_pop_prim = dff_pop_prim.rename(columns={'index': 'Sex', 0: 'percentage'})

        fig = px.bar(dff_pop_prim,
                     x='Sex',
                     y='percentage',
                     text='percentage',
                     color='Sex')
        fig.update_layout(yaxis_title='Percentage',title='Percentage of 6-11 age in primary school in {} district'.format(selected_distr))

        fig.update_traces(showlegend=False)
        fig.update_layout(
            title_font_color='blue',
            font_color='blue',
            font_family='Times New Roman',
            legend_title_font_color='blue',
            title_font_family='Arial',
            showlegend=False,
            plot_bgcolor='white')

        return (('In {} district, {} percent of children between\n'
                    ' 6-11 years enrolled in primary education, female are {}\n'
                    ' percent while male are {} percent.\n'
                 ''.format(selected_distr,round(df_primary[df_primary['district']==selected_distr].squeeze()[2],1),
                           round(df_primary[df_primary['district']==selected_distr].squeeze()[4],1),
                           round(df_primary[df_primary['district']==selected_distr].squeeze()[3],1))),fig)

@callback(
    Output('sent-sec','children'),
    Output('graph-sec','figure'),
    Input('district','value')
)
def update_graph_sec(select):
    if len(select) == 0:
        return dash.no_update

    else:
        dff_pop_sec = df_secondary[(df_secondary['district'] == select)].sum().squeeze()[2:5]
        # convert series into a dataframe
        dff_pop_sec = pd.DataFrame(dff_pop_sec)
        # reset index of a dataframe
        dff_pop_sec = dff_pop_sec.reset_index()
        # rename the columns of a dataframe
        dff_pop_sec = dff_pop_sec.rename(columns={'index': 'Sex', 0: 'percentage'})

        fig = px.bar(dff_pop_sec,
                     x='Sex',
                     y='percentage',
                     text='percentage',
                     color='Sex')
        fig.update_layout(yaxis_title='Percentage',
                          title='Percentage of 12-17 age in secondary school in {} district'.format(select))
        fig.update_traces(showlegend=False)
        fig.update_layout(
            title_font_color='blue',
            font_color='blue',
            font_family='Times New Roman',
            legend_title_font_color='blue',
            title_font_family='Arial',
            showlegend=False,
            plot_bgcolor='white')

        return (('In {} district, {} percent of children between\n'
                 ' 12-17 years enrolled in secondary education, female are {}\n'
                 ' percent while male are {} percent.\n'
                 ''.format(select, round(df_secondary[df_secondary['district'] == select].squeeze()[2], 1),
                           round(df_secondary[df_secondary['district'] == select].squeeze()[4], 1),
                           round(df_secondary[df_secondary['district'] == select].squeeze()[3],1))), fig)

