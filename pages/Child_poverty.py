#import useful libraries
import dash
from dash.dependencies import Output, Input
import pandas as pd
from dash import html,callback
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px

#import dataset
dash.register_page(__name__,order=5)
df_child_poverty = pd.read_csv(r'C:\Users\ENVY\PycharmProjects\Unicef_dashboard\EICV dash\children_poverty.csv')
layout = dbc.Container([])