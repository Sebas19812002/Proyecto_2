import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
datos = pd.read_csv("Datos.data")
datos.head()

print(datos.corr())
#Recorrer datos y eliminar faltantes
datos1 = datos
for i in range (0,len(datos1)):
    if datos1["Ca"][i]=="?":
        datos1.drop(i,axis=0,inplace=True)
    elif datos1["Thal"][i]=="?":
        datos1.drop(i,axis=0,inplace=True)
#Cambiar tipo 
print(datos1.dtypes)
datos1[["Ca","Thal"]]=datos1[["Ca","Thal"]].apply(pd.to_numeric)


# Diagrama de regresion
x = [datos1["Num"]]
y = [datos1["Thalach"]]

x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

x_reg = np.linspace(min(x), max(x), 100).reshape(-1, 1)
y_reg = model.predict(x_reg)

plt.scatter(x, y,color='#92C5FC')
plt.plot(x_reg, y_reg, color='red')

plt.xlabel('Num')
plt.ylabel('Thalach')
plt.title('Regresión lineal Num vs Thalach')

plt.show()

#Grafica de Barras
x = datos1["Num"]
y = datos1["Oldpeak"]

# Crear un gráfico de barras
fig, ax=plt.subplots()
ax.bar(x, y,color='#92C5FC')

# Agregar etiquetas de eje y título
ax.set_xlabel('Num')
ax.set_ylabel('Oldpeak')
ax.set_title('Diagrama de barras Num vs Oldpeak')
ax.set_xticks(x)

# Mostrar el gráfico
plt.show()


scores=["Age","Trestbps", "Chol","Thalach","Oldpeak"]
for i in scores:
    fig = plt.figure()
    x=datos1[i]
    #plt.hist(x,color='#53B8B4')
    plt.hist(x,color='#3CB043')
    plt.title(i + " (Discreta)", fontsize = 18)
    #grafica=x.plot(kind="hist",bins=30,color='#53B8B4')
    #grafica.set_title(i)
    
plt.show()
#Graficas de dispesión
for i in scores:
    for j in scores:
        fig, ax = plt.subplots()
        ax.scatter(datos[i],datos[j])
        ax.set_title (i + " VS " + j)
        plt.show()
# Estadisticas descriptivas
print(datos.min())
print(datos.mean())
print(datos.max())
print(datos.corr())
corr=datos.corr()

datos1=datos

#Cambiar los valores de NUM

for i in range (0,302):
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287: 
        if datos1["Num"][i]!=0: 
            datos1["Num"][i]=1



#Variables Categoricas

for i in range (0,302):
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287: 
        if datos1["Age"][i]>=29 and datos1["Age"][i]<40:
            datos1["Age"][i]=1
        elif datos1["Age"][i]>=40 and datos1["Age"][i]<55:
            datos1["Age"][i]=2
        elif datos1["Age"][i]>=55 and datos1["Age"][i]<65:
            datos1["Age"][i]=3
        elif datos1["Age"][i]>=65 and datos1["Age"][i]<80:
            datos1["Age"][i]=4

   
    
for i in range (0,302):    
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287: 
        if datos1["Trestbps"][i]>=94 and datos1["Trestbps"][i]<120:
            datos1["Trestbps"][i]=1
        elif datos1["Trestbps"][i]>=120 and datos1["Trestbps"][i]<130:
            datos1["Trestbps"][i]=2
        elif datos1["Trestbps"][i]>=130 and datos1["Trestbps"][i]<140:
            datos1["Trestbps"][i]=3
        elif datos1["Trestbps"][i]>=140 and datos1["Trestbps"][i]<181:
            datos1["Trestbps"][i]=4
        elif datos1["Trestbps"][i]>=181 and datos1["Trestbps"][i]<=210:
            datos1["Trestbps"][i]=5


for i in range (0,302):    
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287:     
        if datos1["Chol"][i]>=126 and datos1["Chol"][i]<200:
            datos1["Chol"][i]=1
        elif datos1["Chol"][i]>=200 and datos1["Chol"][i]<301:
            datos1["Chol"][i]=2
        elif datos1["Chol"][i]>=301 and datos1["Chol"][i]<570:
            datos1["Chol"][i]=3

for i in range (0,302):    
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287:      
        if datos1["Thalach"][i]>=71 and datos1["Thalach"][i]<140:
            datos1["Thalach"][i]=1
        elif datos1["Thalach"][i]>=140 and datos1["Thalach"][i]<170:
            datos1["Thalach"][i]=2
        elif datos1["Thalach"][i]>=170 and datos1["Thalach"][i]<=210:
            datos1["Thalach"][i]=3


for i in range (0,302):    
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287:      
        if datos1["Oldpeak"][i]<1:
            datos1["Oldpeak"][i]=1
        elif datos1["Oldpeak"][i]>=1 and datos1["Oldpeak"][i]<2:
            datos1["Oldpeak"][i]=2
        elif datos1["Oldpeak"][i]>=2 and datos1["Oldpeak"][i]<=3:
            datos1["Oldpeak"][i]=3
        elif datos1["Oldpeak"][i]>=3:
            datos1["Oldpeak"][i]=4



#datos1.to_excel("Datos Categorizados.xlsx", index=False)


# Age vs Num
etiquetas=["Joven Adulto","Adultos","Adultos Mayores","Tercera Edad"]
y1=[4,38,75,20]
y0=[10,86,43,21]

Co=np.arange(len(y1))
Ancho=0.30

fig, ax=plt.subplots()
ax.bar(Co-Ancho/2,y1,width=Ancho,color='#53B8B4', label="1")
ax.bar(Co+Ancho/2,y0,width=Ancho,color='#6ACDE5', label="0")

ax.set_title("Age vs Num", fontsize = 18)
ax.set_ylabel("Numero de personas")
ax.set_xlabel("Categorias de la Edad")
ax.set_xticks(Co)
ax.set_xticklabels(etiquetas)
plt.legend(loc='best')
plt.show()



#Trestbps vs Num
etiquetas=["P.A Normal","Prehip.","Hip. etapa 1","Hip. etapa 2","Crisis Hip."]
y1=[23,34,26,52,2]
y0=[37,38,41,44,0]

Co=np.arange(len(y1))
Ancho=0.30

fig, ax=plt.subplots()
ax.bar(Co-Ancho/2,y1,width=Ancho,color="#98fb98", label="1")
ax.bar(Co+Ancho/2,y0,width=Ancho,color="#6DC36D", label="0")

ax.set_title("Trestbps vs Num", fontsize = 18)
ax.set_ylabel("Numero de personas")
ax.set_xlabel("Categorias de Trestbps")
ax.set_xticks(Co)
ax.set_xticklabels(etiquetas)
plt.legend(loc='best')
plt.show()


#"Chol" vs Num
etiquetas=["Deseable","Elevado","Muy Elevado"]
y1=[20,96,21]
y0=[28,109,23]

Co=np.arange(len(y1))
Ancho=0.30

fig, ax=plt.subplots()
ax.bar(Co-Ancho/2,y1,width=Ancho,color='#53B8B4', label="1")
ax.bar(Co+Ancho/2,y0,width=Ancho,color='#6ACDE5', label="0")

ax.set_title("Chol vs Num", fontsize = 18)
ax.set_ylabel("Numero de personas")
ax.set_xlabel("Categorias de Chol")
ax.set_xticks(Co)
ax.set_xticklabels(etiquetas)
plt.legend(loc='best')
plt.show()


#"Thalach" vs Num
etiquetas=["Reposo","Ejercicio Aerobico","Ejercicio Intenso"]
y1=[61,66,10]
y0=[22,86,51]

Co=np.arange(len(y1))
Ancho=0.30

fig, ax=plt.subplots()
ax.bar(Co-Ancho/2,y1,width=Ancho,color="#98fb98", label="1")
ax.bar(Co+Ancho/2,y0,width=Ancho,color="#6DC36D", label="0")

ax.set_title("Thalach vs Num", fontsize = 18)
ax.set_ylabel("Numero de personas")
ax.set_xlabel("Categorias de Thalach")
ax.set_xticks(Co)
ax.set_xticklabels(etiquetas)
plt.legend(loc='best')
plt.show()


#"Oldpeak" vs Num
etiquetas=["Normal","Ligeramente","Moderadamente","Altamente"]
y1=[46,41,32,18]
y0=[115,36,7,2]

Co=np.arange(len(y1))
Ancho=0.30

fig, ax=plt.subplots()
ax.bar(Co-Ancho/2,y1,width=Ancho,color='#53B8B4', label="1")
ax.bar(Co+Ancho/2,y0,width=Ancho,color='#6ACDE5', label="0")

ax.set_title("Oldpeak vs Num", fontsize = 18)
ax.set_ylabel("Numero de personas")
ax.set_xlabel("Categorias de Oldpeak")
ax.set_xticks(Co)
ax.set_xticklabels(etiquetas)
plt.legend(loc='best')
plt.show()


#"Sexo" vs Num
etiquetas=["Hombre","Mujer"]
y1=[112,25]
y0=[89,71]

Co=np.arange(len(y1))
Ancho=0.30

fig, ax=plt.subplots()
ax.bar(Co-Ancho/2,y1,width=Ancho,color='#53B8B4', label="1")
ax.bar(Co+Ancho/2,y0,width=Ancho,color='#6ACDE5', label="0")

ax.set_title("Sexo vs Num", fontsize = 18)
ax.set_ylabel("Numero de personas")
ax.set_xticks(Co)
ax.set_xticklabels(etiquetas)
plt.legend(loc='best')
plt.show()





#Diagrama de PIE
#Age   
fig, ax = plt.subplots()
etiquetas = ["Joven Adulto","Adultos","Adultos Mayores","Tercera Edad"]
valores = [(datos1["Age"]==1).sum(),(datos1["Age"]==2).sum(),(datos1["Age"]==3).sum(),(datos1["Age"]==4).sum()]
colores=["#87CEFA", "#0079A5","#6ACDE5","#C1E9FC"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Age (Categórica)", fontsize = 18)
plt.show() 

#"Trestbps"
fig, ax = plt.subplots()
etiquetas = ["Presión arterial normal","Prehipertensión","Hipertensión etapa 1","Hipertensión etapa 2","Crisis Hipertensiva"]
valores = [(datos1["Trestbps"]==1).sum(),(datos1["Trestbps"]==2).sum(),(datos1["Trestbps"]==3).sum(),(datos1["Trestbps"]==4).sum(),(datos1["Trestbps"]==5).sum()]
colores=["#3DED97", "#98fb98","#3CB043","#6DC36D","#234F1E"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Trestbps (Categórica)", fontsize = 18)
plt.show() 

#"Chol"
fig, ax = plt.subplots()
etiquetas = ["Deseable","Elevado","Muy Elevado"]
valores = [(datos1["Chol"]==1).sum(),(datos1["Chol"]==2).sum(),(datos1["Chol"]==3).sum()]
colores=["#87CEFA", "#0079A5","#C1E9FC"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Chol (Categórica)", fontsize = 18)
plt.show() 

#"Thalach"
fig, ax = plt.subplots()
etiquetas = ["Reposo","Ejercicio Aerobico","Ejercicio Intenso"]
valores = [(datos1["Thalach"]==1).sum(),(datos1["Thalach"]==2).sum(),(datos1["Thalach"]==3).sum()]
colores=["#3DED97", "#98fb98","#3CB043"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Thalach (Categórica)", fontsize = 18)
plt.show() 

#"Oldpeak"
fig, ax = plt.subplots()
etiquetas = ["Normal","Ligeramente Elevado","Moderadamente Elevado","Altamente Elevado"]
valores = [(datos1["Age"]==1).sum(),(datos1["Age"]==2).sum(),(datos1["Age"]==3).sum(),(datos1["Age"]==4).sum()]
colores=["#87CEFA", "#0079A5","#6ACDE5","#C1E9FC"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Oldpeak (Categórica)", fontsize = 18)
plt.show() 

















