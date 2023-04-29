from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.estimators import HillClimbSearch
from pgmpy.estimators import K2Score
from pgmpy.readwrite import BIFReader
from pgmpy.estimators import PC
from pgmpy.estimators import BicScore
import pandas as pd
#Tipo es si el modelo es de un .Bif (B) o recien estimado(E), pues el .bif vuelve todo string
def Metricas (test_data, modelo, tipo):
    
    filas=test_data.shape[0]
    nodos=modelo.nodes()
    inferencia = VariableElimination(modelo)    
    tabla = pd.DataFrame(columns=['VP', 'VN', 'FP', 'FN'], index=[0])
    vp=0
    vn=0
    fp=0
    fn=0
    for j in range(0,filas): 
        real=test_data.iloc[j]
        Evidencia={}
        for i in range(0,real.shape[0]-1):
            if  real.index[i] in nodos:
                if tipo=="B" :
                    Evidencia[real.index[i]]=str(real[i])
                elif tipo =="E":
                    Evidencia[real.index[i]]=real[i]
        resultado = inferencia.query(['diagnosis'], evidence=Evidencia).values
        Prediccion=1
        #Prob de no tener = 0
        if resultado[0]>=0.5 :
            Prediccion=0
        if Prediccion == real[-1] and Prediccion==1  :
            vp+=1
        elif Prediccion == real[-1] and Prediccion==0 :
            fp+=1
        elif Prediccion != real[-1] and Prediccion==0 and real[-1]==1 :
            fn+=1
        else:   
            vn+=1
    tabla.loc[0] = [vp,vn, fp, fn]     
    return(tabla)

df=pd.read_csv("Datos_entrenamiento.csv")
df2= pd.read_csv("Datos_test.csv")

###-------------- Nodos que son importantes y no deben cambiar---------------# 
#-----Padres---------#
padres={"sex":0, "age":0}
#-----nodos-------#
nodos=[("diagnosis","ecg")]
#-----------------------Modelo nuestro----------------------------##
modelo = BIFReader("Modelo.bif").get_model()
modelo.check_model()
print(modelo.nodes())
Resultados=Metricas(df2, modelo, "B")
print(modelo.edges())
print("")
print("Resultados del modelo inicial")
print(Resultados)

#--------------Modelo estimado por PC sin nada nuevo--------------##


est = PC(data=df)
modelo_PC = est.estimate(variant="stable", max_cond_vars=5)
print(modelo_PC.nodes())
print(modelo_PC.edges())
modelo_PC = BayesianNetwork(modelo_PC)
modelo_PC.fit(data=df, estimator = BayesianEstimator)
modelo_PC.check_model() 
Resultados=Metricas(df2, modelo_PC, "E")
print("")
print("Resultados del modelo estimado por restricciones")
print(Resultados)


#-----------sacar modelo por Hillclimb y score K2 ------------#x    

scoring_method = K2Score(data=df)  #Que tanto una variable es influenciada por posibles padres
esth = HillClimbSearch(data=df)
modelo_k2 = esth.estimate(scoring_method=scoring_method,max_indegree=4,max_iter=int(1e4)) #max indegree es el numero de padres maximosn max_inter es el numero de pasos a iterar el Hillclimb
print(modelo_k2.nodes())
nodos=list(modelo_k2.nodes())
edges= list(modelo_k2.edges())
print(scoring_method.score(modelo_k2))


#print(scoring_method.score(estimated_model))

#----------------Modelo Hillclimb con BIC score------------------#

scoring_method = BicScore(data=df)  #Que tanto una variable es influenciada por posibles padres
esth = HillClimbSearch(data=df)
estimated_modelh1 = esth.estimate(
    scoring_method=scoring_method, max_indegree=4, max_iter=int(1e4)
) #max indegree es el numero de padres maximosn max_inter es el numero de pasos a iterar el Hillclimb
#print(estimated_modelh1)
#print(estimated_modelh1.nodes())
print(estimated_modelh1.edges())
print(scoring_method.score(estimated_model))







