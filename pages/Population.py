import dash
from dash.dependencies import Output, Input
import pandas as pd
from dash import html,callback
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px

dash.register_page(__name__,order=6)

#import dataset
df_chil_popul_share = pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\population_share_children.xlsx')
df_chil_pop = pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\children_population.xlsx')

layout = dbc.Container([
    dbc.Row([
        html.H2('Children population in Rwanda',className="text-center text-primary mb-4 font-weight-bold"),
    ]),

    dbc.Row([
        dbc.Col([
            html.P('Children population by district',className="text-start text-primary mb-4 font-weight-bold"),
            html.P('Select district',className="text-start text-primary mb-4 font-weight-bold"),
            dcc.Dropdown(id='district-drpn',
                         value='Bugesera',
                         options=[{'label':x,'value':x} for x in sorted(df_chil_pop['district'].unique())],className='w-25'),
            html.Div(id='sent-pop'),
            dcc.Graph(id='graph-pop',figure={},
                      style = {'width':'400px','height':'300px'})
        ],width=6),

        dbc.Col([
            html.P('Children share to total population',className="text-center text-primary mb-4 font-weight-bold"),
            html.Div(id='sent-sha'),
            dcc.Graph(id='graph-share',figure={},
                      style = {'width':'400px','height':'300px'})
        ],width={'size':5, 'offset':1})
    ]),
    dbc.Row(html.P('Source: Fifth Population and Housing census 2022',className="text-center text-primary mb-4 font-weight-bold"))
])
@callback(
    Output('sent-pop','children'),
    Output('graph-pop','figure'),
    Input('district-drpn','value')
)
def pop(slctdistrict):
    if len(slctdistrict) == 0:
        return dash.no_update
    else:
        dff_pop = df_chil_pop[df_chil_pop['district'] == slctdistrict].sum().squeeze()[2:5]
        dff_pop = pd.DataFrame(dff_pop)
        # reset index of a dataframe
        dff_pop = dff_pop.reset_index()
        # rename the columns of a dataframe
        dff_pop = dff_pop.rename(columns={'index': 'Sex', 0: 'total_pop'})

        fig = px.bar(dff_pop,
                     x='Sex',
                     y='total_pop',
                     color='Sex')
        fig.update_layout(yaxis_title = 'Children Population',title ='Children in {} district'.format(slctdistrict))
        fig.update_layout(
        title_font_color = 'blue',
        font_color = 'blue',
        font_family = 'Times New Roman',
        legend_title_font_color = 'blue',
        title_font_family = 'Arial',
        showlegend = False,
        plot_bgcolor ='white')

        return (('In {}, total number of children between\n'
                 ' 0-17 age is {}, female are {}\n'
                 ' while male are {}.\n'
                 ''.format(slctdistrict, round(df_chil_pop[df_chil_pop['district'] == slctdistrict].squeeze()[2], 1),
                           round(df_chil_pop[df_chil_pop['district'] == slctdistrict].squeeze()[4], 1),
                           round(df_chil_pop[df_chil_pop['district'] == slctdistrict].squeeze()[3], 1))), fig)


@callback(
    Output('sent-sha','children'),
    Output('graph-share','figure'),
    Input('district-drpn','value')
)

def pop_share(slctsha):
    if len(slctsha) == 0:
        return dash.no_update

    else:
        dff_pop_share = df_chil_popul_share[df_chil_popul_share['district'] == slctsha].sum().squeeze()[2:5]
        dff_pop_share = pd.DataFrame(dff_pop_share)
        # reset index of a dataframe
        dff_pop_share = dff_pop_share.reset_index()
        # rename the columns of a dataframe
        dff_pop_share = dff_pop_share.rename(columns={'index': 'Sex', 0: 'per_pop_share'})

        fig = px.bar(dff_pop_share,
                     x='Sex',
                     y='per_pop_share',
                     color='Sex')
        fig.update_layout(yaxis_title='Children share Population', title='Children share in {} district'.format(slctsha))
        fig.update_layout(
            title_font_color='blue',
            font_color='blue',
            font_family='Times New Roman',
            legend_title_font_color='blue',
            title_font_family='Arial',
            autotypenumbers='strict',
            showlegend=False,
            plot_bgcolor='white')

        return (('In {}, children between 0-17 age share {} percent of total population \n'
                 ', female share is {} percent of the total females\n'
                 ' while male share is {} percent of the total male in district.\n'
                 ''.format(slctsha, round(df_chil_popul_share[df_chil_popul_share['district'] == slctsha].squeeze()[2], 1),
                           round(df_chil_popul_share[df_chil_popul_share['district'] == slctsha].squeeze()[4], 1),
                           round(df_chil_popul_share[df_chil_popul_share['district'] == slctsha].squeeze()[3], 1))), fig)


#print(df_chil_pop[df_chil_pop['district'] == 'Nyamagabe'].sum().squeeze()[2:5])
#print(dff_pop)