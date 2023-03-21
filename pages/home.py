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
                           'padding-top' : 3,'padding-right' : 0},className='pt-4')

           ],href='http://127.0.0.1:6500/protection'),
           html.P('Children protection indicators includes protection of young girls from getting married or union at early ages \n'
                  'and protects girls to any other kind of violence such as sexual violence, physical violence and psychological violence.\n'
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

                ,className='pt-4')
            ],href='http://127.0.0.1:6500/environment'),
            html.P('Children Environment related indicators includes indicators related to access to drinking water services\n'
                   'and access to sanitation services. the indicators includes also the proportions of population \n'
                   'with a basic handwashing facility with soap and water available on premises \n'
                   'and the proportion of population practicing open defecation.',className='text-info bg-light pt-3')
        ],width=4),

        dbc.Col([
            html.Label('Education: Access to infrastructures at School',className="text-primary mb-4 font-weight-bold"),
            html.A([
                html.Img(
                    src='https://www.thegaudium.com/wp-content/uploads/2021/11/The_Gaudium_International_School_Hyderabad_Role_Of_School_2021_11_3.jpg',
                    style={'height' : '80%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 3,'padding-right' : 0}
                ,className='pt-4')
            ],href='http://127.0.0.1:6500/learning'),

            html.P('The children education indicators includes indicators related to children from their \n'
                   'nursery to lower secondary education. there are also indicators to schools infrastructures such as \n'
                   'Proportions of schools with access to electricity, Proportions of schools with access to internet, proportions of schools \n'
                   'with basic handwashing services and many more.',className='text-info bg-light pt-3')
        ],width=4)
       ]),

    dbc.Row([
        dbc.Col([
            html.Label('Survive and thrive',className='text-primary mb-4 font-weight-bold'),
            html.A([
                html.Img(
                    src='https://www.interiorhealth.ca/sites/default/files/styles/details_page_banner_mobile/public/2021-10/Children%20%26%20Youth%20Health%20Banner.png?itok=PSS8vt_J',
                    style={'height' : '60%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 3,'padding-right' : 0})

            ],href='http://127.0.0.1:6500/pages/survive-and-thrive'),
            html.P('Survive and thrive children related indicators includes adolescent birth rate, birth attended by skilled person, \n'
                   'Underfive mortality rate, Neonatal mortality rate, malnutrition (stunting, wasting and overweight) \n'
                   'infants receiving measles containing vaccine (MCV), surviving receiving 3 doses of diphtheria-\n'
                   'tetanus-pertussis (DTP3)',className='text-info bg-light pt-3')
        ],width=4),

        dbc.Col([
            html.Label('Child Poverty',className='text-primary mb-4 font-weight-bold'),
            html.A([
                html.Img(
                    src='https://www.compassion.com/Images/effects-of-poverty-on-children_144714_640x276.jpg',
                    style={'height' : '60%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 3,'padding-right' : 0}
                )
            ],href='http://127.0.0.1:6500/child-poverty'),
            html.P('Children Poverty related indicators includes children living in households in extreme poverty. \n'
                   'Children living below the national poverty line, children living in all its dimensions according to national definitions \n'
                   'and proportions of child populations covered by social protection floors/systems',className='text-info bg-light pt-3')
        ],width=4),
        dbc.Col([
            html.Label('Population',className='text-primary mb-4 font-weight-bold'),
            html.A([
                html.Img(
                    src='https://thewhistler.ng/wp-content/uploads/2017/10/Africa-children-1.jpg',
                    style={'height' : '60%','width': '30%',
                           'float' : 'left','position' : 'static',
                           'padding-top' : 0,'padding-right' : 0})
            ],href='http://127.0.0.1:6500/population')
        ])
    ])


])