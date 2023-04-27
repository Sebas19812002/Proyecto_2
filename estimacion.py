from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.sampling import BayesianModelSampling
from pgmpy.estimators import BayesianEstimator
import pandas as pd

# El archivo esta delimitado por ;

df = pd.read_csv("Datos_Discretizados.csv")
print(df.head(5))


#Parametrización del modelo
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
#En caso de querer usar con estimador bayesiano
mod_fit.fit(data=df , estimator = BayesianEstimator)

print(mod_fit.nodes())
#Estimador MaximumLikelihoodEstimator
mod_fit.fit(data = df , estimator = MaximumLikelihoodEstimator)


breakpoint()




























inferencia = VariableElimination(mod_fit)
Ejemplo1 = inferencia.query(['diagnosis'],evidence={"sex":1, "angina":1, "age": 2 })
print ("Ejemplo 1", Ejemplo1)
#Creación de una funcion que reciba los parámetros del dash y los transforme en la categorización de las variables

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
    #En caso de querer usar con estimador bayesiano
    #mod_fit.fit(data=df , estimator = BayesianEstimator)
    #estimacion Bayesiana
    
    mod_fit.fit(data = df , estimator = MaximumLikelihoodEstimator)
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
ejemplo = estimar(df, 'Hombre', 'Si', 'Si', "Entre 29 y 39 años", 'Angina típica', 'Entre 94 y 120', 'Deseable', 'No aplica', 'Entre 170 y 210', 'No aplica', '1', 'Normal', 'Normal')
print("")
print ("Ejemplo 2", ejemplo)












