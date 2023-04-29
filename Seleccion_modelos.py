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
print("Nodos y edges\n")
print(modelo.nodes(),"\n")
print(modelo.edges(),"\n")
modelo_etruct=BayesianNetwork(list(modelo.edges()))
Resultados=Metricas(df2, modelo, "B")
print("Resultados del modelo inicial","\n")
print(Resultados,"\n")
scoring_method = K2Score(data=df)
print("K2 Score","\n")
print(scoring_method.score(modelo_etruct))
scoring_method = BicScore(data=df)
print("BIC Score","\n")
print(scoring_method.score(modelo_etruct))
#--------------Modelo estimado por PC sin nada nuevo--------------##


est = PC(data=df)
modelo_PC = est.estimate(variant="stable", max_cond_vars=5)
modelo_PC = BayesianNetwork(modelo_PC)
modelo_PC.fit(data=df, estimator = BayesianEstimator)
modelo_PC.check_model() 
print("Nodos y edges\n")
print(modelo_PC.nodes(),"\n")
print(modelo_PC.edges(),"\n")
modelo_etruct=BayesianNetwork(list(modelo_PC.edges()))
Resultados=Metricas(df2, modelo_PC, "E")
print("Resultados del modelo inicial","\n")
print(Resultados,"\n")
scoring_method = K2Score(data=df)
print("K2 Score","\n")
print(scoring_method.score(modelo_etruct))
scoring_method = BicScore(data=df)
print("BIC Score","\n")
print(scoring_method.score(modelo_etruct))

#-----------sacar modelo por Hillclimb y score K2 ------------#x    

scoring_method = K2Score(data=df)  #Que tanto una variable es influenciada por posibles padres
esth = HillClimbSearch(data=df)


modelo_k2 = esth.estimate(scoring_method=scoring_method,max_indegree=4,max_iter=int(1e4)) 





#max indegree es el numero de padres maximosn max_inter es el numero de pasos a iterar el Hillclimb
modelo_k2 = BayesianNetwork(modelo_k2)
modelo_k2.fit(data=df, estimator = BayesianEstimator)
modelo_k2.check_model()
print("Nodos y edges\n")
print(modelo_k2.nodes(),"\n")
print(modelo_k2.edges(),"\n")
modelo_etruct=BayesianNetwork(list(modelo_k2.edges()))
Resultados=Metricas(df2, modelo_k2, "E")
print("Resultados del modelo inicial","\n")
print(Resultados,"\n")
scoring_method = K2Score(data=df)
print("K2 Score","\n")
print(scoring_method.score(modelo_etruct))
scoring_method = BicScore(data=df)
print("BIC Score","\n")
print(scoring_method.score(modelo_etruct))



#----------------Modelo Hillclimb con BIC score------------------#

scoring_method = BicScore(data=df)  #Que tanto una variable es influenciada por posibles padres
esth = HillClimbSearch(data=df)
modelo_BIC = esth.estimate(scoring_method=scoring_method, max_indegree=4, max_iter=int(1e4)) #max indegree es el numero de padres maximosn max_inter es el numero de pasos a iterar el Hillclimb
modelo_BIC = BayesianNetwork(modelo_BIC)
modelo_BIC.fit(data=df, estimator = BayesianEstimator)
modelo_BIC.check_model()

print("Nodos y edges\n")
print(modelo_BIC.nodes(),"\n")
print(modelo_BIC.edges(),"\n")
modelo_etruct=BayesianNetwork(list(modelo_BIC.edges()))
Resultados=Metricas(df2, modelo_BIC, "E")
print("Resultados del modelo inicial","\n")
print(Resultados,"\n")
scoring_method = K2Score(data=df)
print("K2 Score","\n")
print(scoring_method.score(modelo_etruct))
scoring_method = BicScore(data=df)
print("BIC Score","\n")
print(scoring_method.score(modelo_etruct))

#-----------------------Modelo de otro grupo----------------------------##
#modelo = BIFReader("modelo_otro_grupo.bif").get_model()
#modelo.check_model()
#print("Nodos y edges\n")
#print(modelo.nodes(),"\n")
#print(modelo.edges(),"\n")
#modelo_etruct=BayesianNetwork(list(modelo.edges()))
#Resultados=Metricas(df2, modelo, "B")
#print("Resultados del modelo inicial","\n")
#print(Resultados,"\n")
#scoring_method = K2Score(data=df)
#print("K2 Score","\n")
#print(scoring_method.score(modelo_etruct))
#scoring_method = BicScore(data=df)
#print("BIC Score","\n")
#print(scoring_method.score(modelo_etruct))




