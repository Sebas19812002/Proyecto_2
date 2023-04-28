from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.readwrite import BIFReader
import pandas as pd

def Metricas (test_data, modelo ):
    filas=test_data.shape[0]
    inferencia = VariableElimination(modelo)    
    tabla = pd.DataFrame(columns=['VP', 'VN', 'FP', 'FN'], index=[0])
    vp=0
    vn=0
    fp=0
    fn=0
    for j in range(0,filas): 
        real=test_data.iloc[j]
        Evidencia={"age":0,"sex":0,"cpt":0,"pressure":0,"chol":0,"sugar":0,"ecg":0,"maxbpm":0,"angina":0,"oldpeak":0, "slope":0, "flourosopy":0,"thal":0}
        Evidencia["age"]=str(real[0])
        Evidencia["sex"]=str(real[1])
        Evidencia["cpt"]=str(real[2])
        Evidencia["pressure"]=str(real[3])
        Evidencia["chol"]=str(real[4])
        Evidencia["sugar"]=str(real[5])
        Evidencia["ecg"]=str(real[6])
        Evidencia["maxbpm"]=str(real[7])
        Evidencia["angina"]=str(real[8])
        Evidencia["oldpeak"]=str(real[9])
        Evidencia["slope"]=str(real[10])
        Evidencia["flourosopy"]=str(real[11])
        Evidencia["thal"]=str(real[12])
        resultado = inferencia.query(['diagnosis'], evidence=Evidencia).values
        
        Prediccion=1
        #Prob de no tener = 0
        if resultado[0]>=0.5 :
            Prediccion=0
        if Prediccion == real[13] and Prediccion==1  :
            vp+=1
        elif Prediccion == real[13] and Prediccion==0 :
            fp+=1
        elif Prediccion != real[13] and Prediccion==0 and real[13]==1 :
            fn+=1
        else:   
            vn+=1
    tabla.loc[0] = [vp,vn, fp, fn]    
    return(tabla)
#Datos de entreno
df= pd.read_csv("Datos_test.csv")
print(df.head(5))

modelo = BIFReader("Modelo.bif").get_model()
modelo.check_model()
Resultados=Metricas(df, modelo)
print(Resultados)
