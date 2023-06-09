import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
import folium
from folium.plugins import MousePosition
import dash_leaflet as dl
import json
from src import predict

# Create a Folium map with mouse position plugin
map = folium.Map(location=[-17.783, -63.182], zoom_start=10)
MousePosition().add_to(map)

dash.register_page(__name__, path='/', title="Estimador")


text_intro_model = html.Div([
    html.H5("Introducir los valores necesarios:")
    ], style={'text-align': 'left',
            'margin-left': '20%'})

input = html.Div([
    html.Div([
        html.Br(),
        html.Label("Número de ambientes:"),
        html.Br(),
        dcc.Input(type="number", 
                  id="ambientes",
                  #placeholder='Número de ambientes',
                  value = 6,
                  step=1, min=0, #required=True,
                  style={
                        'display': 'inline-block',
                        'text-align': 'center',
                        'width': '40%',
                        #'margin': '0.25% 0.25% 0.25% 0.25%'
                        }),
        html.Br(),
        html.Label("Número de dormitorios:"),
        html.Br(),
        dcc.Input(
            type="number",
            id="no_dormitorios",
            #placeholder='Número de dormitorios',
            value = 3,
            step=1, min=0, #required=True,
            style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '40%',
                #'margin': '0.25% 0.25% 0.25% 0.25%'
                }),
        html.Br(),
        html.Label("Número de Baños:"),
        html.Br(),
        dcc.Input(type="number", 
                  id="no_baños",
                  #placeholder='Número de Baños',
                  value = 2,
                  step=1, min=0, #required=True,
                  style={
                        'display': 'inline-block',
                        'text-align': 'center',
                        'width': '40%',
                        #'margin': '0.25% 0.25% 0.25% 0.25%'
                        }),
        html.Br(),
        html.Label("Dimensión del terreno (m2):"),
        html.Br(),
        dcc.Input(
            type="number",
            id="terreno_m2",
            value = 400,
            #placeholder='Dimensión del terreno (m2)',
            step=0.01, min=0, #required=True,
            style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '40%',
                #'margin': '0.25% 0.25% 0.25% 0.25%'
                }),
        html.Br(),
        html.Label("Número de estacionamientos:"),
        html.Br(),
        dcc.Input(
            type="number",
            id="estacionamientos",
            #placeholder='Número de estacionamientos',
            value = 2,
            step=1, min=0, #required=True,
            style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '40%',
                #'margin': '0.25% 0.25% 0.25% 0.25%'
                }),
        html.Br(),
        html.Label("Área construida (m2):"),
        html.Br(),
        dcc.Input(
            type="number",
            id="area_constr_m2",
            #placeholder='Área construida (m2)',
            value = 100,
            step=0.01, min=0, #required=True,
            style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '40%',
                #'margin': '0.25% 0.25% 0.25% 0.25%'
                }),
        html.Br(),
        html.Label("Año de construcción:"),
        html.Br(),
        dcc.Input(
            type="number",
            id="año_constr",
            #placeholder='Año de construcción',
            value = 2018,
            step=1,
            min=1990, max=2025, #required=True,
            style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '40%',
                #'margin': '0.25% 0.25% 0.25% 0.25%'
                }),
        html.Br(),
        html.Label("Seleccionar el tipo de propiedad:"),
        html.Br(),
        dcc.Dropdown(
            options = [
                {'label' : 'Departamento', 'value' : 'Departamento'}, 
                {'label' : 'Casa', 'value' : 'Casa'},
                {'label' : 'Casa con Espacio Comercial', 'value' : 'Casa con Espacio Comercial'}, 
                {'label' : 'Estudio/Monoambiente', 'value' : 'Estudio/Monoambiente'}], 
                      #placeholder='Tipo de propiedad',
                      value='Casa',
                      searchable=True,
                      id='tipo_de_propiedad',
                    style={
                        'display': 'inline-block',
                        'text-align': 'center',
                        'width': '64%'}),
        html.Br(),
        html.Label("Seleccionar la zona:"),
        html.Br(),
        dcc.Dropdown(
            options=[
                {'label': 'Norte', 'value': 'Norte'},
                {'label': 'Sur', 'value': 'Sur'},
                {'label': 'Este', 'value': 'Este'},
                {'label': 'Equipetrol/NorOeste', 'value': 'Equipetrol/NorOeste'},
                {'label': 'Urubo', 'value': 'Urubo'},
                {'label': 'Oeste', 'value': 'Oeste'},
                {'label': 'Sureste', 'value': 'Sureste'},
                {'label': 'Urbari', 'value': 'Urbari'},
                {'label': 'Centro (Casco Viejo)', 'value': 'Centro (Casco Viejo)'},
                {'label': 'ESTE', 'value': 'ESTE'},
                {'label': 'Noreste', 'value': 'Noreste'},
                {'label': 'Suroeste', 'value': 'Suroeste'},
                {'label': 'Noroeste', 'value': 'Noroeste'}],
            #placeholder='Zona',
            value='Este',
            id='zona',
            style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '64%'}),
        html.Br(),
        html.Label("Seleccionar la ciudad:"),
        html.Br(),
        dcc.Dropdown(
            options=[
                {'label': 'Santa Cruz de la Sierra', 'value': 'Santa Cruz de la Sierra'},
                {'label': 'Porongo', 'value': 'Porongo'}],
            #placeholder='ciudad',
            value='Santa Cruz de la Sierra',
            id='ciudad',
            style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '64%'}),
        html.Br(),
        html.Label("Ubicación, hacer click en el mapa:"),
        html.Br(),   
        dcc.Input(
            type="text",
            id="coordenadas",
            #placeholder="Ubicación, hacer click en el mapa",
            value='[-17.77909, -63.16245]',
            #required=True,
            style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '40%',
                'margin': '0.25% 0.25% 0.25% 0.25%'
                }),
        dl.Map(id='MAP_ID',  
               center=[-17.783, -63.182], 
               zoom=14, 
               children=[
                   dl.TileLayer(),
                   dl.Marker(id='pin', 
                             position=[-17.77909, -63.16245], 
                             draggable=False),
                   ],
               style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '60%',
                'height': '300px'}),
        html.Br(),
        html.Br(),
        html.Br(),
        ],style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '100%'}
    )]
)

output = html.Div([
    html.Div([
        html.Button('Estimar', 
                    id='submit-button', 
                    n_clicks=0,
                        style={
                            'border-radius': '5px',
                            'padding': '10px 20px',
    }
),
        html.Br(),
        html.Br(),
        html.H5(id='output')
    ],style={
                'display': 'inline-block',
                'text-align': 'center',
                'width': '100%'}
    )]
)

note_about_output = html.Div([
    html.Div([
    html.P([
    "Notas sobre el resultado:",
    html.Br(),
    "(1) El estimado se obtiene a partir de un modelo de aprendizaje automático.",
    html.Br(),
    "(2) Puede dar resultados imprecisos para propiedades con un valor superior a US $ 130 000.",
    html.Br(),
    "(3) La recolección de los datos usados para entrenar el modelo se llevó a cabo en mayo del 2023.",
    html.Br(),
    """(4) Los datos fueron obtenidos de ofertas publicadas en internet, 
    las cuales incluyen la comisión de venta. Esto se verá reflejado en el 
    estimado final del precio.""",
    html.Br(),
    "(5) Para el año de construcción, los valores aceptados varían desde el año 2000 hasta el año 2025."
    ])
    ],style={
                'display': 'inline-block',
                'text-align': 'left',
                'margin-left': '20%',
                'width': '60%',
                'fontSize': 14}
    )]
)

layout = html.Div(children=[
    html.Br(),
    html.H2(children='Estimar el Precio de Propiedades',
            style={'textAlign': 'center'}),
    html.Div([
        html.Br(),
        text_intro_model,
        html.Br(),
        input,
        output,
        html.Br(),
        html.Br(),
        note_about_output,
        html.Br(),
        html.Br(),
        html.Br(),
        html.P('''Versión 1.0 | Última actualización de datos: mayo 2023.''', 
               style={'fontSize': 10,
                      'margin-left' : '10%'},)
    ])

])

@callback(Output('coordenadas', 'value'),
        Output('pin', 'position'),
        [Input('MAP_ID', 'click_lat_lng')])
def click_coord(coordinates):
    init_coordinates = [-17.77909, -63.16245]
    if coordinates is not None:
        return json.dumps(coordinates), coordinates
    else:
        return json.dumps(init_coordinates), init_coordinates
    
@callback(
    Output('output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [
        State('ambientes', 'value'),
        State('no_baños', 'value'),
        State('terreno_m2', 'value'),
        State('año_constr', 'value'),
        State('no_dormitorios', 'value'),
        State('area_constr_m2', 'value'),
        State('estacionamientos', 'value'),
        State('tipo_de_propiedad', 'value'),
        State('ciudad', 'value'),
        State('zona', 'value'),
        State('coordenadas', 'value')
    ]
)
def calculate_value(n_clicks, ambientes, no_baños, terreno_m2, año_constr, no_dormitorios,
                    area_constr_m2, estacionamientos, tipo_de_propiedad, ciudad,
                    zona, coordenadas):
    if n_clicks > 0:
        if None in [ambientes, no_baños, terreno_m2, año_constr, no_dormitorios, 
                    area_constr_m2, estacionamientos, tipo_de_propiedad, ciudad, 
                    zona, coordenadas]:
            return 'Por favor completar todos los campos'
        
        #convirtiendo el formato de las coordenadas
        values = json.loads(coordenadas)
        latitud = values[0]
        longitud = values[1]


        #prediciendo el resultado
        input_for_model = [ambientes, no_baños, terreno_m2, año_constr, no_dormitorios,
                    area_constr_m2, estacionamientos, latitud, longitud,
                   tipo_de_propiedad, ciudad, zona]
        prediction = predict(input_for_model)
        return f'El precio estimado es: US $ {prediction}'
    else:
        return ''