import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Estimar", href="/")),
        dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
        dbc.NavItem(dbc.NavLink("Acerca de", href="/about")),
        #dbc.DropdownMenu(
        #    children=[
        #        dbc.DropdownMenuItem("Estimar", href="/"),
                #dbc.DropdownMenuItem(divider=True),
        #        dbc.DropdownMenuItem("Dashboard", href="/dashboard"),
        #        dbc.DropdownMenuItem("Acerca de", href="/about"),
        #    ],
        #    nav=True,
        #    in_navbar=True,
        #    label="Menú",
        #),
    ],
    brand="Bienes Raíces\nSanta Cruz de la Sierra",
    brand_style={"whiteSpace": "pre-wrap"},
    brand_href="/",
    color="primary",
    dark=True,
)
   
