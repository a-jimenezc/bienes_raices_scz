import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, 
                   path='/about',
                   title="Acerca de")

layout = html.Div(
    children=[
        html.Br(),
        html.Br(),
        html.Br(),

        html.Div([
            html.H4("Sobre el Autor")
            ], style={'textAlign': 'center'}),
        html.P(
            """Esta página web fue hecha por Antonio Jimenez Caballero con 
             el objetivo de usar la Ciencia de Datos
             para responder necesidades concretas."""
        ),

        html.Div(
            className="d-flex justify-content-center",
            children=[
                html.A(
                    href="https://github.com/a-jimenezc",
                    target="_blank",
                    children=[
                        html.I(className="fab fa-github"),
                        " GitHub",
                    ],
                    className="m-2",
                ),
                html.A(
                    href="https://www.linkedin.com/in/antonio-jimnzc",
                    target="_blank",
                    children=[
                        html.I(className="fab fa-linkedin"),
                        " LinkedIn",
                    ],
                    className="m-2",
                ),
                html.A(
                    href="mailto:antonio.jimzC@gmail.com",
                    target="_blank",
                    children=[
                        html.I(className="fab fa-google"),
                        " Gmail",
                    ],
                    className="m-2",
                ),
            ],
        ),
    ],
    className="container mt-4",
)