import os
import pandas as pd
from pymongo import MongoClient
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from censusAPI.censusCfg import Api

# labels = {
#     "water_level": ["height", "Feet"],
#     "water_temperature": ["temp", "Temperature(degrees F)"],
#     "wind": ["Speed", "Gust", "Direction"],
# }

dectest = Api.decSelfRepRates("table")
print(dectest)