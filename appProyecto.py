import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import dcc  # dash core components
from dash import html # dash html components
import pandas as pd
import base64
from pgmpy.estimators import BayesianEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator

#Toca poner los datos en una base de datos de AWS
df = pd.read_csv("datosvf.csv", sep=";")
df.columns =['age', 'sex', 'cpt', 'pressure','chol','sugar','ecg','maxbpm','angina','oldpeak','slope','flourosopy','thal','diagnosis']


def estimar(df,radio1,radio2, radio3, dropdown1, dropdown2, dropdown3, dropdown4, dropdown5, dropdown6, dropdown7, dropdown8, dropdown9, dropdown10):

    Sex=9
    if radio1 == 'Hombre':
       Sex=1
    elif radio1 ==  'Mujer':
       Sex=0
       
    Exang=9
    if radio2 == 'Si':
       Exang=1
    elif radio2 == 'No':
       Exang=0
 
       
    Fbs=9
    if radio3 == 'Si':
       Fbs=1
    elif radio3 ==  'No':
       Fbs=0
    
    
    edad = 9
    if dropdown1 == "Entre 29 y 39 años":
        edad = 1
    elif dropdown1 == "Entre 40 y 54 años":
            edad = 2
    elif dropdown1 == "Entre 55 y 64 años":
        edad = 3
    elif dropdown1 == "Entre 65 y 79 años":
        edad = 4
    
    CP = 9
    if dropdown2 == 'Angina típica':
        CP = 1
    elif dropdown2 == 'Angina atípica':
        CP = 2
    elif dropdown2 == 'Dolor no anginoso':
        CP = 3
    elif dropdown2 == 'Asintomático':
        CP = 4
    
    Trestbps =9
    
    if dropdown3 == 'Entre 94 y 120':
        Trestbps = 1
    elif dropdown3 == 'Entre 121 y 129':
        Trestbps = 2
    elif dropdown3 == 'Entre 130 y 139':
        Trestbps = 3
    elif dropdown3 == 'Entre 140 y 180':
        Trestbps = 4
    elif dropdown3 == 'Entre 181 y 210':
        Trestbps = 5
        
    Chol =9
    
    if dropdown4 == 'Deseable':
        Chol = 1
    elif dropdown4 == 'Elevado':
        Chol = 2
    elif dropdown4 == 'Muy Elevado':
        Chol = 3
    
    ecg=9
    if dropdown5 == 'Normal':
        ecg = 0
    elif dropdown5 =='Anormalidad de la onda ST-T':
        ecg = 1
    elif dropdown5 =='Hipertrofia ventricular':
        ecg = 2
        
    maxbpm=9    
    if dropdown6 =='Entre 71 y 139':
        maxbpm=1
    elif dropdown6 =='Entre 140 y 169':
        maxbpm=2
    elif dropdown6 =='Entre 170 y 210':
        maxbpm=3
    
    slope = 9
    if dropdown7 =='Pendiente ascendente':
        slope=1
    elif dropdown7 =='Plano':
        slope=2
    elif dropdown7 =='Pendiente descendente':
        slope=3

    ca=9
    if dropdown8 =='1':
        ca=1
    elif dropdown8 =='2':
        ca=2
    elif dropdown8 =='3':
        ca=3
    
    Oldpeak=9
    if dropdown9 == 'Normal':
        Oldpeak=1
    elif dropdown9 == 'Lig. Elevada':
        Oldpeak=2
    elif dropdown9 == 'Mod. Elevada':
        Oldpeak=3
    elif dropdown9 == 'Alt. Elevada':
        Oldpeak=4
   
    
    Thal=9
    if dropdown10 == 'Normal':
        Thal=3
    elif dropdown10 == 'Defecto Fijo':
        Thal=6
    elif dropdown10 == 'Defecto Reversible':
        Thal=6
   
    mod_fit = BayesianNetwork([("sugar","chol"),
                                ("sugar","angina"),
                                ("sugar","pressure"),
                                ("angina","diagnosis"),
                                ("diagnosis","flourosopy"),
                                ("diagnosis","ecg"),
                                ("diagnosis","cpt"),
                                ("ecg","slope"),
                                ("ecg","oldpeak"),
                                ("sex","pressure"),
                                ("age","pressure"),
                                ("age","maxbpm"),
                                ("thal","maxbpm"),
                                ("maxbpm","diagnosis")])
    #En caso de querer usar con MaximumLikelihoodEstimator use el codigo de abajo y quite el otro mod_fit. OJO, usar el estimador de MV algunas estimaciones seran muy extremas
    #y daran desultados nan
    #mod_fit.fit(data = df , estimator = MaximumLikelihoodEstimator)
    
    mod_fit.fit(data=df , estimator = BayesianEstimator)
    #estimacion Bayesiana
    
    
    inferencia = VariableElimination(mod_fit)
    evidencia = {}
    if Sex !=9: 
        evidencia["sex"]= Sex
    if Exang !=9: 
        evidencia["angina"]= Exang
    if edad !=9: 
        evidencia["age"]= edad
    if Fbs !=9: 
        evidencia["sugar"]= Fbs
    if CP !=9: 
        evidencia["cpt"]= CP
    if Trestbps !=9: 
        evidencia["pressure"]= Trestbps
    if Chol !=9: 
        evidencia["chol"]= Chol
    if ecg !=9: 
        evidencia["ecg"]= ecg
    if maxbpm !=9: 
        evidencia["maxbpm"]= maxbpm
    if slope !=9: 
        evidencia["slope"]= slope
    if ca !=9: 
        evidencia["flourosopy"]= ca
    if Oldpeak !=9: 
        evidencia["oldpeak"]= Oldpeak
    if Thal !=9: 
        evidencia["thal"]= Thal
    resultado = inferencia.query(['diagnosis'],evidence=evidencia)
    return resultado



#http://127.0.0.1:8050/ 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


#############################################################################################
#Creación de las visualizaciones
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
datos = pd.read_csv("Datos_Discretizados.csv")
datos.head()
"1. Exploración de los datos"
#Graficos de pie
#Género
fig, ax = plt.subplots()
etiquetas = ["Mujeres","Hombres"]
valores = [datos.loc[(datos['sex'] == 0)].shape[0],(datos["sex"]==1).sum()]
colores=["#D7F47C", "#81E2DF"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Sexo de la muestra", fontsize = 18)
fig.subplots_adjust(top=0.9,bottom=0.01,right=0.9)
plt.savefig('Exploracion1.png')

#Age   
fig, ax = plt.subplots()
etiquetas = ["Joven Adulto","Adultos","Adultos Mayores","Tercera Edad"]
valores = [(datos["age"]==1).sum(),(datos["age"]==2).sum(),(datos["age"]==3).sum(),(datos["age"]==4).sum()]
colores=["#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Edad de la muestra", fontsize = 18)
fig.subplots_adjust(top=0.9,bottom=0.01,left=0.008)
plt.savefig('Exploracion2.png')

#"Trestbps"
fig, ax = plt.subplots()
etiquetas = ["Presión arterial normal","Prehipertensión","Hipertensión E1","Hipertensión E2","Crisis Hipertensiva"]
valores = [(datos["pressure"]==1).sum(),(datos["pressure"]==2).sum(),(datos["pressure"]==3).sum(),(datos["pressure"]==4).sum(),(datos["pressure"]==5).sum()]
colores=["#D7F47C", "#12B687","#5EC160","#90E0AE","#234F1E"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Presión arterial de la muestra", fontsize = 18)
fig.subplots_adjust(top=0.9,bottom=0.01,left=0.01)
plt.savefig('Exploracion3.png')

#"Chol"
fig, ax = plt.subplots()
etiquetas = ["Deseable","Elevado","Muy Elevado"]
valores = [(datos["chol"]==1).sum(),(datos["chol"]==2).sum(),(datos["chol"]==3).sum()]
colores=["#87CEFA", "#81E2DF","#C1E9FC"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Colesterol sérico de la muestra", fontsize = 18)
fig.subplots_adjust(top=0.9,bottom=0.01,left=0.008)
plt.savefig('Exploracion4.png')

#"Thalach"
fig, ax = plt.subplots()
etiquetas = ["Reposo","Ej. Aerobico","Ej. Intenso"]
valores = [(datos["maxbpm"]==1).sum(),(datos["maxbpm"]==2).sum(),(datos["maxbpm"]==3).sum()]
colores=["#D7F47C", "#12B687","#5EC160"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Frecuencia cardiaca máxima de la muestra", fontsize = 18)
fig.subplots_adjust(top=0.9,bottom=0.01,left=0.01)
plt.savefig('Exploracion5.png')

#"Oldpeak"
fig, ax = plt.subplots()
etiquetas = ["Normal","Ligeramente Elevado","Moderadamente Elevado","Altamente Elevado"]
valores = [(datos["oldpeak"]==1).sum(),(datos["oldpeak"]==2).sum(),(datos["oldpeak"]==3).sum(),(datos["oldpeak"]==4).sum()]
colores=[ "#8AD6F4","#3EAEF4","#81E2DF","#CFEFFC"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Depresión del ST de la muestra", fontsize = 18)
fig.subplots_adjust(top=0.9,bottom=0.01,left=0.008)
plt.savefig('Exploracion6.png')

#Genero por edad
#Mujeres
M_Jovenes = datos.loc[(datos['age'] == 1) & (datos['sex'] == 0)].shape[0]
M_Adultos = datos.loc[(datos['age'] == 2) & (datos['sex'] == 0)].shape[0]
M_AdultosMay = datos.loc[(datos['age'] == 3) & (datos['sex'] == 0)].shape[0]
M_Tercera = datos.loc[(datos['age'] == 4) & (datos['sex'] == 0)].shape[0]

y = [M_Jovenes, M_Adultos,  M_AdultosMay,M_Tercera]
x = ['1','2','3','4']

# crear gráfica de barras
fig, ax = plt.subplots()
fig.subplots_adjust(top=1)

#ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE","#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos")
ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE"],label="Adultos")
ax.bar(x, y, color=["#12B687", "#12B687","#5EC160","#90E0AE"],label="Adultos Mayores")
ax.bar(x, y, color=["#5EC160", "#12B687","#5EC160","#90E0AE"],label="Tercera Edad")
ax.bar(x, y, color=["#90E0AE", "#12B687","#5EC160","#90E0AE"],label="Jovenes")
ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE"])

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])

for i, v in enumerate(y):
    plt.text(i, v + 0.8, str(v), color='black', ha='center')

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=4)
ax.set_title('Edad de las mujeres de la muestra')
#ax.set_xticks(x)
#ax.set_xticklabels(['                         Enfermos','','','','                         Sanos','','',''])
fig.subplots_adjust(top=0.9,bottom=0.2)
plt.savefig('Exploracion7.png')


#Hombres
H_Jovenes = datos.loc[(datos['age'] == 1) & (datos['sex'] == 1)].shape[0]
H_Adultos = datos.loc[(datos['age'] == 2) & (datos['sex'] == 1)].shape[0]
H_AdultosMay = datos.loc[(datos['age'] == 3) & (datos['sex'] == 1)].shape[0]
H_Tercera = datos.loc[(datos['age'] == 4) & (datos['sex'] == 1)].shape[0]

y = [H_Jovenes,H_Adultos,H_AdultosMay,H_Tercera]
x = ['1','2','3','4']

# crear gráfica de barras
fig, ax = plt.subplots()
fig.subplots_adjust(top=1)

#ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE","#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos")
ax.bar(x, y, color=["#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos")
ax.bar(x, y, color=["#8AD6F4", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos Mayores")
ax.bar(x, y, color=["#3EAEF4", "#8AD6F4","#3EAEF4","#81E2DF"],label="Tercera Edad")
ax.bar(x, y, color=["#81E2DF", "#8AD6F4","#3EAEF4","#81E2DF"],label="Jovenes")
ax.bar(x, y, color=["#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"])

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])

for i, v in enumerate(y):
    plt.text(i, v + .8, str(v), color='black', ha='center')

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=4)
ax.set_title('Edad de las mujeres de la muestra')
#ax.set_xticks(x)
#ax.set_xticklabels(['                         Enfermos','','','','                         Sanos','','',''])
fig.subplots_adjust(top=0.9,bottom=0.2)
plt.savefig('Exploracion8.png')
###########################################################################
import seaborn as sns
Correlacion= datos.corr()
fig, ax = plt.subplots(figsize=(10,10))
matriz_redondeada=np.round(Correlacion, decimals=2)
sns.heatmap(matriz_redondeada, annot=True, cmap='coolwarm', linewidths=1, ax=ax)

# guardar la figura en una imagen
fig.savefig("tabla_de_correlacion.png")

###################################################################################################
"3. Quienes son más propensos a tener la enfermedad"
# Diagramas de los Enfermos

"--------------------------PRIMER GRÁFICO: SEXO-------------------------------"
Mujeres_enfermas = datos.loc[(datos['sex'] == 0) & (datos['diagnosis'] == 1)].shape[0]
Hombres_enfermos = datos.loc[(datos['sex'] == 1) & (datos['diagnosis'] == 1)].shape[0]

Mujeres_sanas = datos.loc[(datos['sex'] == 0) & (datos['diagnosis'] == 0)].shape[0]
Hombres_sanos = datos.loc[(datos['sex'] == 1) & (datos['diagnosis'] == 0)].shape[0]

# crear lista con datos y nombres de cada barra
y = [Hombres_enfermos, Mujeres_enfermas,  Hombres_sanos,Mujeres_sanas]
x = ['Enfermos', 'Enfermas','Sanos', 'Sanas']

# crear gráfica de barras
fig, ax = plt.subplots()
fig.subplots_adjust(top=1)
ax.bar(x, y, color=["#FC91B1","#5EBDF8","#DEF2FE", "#FEECF2"],label="Mujeres")
ax.bar(x, y, color=["#5EBDF8","#FC91B1","#DEF2FE", "#FEECF2"],label="Hombres")

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])

for i, v in enumerate(y):
    plt.text(i, v + 3, str(v), color='black', ha='center')

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=2)
ax.set_title('Cantidad de personas enfermas y sanas por sexo')
ax.set_xticks(x)
ax.set_xticklabels(['                         Enfermos','','                         Sanos',''])

fig.subplots_adjust(top=0.9,bottom=0.2)
plt.savefig('Propension1.png')

"--------------------------SEGUNDO GRÁFICO: EDAD-------------------------------"
Jovenes_enfermas = datos.loc[(datos['age'] == 1) & (datos['diagnosis'] == 1)].shape[0]
Adultos_enfermos = datos.loc[(datos['age'] == 2) & (datos['diagnosis'] == 1)].shape[0]
AdultosMay_enfermos = datos.loc[(datos['age'] == 3) & (datos['diagnosis'] == 1)].shape[0]
Tercera_enfermos = datos.loc[(datos['age'] == 4) & (datos['diagnosis'] == 1)].shape[0]


Jovenes_sanos = datos.loc[(datos['age'] == 1) & (datos['diagnosis'] == 0)].shape[0]
Adultos_sanos = datos.loc[(datos['age'] == 2) & (datos['diagnosis'] == 0)].shape[0]
AdultosMay_sanos = datos.loc[(datos['age'] == 3) & (datos['diagnosis'] == 0)].shape[0]
Tercera_sanos = datos.loc[(datos['age'] == 4) & (datos['diagnosis'] == 0)].shape[0]

# crear lista con datos y nombres de cada barra
y = [Jovenes_enfermas, Adultos_enfermos,  AdultosMay_enfermos,Tercera_enfermos,
     Jovenes_sanos,Adultos_sanos,AdultosMay_sanos,Tercera_sanos]
x = ['1','2','3','4','5','6','7','8']

# crear gráfica de barras
fig, ax = plt.subplots()
fig.subplots_adjust(top=1)

ax.bar(x, y, color=["#92D050","#97F836","#00B050", "#385723","#E9FEB4","#EEF8E4","#CDE9DC","#D8EACC"],label="Adultos")
ax.bar(x, y, color=["#00B050","#97F836","#92D050", "#385723","#E9FEB4","#EEF8E4","#CDE9DC","#D8EACC"],label="Adultos Mayores")
ax.bar(x, y, color=["#385723","#97F836","#92D050","#00B050","#E9FEB4","#EEF8E4","#CDE9DC","#D8EACC"],label="Tercera Edad")
ax.bar(x, y, color=["#97F836","#92D050","#00B050", "#385723","#E9FEB4","#EEF8E4","#CDE9DC","#D8EACC"],label="Jovenes")

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])

for i, v in enumerate(y):
    plt.text(i, v + 3, str(v), color='black', ha='center')

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=4)
ax.set_title('Cantidad de personas enfermas y sanas por edad')
ax.set_xticks(x)
ax.set_xticklabels(['                         Enfermos','','','','                         Sanos','','',''])
fig.subplots_adjust(top=0.9,bottom=0.2)
plt.savefig('Propension2.png')
########################################################################################################################







#Cargar una imagen desde el computador
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

Exploracion3='Exploracion3.png'
encoded_image = base64.b64encode(open(Exploracion3, 'rb').read())
exp3 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion4='Exploracion4.png'
encoded_image = base64.b64encode(open(Exploracion4, 'rb').read())
exp4 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion5='Exploracion5.png'
encoded_image = base64.b64encode(open(Exploracion5, 'rb').read())
exp5 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion6='Exploracion6.png'
encoded_image = base64.b64encode(open(Exploracion6, 'rb').read())
exp6 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
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
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})


#########################################################333######################################
Propension1='Propension1.png'
encoded_image = base64.b64encode(open(Propension1, 'rb').read())
Prop1 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Propension2='Propension2.png'
encoded_image = base64.b64encode(open(Propension2, 'rb').read())
Prop2 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})






tab1=dcc.Tab(label='Análisis de la muestra',children=[
    html.Div('El contenido de esta pesataña hace referencia a.....'),
    html.Br(),
    html.Div(exp1),
    html.Div(exp2),
    html.Div(exp3),
    html.Div(exp4),
    html.Div(exp5),
    html.Div(exp6),
    html.Div(exp7),
    html.Div(exp8)
    
])

tab2=dcc.Tab(label='Propensión a tener la enfermedad',children=[
    html.Div('El contenido de esta pesataña hace referencia a.....'),
    html.Br(),
    html.Div(Prop1),
    html.Div(Prop2)
])

tab3=dcc.Tab(label='Información estadística',children=[
    html.Div('El contenido de esta pesataña hace referencia a.....'),
    html.Br(),
    html.Div(Estad1)
])
pestanas = [tab1, tab2, tab3]
tabs = dcc.Tabs(children=pestanas)








app.layout = html.Div([
    html.Div(children=[image]),
    tabs,
    html.H6(''' Para hacer uso del sistema de datos es necesario realizar lo siguiente:'''),
    html.Div(" 1. Asegurate de ingresar los datos correctamente en las casillas correspondientes."),
    html.Div(''' 2. En caso de que no poseas el dato puedes indicar la opción "No aplica". Sin embargo, debes ingresar al menos información del género y la edad del paciente para poder generar el resultado. Ten en cuenta que entre más información indiques, más acertada será la valoración.'''),
    html.Div(" 3. Cuando ingreses todos los datos, por favor da click en el botón 'Continuar' en cual se encuentra debajo de los datos requeridos. "),
    html.Div(" 4. Luego, fijese de haber completado todos los datos y que el sistema no haya arrojado una alerta, de ser asi, la encontrará de color rojo debajo del boyon 'Continuar'"),
    
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
                options=[{'label': i, 'value': i} for i in ['Angina típica','Angina atípica','Dolor no anginoso','Asintomático','No aplica']]),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
    
    
     html.Div(["Presión arterial en reposo (mm/Hg)",
                dcc.Dropdown(
                id='dropdown-3',
                options=[{'label': i, 'value': i} for i in ['Entre 94 y 120','Entre 121 y 129','Entre 130 y 139', 'Entre 140 y 180','Entre 181 y 210','No aplica']]),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '25%', 'float': 'left', 'display': 'inline-block'}),
     

     html.Div(["Colesterol sérico en mg/dl",
                dcc.Dropdown(
                id='dropdown-4',
                options=[{'label': i, 'value': i} for i in ['Deseable','Elevado','Muy Elevado','No aplica']]),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
          
     
     html.Div(["Resultados electrocardiográficos en reposo",
                dcc.Dropdown(
                id='dropdown-5',
                options=[{'label': i, 'value': i} for i in ['Normal','Anormalidad de la onda ST-T','Hipertrofia ventricular','No aplica']]),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
     
     
    html.Div(["Frecuencia cardiaca máxima alcanzada",
                dcc.Dropdown(
                id='dropdown-6',
                options=[{'label': i, 'value': i} for i in ['Entre 71 y 139','Entre 140 y 169','Entre 170 y 210','No aplica']]),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   

    html.Div(["La pendiente (Slot )del segmento ST de ejercicio máximo",
                dcc.Dropdown(
                id='dropdown-7',
                options=[{'label': i, 'value': i} for i in ['Pendiente ascendente','Plano','Pendiente descendente','No aplica']]),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '25%', 'float': 'left', 'display': 'inline-block'}),

    
    html.Div(["Número de vasos mayores coloreados por fluoroscopia",
                dcc.Dropdown(
                id='dropdown-8',
                options=[{'label': i, 'value': i} for i in ['1','2','3','No aplica']]),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),

    
    html.Div(["Descenso del segmento ST",
                dcc.Dropdown(
                id='dropdown-9',
                options=[{'label': i, 'value': i} for i in ['Normal','Lig. Elevada','Mod. Elevada','Alt. Elevada','No aplica']]),          
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
    
    
     html.Div(["¿Qué tipo de Talasemia posee?",
                dcc.Dropdown(
                id='dropdown-10',
                options=[{'label': i, 'value': i} for i in ['Normal','Defecto Fijo','Defecto Reversible','No aplica']]),          
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
                options=[{'label': i, 'value': i} for i in ['Si', 'No','No aplica']],
                labelStyle={'display': 'inline-block'}), 
                html.Br()],
                style={'display': 'inline-block','width': '22%'}
                ),
    
    html.Div(["¿La glucemia en ayunas es menor a 120 mg/dl?",
                dcc.RadioItems(
                id='Radio-3',
                options=[{'label': i, 'value': i} for i in ['Si', 'No','No aplica']],
                labelStyle={'display': 'inline-block'}), 
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%'}
                ),
    html.Br(),
    html.Button('Continuar', id='button', n_clicks=0),
    html.Div(id='alert-container'),
    html.Div(id='output'),
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
    
    if n_clicks > 0 and radio1 is None or n_clicks > 0 and dropdown1 == "Seleccione" or n_clicks > 0 and dropdown1 is None:
        if radio1 is None:
            return html.H5(html.Div([html.Div('Por favor, asegurate de haber ingresado el genero del paciente',style={'color': 'red'})
                                    ]))
        elif dropdown1 == "Seleccione" or dropdown1 is None:
            return html.H5(html.Div([html.Div('Por favor, asegurate de haber ingresado la edad del paciente', style={'color': 'red'})
                                     ]))
    #Revisar el resto de casillas Radio
    if n_clicks > 0 and radio2 is None or n_clicks > 0 and radio3 is None:
        return html.Div(html.H5('Por favor, asegurate de haber ingresado todas las casillas de selección tipo "Radio".Recuerda que en caso de no tener la información existe la opción no aplica', style={'color': 'red'})
                                 )
    
    #Revisar el resto de casillas Dropdown
    if n_clicks > 0 and dropdown2 == "Seleccione" or n_clicks > 0 and dropdown2 is None or n_clicks > 0 and dropdown3 == "Seleccione" or n_clicks > 0 and dropdown3 is None or n_clicks > 0 and dropdown4 == "Seleccione" or n_clicks > 0 and dropdown4 is None or n_clicks > 0 and dropdown5 == "Seleccione" or n_clicks > 0 and dropdown5 is None or n_clicks > 0 and dropdown6 == "Seleccione" or n_clicks > 0 and dropdown6 is None or n_clicks > 0 and dropdown7 == "Seleccione" or n_clicks > 0 and dropdown7 is None or n_clicks > 0 and dropdown8 == "Seleccione" or n_clicks > 0 and dropdown8 is None or n_clicks > 0 and dropdown9 == "Seleccione" or n_clicks > 0 and dropdown9 is None or n_clicks > 0 and dropdown10 == "Seleccione" or n_clicks > 0 and dropdown10 is None:
        return html.Div(html.H5('Por favor, asegurate de haber ingresado todas las casillas de selección tipo "Menú Desplegable". Recuerda que en caso de no tener la información existe la opción no aplica', style={'color': 'red'})
                                 )
        
    
    
    
    elif n_clicks > 0 and radio1 is not None and radio2 is not None and radio3 is not None and dropdown1 != "Seleccione" and dropdown2 != "Seleccione" and dropdown3 != "Seleccione" and dropdown4 != "Seleccione" and dropdown5 != "Seleccione" and dropdown6 != "Seleccione" and dropdown7 != "Seleccione" and dropdown8 != "Seleccione" and dropdown9 != "Seleccione" and dropdown10 != "Seleccione" :   
        return (html.Div(html.H5(["A Continuación se mostrará la información ingresada:", 
                        html.Br()],style={'color': 'green'})),
               html.Div([f"·    Rango de edad del paciente -----------------------------------------> {dropdown1}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    Tipo de dolor torácico --------------------------------------------------> {dropdown2}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    Presión arterial en reposo (mm/Hg) --------------------------------> {dropdown3}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    Colesterol sérico en mg/dl --------------------------------------------> {dropdown4}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    Resultados electrocardiográficos en reposo ----------------------> {dropdown5}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    Frecuencia cardiaca máxima alcanzada --------------------------> {dropdown6}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    La pendiente (Slot )del segmento ST de ejercicio máximo ----> {dropdown7}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    Número de vasos mayores coloreados por flouroscopia ------> {dropdown8}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    Descenso del segmento ST -------------------------------------------> {dropdown9}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    ¿Qué tipo de Talasemia posee? --------------------------------------> {dropdown10}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    Indique el sexo del paciente -------------------------------------------> {radio1}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    ¿Angina inducida por el ejercicio? ------------------------------------> {radio2}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"·    ¿La glucemia en ayunas es menor a 120 mg/dl? -----------------> {radio3}", 
                        html.Br()],style={'color': 'black'}),
               
               html.Div([f"· En ese sentido, tu resultado es: siendo 0 la probabilidad de no tener enfermedades cardiacas   {estimar(df, radio1,radio2, radio3, dropdown1, dropdown2, dropdown3, dropdown4, dropdown5, dropdown6, dropdown7, dropdown8, dropdown9, dropdown10)}", 
                        html.Br()],style={'color': 'blue'})

               )






if __name__ == '__main__':
    app.run_server(debug=True)
    
