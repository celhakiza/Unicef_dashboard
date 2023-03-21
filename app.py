'''
This project is about creating interactive dashboard for children in Rwanda for different
indicators of sustainable development goals (SDGs). the dataset used were the data reported.
different data sources: DHS, RBC, EICV
Programming Language: Throughout the whole process, we used python language from data cleaning to creating final products
Unit: Statistical methods research and Publication (SMRP)
'''

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

#importing datasets


app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                    dbc.Nav([
                        dbc.NavLink(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                    ])
            ])
        ],
        fluid=True,
    ),
    dark=True,
    color='blue'
)

app.layout = dbc.Container([header, dash.page_container], fluid=True)

#if __name__ == '__main__':
app.run_server(debug=True,port=6500)

#reading the dataset