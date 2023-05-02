import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import base64
import Funciones as F

#http://127.0.0.1:8050/ 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server




#-----------------connect to DB----------------------#
datos=F.Conexion_DB_()
#------------------Graficas--------------------------------#
F.crear_visualizaciones(datos)
#------------Cargar una imagen desde el computador--------------#

imagen_bienvenida='Bienvenidos.png'
encoded_image = base64.b64encode(open(imagen_bienvenida, 'rb').read())
image = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})

imagen_Final='Final.png'
encoded_image = base64.b64encode(open(imagen_Final, 'rb').read())
fina = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), 
    style={'display': 'block','margin-left': 'auto', 'margin-right': 'auto'})

Edad =["Entre 29 y 39 años","Entre 40 y 54 años","Entre 55 y 64 años","Entre 65 y 79 años"]



#################################################################################################
#Imagenes de exploracion
Exploracion1='Exploracion1.png'
encoded_image = base64.b64encode(open(Exploracion1, 'rb').read())
exp1 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion2='Exploracion2.png'
encoded_image = base64.b64encode(open(Exploracion2, 'rb').read())
exp2 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion4='Exploracion4.png'
encoded_image = base64.b64encode(open(Exploracion4, 'rb').read())
exp4 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion5='Exploracion5.png'
encoded_image = base64.b64encode(open(Exploracion5, 'rb').read())
exp5 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion7='Exploracion7.png'
encoded_image = base64.b64encode(open(Exploracion7, 'rb').read())
exp7 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion8='Exploracion8.png'
encoded_image = base64.b64encode(open(Exploracion8, 'rb').read())
exp8 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})
######################################################################################################

Estadistica1='tabla_de_correlacion.png'
encoded_image = base64.b64encode(open(Estadistica1, 'rb').read())
Estad1 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '90%', 'float': 'left'})


#########################################################333######################################
Propension1='Propension1.png'
encoded_image = base64.b64encode(open(Propension1, 'rb').read())
Prop1 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Propension2='Propension2.png'
encoded_image = base64.b64encode(open(Propension2, 'rb').read())
Prop2 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Propension3='Propension3.png'
encoded_image = base64.b64encode(open(Propension3, 'rb').read())
Prop3 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Propension4='Propension4.png'
encoded_image = base64.b64encode(open(Propension4, 'rb').read())
Prop4 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Propension5='Propension5.png'
encoded_image = base64.b64encode(open(Propension5, 'rb').read())
Prop5 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Propension6='Propension6.png'
encoded_image = base64.b64encode(open(Propension6, 'rb').read())
Prop6 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})






tab1=dcc.Tab(label='Análisis de la muestra',children=[
    html.Div('En esta pestaña se encuentra información sobre la distribucón de la muestra de datos'),
    html.Br(),
    html.Div(exp1),
    html.Div(exp5),
    html.Div(exp4),
    html.Br(),
    html.Div(exp2),
    html.Div(exp7),
    html.Div(exp8)
    
])

tab2=dcc.Tab(label='Propensión y comportamiento',children=[
    html.Div('En esta pestaña se encuentra información relacionada a los grupos de personas que son más propensos a tener la enfermedad. Asi mismo, encontrará gráficas con datos acerca de cada uno de los sintomas'),
    html.Br(),
    html.Div('Nota: Para leer las gráficas de líneas, es necesario que tenga en cuenta que el primer punto de cada segmento corresponde a los jovenes, el segundo a los Adultos, el tercero a los Adultos Mayores y finalmente el cuarto a los aductos de Tercera Edad. '),
    html.Br(),
    html.Div(Prop1),
    html.Div(Prop2),
    html.Div(Prop5),
    html.Br(),
    html.Div(Prop4),
    html.Div(Prop3),
    html.Div(Prop6)
])

tab3=dcc.Tab(label='Información estadística',children=[
    html.Div('En esta pesataña usted encontrara una tabla de correlación que le pueden ayudar a comprender mejor los datos y sus relaciones.'),
    html.Br(),
    html.Div(Estad1)
])
pestanas = [tab1, tab2, tab3]
tabs = dcc.Tabs(children=pestanas)


app.layout = html.Div([
    html.Div(children=[image]),
    
    html.H6(''' Para hacer uso del sistema de datos es necesario realizar lo siguiente:'''),
    html.Div(" 1. Asegurate de ingresar los datos correctamente en las casillas correspondientes, en caso de que no poseas el dato puedes dejar la casilla en blanco."),
    html.Div(''' 2. Debes ingresar al menos información del género y la edad del paciente para poder generar el resultado. Ten en cuenta que entre más información indiques, más acertada será la valoración.'''),
    html.Div(" 3. Cuando ingreses todos los datos, por favor da click en el botón 'Continuar' en cual se encuentra debajo de los datos requeridos. "),
    html.Div(" 4. Luego, fijate de haber completado todos los datos y que el sistema no haya arrojado una alerta, de ser asi, la encontrarás de color rojo debajo del boyon 'Continuar'"),
    
    html.Br(),
    
    html.Div(["Rango de edad del paciente: ",
              dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': i, 'value': i} for i in Edad],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
    
    
    html.Div(["Tipo de dolor torácico",
            dcc.Dropdown(
                id='dropdown-2',
                options=[{'label': i, 'value': i} for i in ['Angina típica','Angina atípica','Dolor no anginoso','Asintomático']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
    
    
     html.Div(["Presión arterial en reposo (mm/Hg)",
                dcc.Dropdown(
                id='dropdown-3',
                options=[{'label': i, 'value': i} for i in ['Entre 94 y 120','Entre 121 y 129','Entre 130 y 139', 'Entre 140 y 180','Entre 181 y 210']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '25%', 'float': 'left', 'display': 'inline-block'}),
     

     html.Div(["Colesterol sérico en mg/dl",
                dcc.Dropdown(
                id='dropdown-4',
                options=[{'label': i, 'value': i} for i in ['Deseable','Elevado','Muy Elevado']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
          
     
     html.Div(["Resultados electrocardiográficos en reposo",
                dcc.Dropdown(
                id='dropdown-5',
                options=[{'label': i, 'value': i} for i in ['Normal','Anormalidad de la onda ST-T','Hipertrofia ventricular']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
     
     
    html.Div(["Frecuencia cardiaca máxima alcanzada",
                dcc.Dropdown(
                id='dropdown-6',
                options=[{'label': i, 'value': i} for i in ['Entre 71 y 139','Entre 140 y 169','Entre 170 y 210']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   

    html.Div(["La pendiente (Slot )del segmento ST de ejercicio máximo",
                dcc.Dropdown(
                id='dropdown-7',
                options=[{'label': i, 'value': i} for i in ['Pendiente ascendente','Plano','Pendiente descendente']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '25%', 'float': 'left', 'display': 'inline-block'}),

    
    html.Div(["Número de vasos mayores coloreados por fluoroscopia",
                dcc.Dropdown(
                id='dropdown-8',
                options=[{'label': i, 'value': i} for i in ['1','2','3']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),

    
    html.Div(["Descenso del segmento ST",
                dcc.Dropdown(
                id='dropdown-9',
                options=[{'label': i, 'value': i} for i in ['Normal','Lig. Elevada','Mod. Elevada','Alt. Elevada']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
    
    
     html.Div(["¿Qué tipo de Talasemia posee?",
                dcc.Dropdown(
                id='dropdown-10',
                options=[{'label': i, 'value': i} for i in ['Normal','Defecto Fijo','Defecto Reversible']],
                value='No aplica'),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
            
    
  
    html.Br(),
  
    html.Div(["Indique el sexo del paciente: ",
                dcc.RadioItems(
                id='Radio-1',
                options=[{'label': i, 'value': i} for i in ['Hombre', 'Mujer']],
                labelStyle={'display': 'inline-block'}), 
                html.Br()],
                style={'display': 'inline-block','width': '22%'}
                ),
    

    html.Div(["¿Angina inducida por el ejercicio?",
                dcc.RadioItems(
                id='Radio-2',
                options=[{'label': i, 'value': i} for i in ['Si', 'No']],
                value='No aplica',
                labelStyle={'display': 'inline-block'}), 
                html.Br()],
                style={'display': 'inline-block','width': '22%'}
                ),
    
    html.Div(["¿La glucemia en ayunas es menor a 120 mg/dl?",
                dcc.RadioItems(
                id='Radio-3',
                options=[{'label': i, 'value': i} for i in ['Si', 'No']],
                value='No aplica',
                labelStyle={'display': 'inline-block'}), 
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%'}
                ),
    html.Br(),
    html.Br(),
    
    
    
    html.Button('Continuar', id='button', n_clicks=0,style={'marginLeft': '40%'}),
    html.Button('Vaciar todo', id='reset-button',n_clicks=0,style={'marginLeft': 'auto', 'marginRight': 'auto'}),
    html.Div(id='alert-container'),
    html.Div(id='output'),
    html.Br(),
    html.Br(),   
    
    html.H6(''' Visualizaciones:'''),
    html.Div("A continuación, tienes a tu disposición algunas visualizaciones que pueden ser de tu interés."),
    html.Br(),
    tabs,
    html.Br(),
    html.Br(),   
    
    html.Div(children=[fina])
    ])


@app.callback(
    Output('output', 'children'),
    Input('button', 'n_clicks'),
    State('Radio-1', 'value'),
    State('Radio-2', 'value'),
    State('Radio-3', 'value'),
    State('dropdown-1', 'value'),
    State('dropdown-2', 'value'),
    State('dropdown-3', 'value'),
    State('dropdown-4', 'value'),
    State('dropdown-5', 'value'),
    State('dropdown-6', 'value'),
    State('dropdown-7', 'value'),
    State('dropdown-8', 'value'),
    State('dropdown-9', 'value'),
    State('dropdown-10', 'value')
    )
    
def validate_selection (n_clicks, radio1,radio2, radio3, dropdown1, dropdown2, dropdown3, dropdown4, dropdown5, dropdown6, dropdown7, dropdown8, dropdown9, dropdown10):
    
    if n_clicks > 0 and (radio1 is None or dropdown1 == "Seleccione" or dropdown1 is None):
        if radio1 is None:
            return html.H5(html.Div([html.Div('Por favor, asegurate de haber ingresado el genero del paciente',style={'color': 'red'})
                                    ]))
        elif dropdown1 == "Seleccione" or dropdown1 is None:
            return html.H5(html.Div([html.Div('Por favor, asegurate de haber ingresado la edad del paciente', style={'color': 'red'})
                                     ]))

    
    elif n_clicks > 0 and radio1 is not None and radio2 is not None and radio3 is not None and dropdown1 != "Seleccione" and dropdown2 != "Seleccione" and dropdown3 != "Seleccione" and dropdown4 != "Seleccione" and dropdown5 != "Seleccione" and dropdown6 != "Seleccione" and dropdown7 != "Seleccione" and dropdown8 != "Seleccione" and dropdown9 != "Seleccione" and dropdown10 != "Seleccione" :   
        
        resultado=F.estimar(radio1,radio2, radio3, dropdown1, dropdown2, dropdown3, dropdown4, dropdown5, dropdown6, dropdown7, dropdown8, dropdown9, dropdown10)
        tabla2=html.Table([
                html.Tr([
                    # html.Td(''),
                    html.Th('Probabilidad de NO tener la enfermedad'),
                    html.Th('Probabilidad de SI tener la enfermedad'),
                    
                ]),
                

                html.Tr([
                    # html.Td('En ese sentido, tu resultado es:'),
                    html.Td(f"{round(resultado[0],3)*100}%", style={'text-align': 'center'}),
                    html.Td(f"{round(resultado[1],3)*100}%", style={'text-align': 'center'})
                ])],

                style={'marginLeft': 'auto', 'marginRight': 'auto'})
        
        tabla1=html.Table([
                html.Tr([
                    html.Td('Rango de edad del paciente'),
                    html.Td(dropdown1)
                ]),
                html.Tr([
                    html.Td('Tipo de dolor torácico'),
                    html.Td(dropdown2)
                ]),
                html.Tr([
                    html.Td('Presión arterial en reposo (mm/Hg)'),
                    html.Td(dropdown3)
                ]),
                html.Tr([
                    html.Td('Colesterol sérico en mg/dl'),
                    html.Td(dropdown4)
                ]),
                html.Tr([
                    html.Td('Resultados electrocardiográficos en reposo'),
                    html.Td(dropdown5)
                ]),
                html.Tr([
                    html.Td('Frecuencia cardiaca máxima alcanzada'),
                    html.Td(dropdown6)
                ]),
                html.Tr([
                    html.Td('La pendiente (Slot) del segmento ST de ejercicio máximo'),
                    html.Td(dropdown7)
                ]),
                html.Tr([
                    html.Td('Número de vasos mayores coloreados por flouroscopia'),
                    html.Td(dropdown8)
                ]),
                html.Tr([
                    html.Td('Descenso del segmento ST'),
                    html.Td(dropdown9)
                ]),
                html.Tr([
                    html.Td('¿Qué tipo de Talasemia posee?'),
                    html.Td(dropdown10)
                ]),
                html.Tr([
                    html.Td('Sexo del paciente'),
                    html.Td(radio1)
                ]),
                html.Tr([
                    html.Td('¿Angina inducida por el ejercicio?'),
                    html.Td(radio2)
                ]),
                html.Tr([
                    html.Td('¿La glucemia en ayunas es menor a 120 mg/dl?'),
                    html.Td(radio3)
                ])],
                style={'marginLeft': 'auto', 'marginRight': 'auto'})



        return (html.Div(html.H5(["A Continuación se mostrará la información ingresada:", 
                        html.Br()],style={'color': 'green'})),
               
                html.Br(),
               
                tabla1,
                html.Br(),
               
                html.Div(html.H5(["El diagnostico es:", 
                        html.Br()],style={'color': 'green'})),

                tabla2,
                html.Br(),
            
               )

@app.callback(
    Output('Radio-1', 'value'),
    Output('Radio-2', 'value'),
    Output('Radio-3', 'value'),
    Output('dropdown-1', 'value'),
    Output('dropdown-2', 'value'),
    Output('dropdown-3', 'value'),
    Output('dropdown-4', 'value'),
    Output('dropdown-5', 'value'),
    Output('dropdown-6', 'value'),
    Output('dropdown-7', 'value'),
    Output('dropdown-8', 'value'),
    Output('dropdown-9', 'value'),
    Output('dropdown-10', 'value'),
    Input('reset-button', 'n_clicks')
    )
def reset_btn(n_clicks):
    if n_clicks>0:
        return (None,'No aplica','No aplica',None,'No aplica','No aplica','No aplica','No aplica','No aplica','No aplica','No aplica','No aplica','No aplica')
    return dash.no_update



if __name__ == '__main__':
    app.run_server(debug=True)
    
