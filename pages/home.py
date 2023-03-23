'''
the home page is the pop up page that appears directly when you open the link.

'''
import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc

dash.register_page(__name__,path='/',order=0)

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2('Rwanda indicators related to Children',className="text-center text-primary mb-4 font-weight-bold")
        ],width=12)
    ]),

    dbc.Row([
       dbc.Col([
           html.Label('Protection',className="text-primary mb-4 font-weight-bold"),
           html.A([
               html.Img(
                    src='https://cdn2.vectorstock.com/i/1000x1000/97/21/child-protection-sign-vector-25919721.jpg',

                    style={'height' : '80%','width' : '30%',
                           'float' : 'left','position' : 'relative',
                           'padding-top' : 3,'padding-right' : 0},className='w-30 h-30')

           ],href='http://127.0.0.1:6500/protection'),
           html.P('Children protection indicators includes protection of young girls from getting married or union at early ages \n'
                  'and protects girls to any other violence.\n'
                  'there are also indicators related to preventing child labors and the right of \n'
                  'children to be registered in civil authority',className='text-info bg-light pt-3')
           ],width=4),

        dbc.Col([
            html.Label('Hygiene and Sanitation',className="text-primary mb-4 font-weight-bold"),
            html.A([
                html.Img(
                    src='https://www.unicef.org/turkiye/sites/unicef.org.turkiye/files/styles/hero_desktop/public/UN0199405.jpg?itok=vGJFERuI',

                    style={'height' :'80%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 3,'padding-right' : 0}

                ,className='w-30 h-30')
            ],href='http://127.0.0.1:6500/environment'),
            html.P('Children Environment related indicators includes indicators related to access to drinking water services\n'
                   'and access to sanitation services.',className='text-info bg-light pt-3')
        ],width=4),

        dbc.Col([
            html.Label('Education: Access to infrastructures at School',className="text-primary mb-4 font-weight-bold"),
            html.A([
                html.Img(
                    src='https://www.thegaudium.com/wp-content/uploads/2021/11/The_Gaudium_International_School_Hyderabad_Role_Of_School_2021_11_3.jpg',
                    style={'height' : '80%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 3,'padding-right' : 0}
                ,className='w-30 h-30')
            ],href='http://127.0.0.1:6500/learning'),

            html.P('there are also indicators to schools net attendance rate in primary and secondary schools, also infrastructures such as \n'
                   'access to electricity, access to internet and schools\n'
                   'with basic handwashing services.',className='text-info bg-light pt-3')
        ],width=4)
       ]),

    dbc.Row([
        dbc.Col([
            html.Div('Survive and thrive',className='text-primary font-weight-bold m-3'),
            html.A([
                html.Img(
                    src='https://www.interiorhealth.ca/sites/default/files/styles/details_page_banner_mobile/public/2021-10/Children%20%26%20Youth%20Health%20Banner.png?itok=PSS8vt_J',
                    style={'height' : '60%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 3,'padding-right' : 0},className='w-30 h-30')

            ],href='http://127.0.0.1:6500/pages/survive-and-thrive'),
            html.P('Survive and thrive children related indicators such as adolescent birth rate, \n'
                   'Underfive mortality rate, Neonatal mortality rate, malnutrition and vaccination',className='text-info bg-light pt-3')
        ],width=4),

        dbc.Col([
            html.Div('Child Poverty',className='text-primary font-weight-bold m-3'),
            html.A([
                html.Img(
                    src='https://www.compassion.com/Images/effects-of-poverty-on-children_144714_640x276.jpg',
                    style={'height' : '60%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 3,'padding-right' : 0}
                ,className='w-30 h-30')
            ],href='http://127.0.0.1:6500/child-poverty'),
            html.P('Children Poverty related indicators such as children living in households in extreme poverty. \n'
                   'Children living below the national poverty line',className='text-info bg-light pt-3')
        ],width=4),

        dbc.Col([
            html.Div('Population',className='text-primary font-weight-bold m-4'),
            html.A([
                html.Img(
                    src='https://thewhistler.ng/wp-content/uploads/2017/10/Africa-children-1.jpg',
                    style={'height' : '60%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 0,'padding-right' : 0},className='w-30 h-30')
            ],href='http://127.0.0.1:6500/population'),
            html.P('Shows the population who are children in Rwanda. the data used is from fifth Rwanda \n'
                   'population and census carried out in 2022. the data are disaggregated by gender and age group.',className='text-info bg-light pt-3')
        ])
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
        html.A([
            html.Img(
                src='https://getinthepicture.org/sites/default/files/images/partner/logos/unicef.png',
                style={
                        'height' :'100%','width':'30%',
                        'padding-top' :0,'padding-bottom':0
                }
            ,className='w-25')
        ])
        ],width=4),

        dbc.Col([
            html.A([
                html.Img(
                    src='https://cdn.vectorstock.com/i/preview-1x/27/01/rwanda-flag-design-vector-45422701.jpg',
                    style={
                        'height' :'100%','width':'50%',
                        'float':'center', 'position':'relative',
                        'padding-top' :0,'padding-bottom':0
                    }
                ,className='w-40 h-20')
            ])
        ],width=4),

        dbc.Col([
            html.A([
                html.Img(
                    src='https://pbs.twimg.com/profile_images/1115228529812287489/5ciAZeIe_400x400.png',
                    style={
                        'height' :'100%','width':'30%',
                        'float':'right','position':'relative',
                        'padding-top' :0,'padding-bottom':0
                    }
                ,className='w-25')
            ])
        ],width=4)

    ]),
    html.Br(),
    html.Br()


])