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
                html.H1('Rwanda indicators related to Children',className="text-center text-primary mb-4 font-weight-bold")
            ],width=12)
        ]),

        dbc.Row([
           dbc.Col([
                   dbc.Carousel(
                       items=[
                           {'key':'1','src':'https://www.shutterstock.com/image-vector/child-safety-icon-vector-set-260nw-2170501809.jpg','caption':'Child protection',"img_style":{"max-height":"400px"}},
                           {'key':'2','src':'https://www.unicef.org/turkiye/sites/unicef.org.turkiye/files/styles/hero_desktop/public/UN0199405.jpg?itok=vGJFERuI','caption':'Hygiene and sanitation',"img_style":{"max-height":"400px"}},
                           {'key':'3','src':'https://i0.wp.com/theblackwallsttimes.com/wp-content/uploads/2019/07/Black-students-800x393.jpg?fit=880%2C393&ssl=1','caption':'Education',"img_style":{"max-height":"450px"}},
                           {'key':'4','src':'https://www.interiorhealth.ca/sites/default/files/styles/details_page_banner_mobile/public/2021-10/Children%20%26%20Youth%20Health%20Banner.png?itok=PSS8vt_J','caption':'Survive and Thrive',"img_style":{"max-height":"400px"}},
                           {'key':'5','src':'https://www.compassion.com/Images/effects-of-poverty-on-children_144714_640x276.jpg','caption':'Child Poverty',"img_style":{"max-height":"600px"}},
                           {'key':'6','src':'https://thewhistler.ng/wp-content/uploads/2017/10/Africa-children-1.jpg','caption':'Child Population',"img_style":{"max-height":"400px"}}],

                    controls=True,
                    indicators=True,
                    interval=4000,
                    ride="carousel",
    #                 className="carousel-fade"
                )
            ], width=6,className='w-75')
        ], justify="center"),

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

