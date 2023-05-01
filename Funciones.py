#Creación de las visualizaciones

"1. Exploración de los datos--------------------------------------------------------------"
#Graficos de pie
def Conexion_DB_():
    import pandas as pd
    import psycopg2
    import os
    from dotenv import load_dotenv
    # path to env file
    env_path='informacion.env'
    # load env 
    load_dotenv(dotenv_path=env_path)
    # extract env variables
    USER=os.getenv('DUSER')
    PASSWORD=os.getenv('DPASSWORD')
    HOST=os.getenv('DHOST')
    PORT=os.getenv('DPORT')
    DBNAME=os.getenv('DDBNAME')
    print(HOST)
    #connect to DB
    engine = psycopg2.connect(
        dbname=DBNAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    
    cursor = engine.cursor()
    
    query = """
    SELECT * 
    FROM mytable;"""
    
    cursor.execute(query)
    data=cursor.fetchall()
    df=pd.DataFrame(data,columns=['id','age', 'sex', 'cpt', 'pressure', 'chol', 'sugar', 'ecg', 'maxbpm',
           'angina', 'oldpeak', 'slope', 'flourosopy', 'thal', 'diagnosis'])
    datos=df.drop("id", axis=1)
    return datos
def crear_visualizaciones(datos):
    #############################################################################################
    #Creación de las visualizaciones
    import numpy as np
    import matplotlib.pyplot as plt
    
    "1. Exploración de los datos--------------------------------------------------------------"
    #Graficos de pie
    
    
    #Género
    fig, ax = plt.subplots()
    etiquetas = ["Mujeres","Hombres"]
    valores = [datos.loc[(datos['sex'] == 0)].shape[0],(datos["sex"]==1).sum()]
    colores=["#D7F47C", "#81E2DF"]
    ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%', textprops = {'fontsize': 14})
    plt.title("Sexo de la muestra", fontsize = 18)
    fig.subplots_adjust(top=0.9,bottom=0.01,right=0.9)
    plt.savefig('Exploracion1.png')
    
    
    #Age   
    fig, ax = plt.subplots()
    etiquetas = ["Joven Adulto","Adultos","Adultos Mayores","Tercera Edad"]
    valores = [(datos["age"]==1).sum(),(datos["age"]==2).sum(),(datos["age"]==3).sum(),(datos["age"]==4).sum()]
    colores=["#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"]
    ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%', textprops = {'fontsize': 14})
    plt.title("Edad de la muestra", fontsize = 18)
    fig.subplots_adjust(top=0.9,bottom=0.01,left=0.008)
    plt.savefig('Exploracion2.png')
    
    
    #"Chol"
    fig, ax = plt.subplots()
    etiquetas = ["Deseable","Elevado","Muy Elevado"]
    valores = [(datos["chol"]==1).sum(),(datos["chol"]==2).sum(),(datos["chol"]==3).sum()]
    colores=["#87CEFA", "#81E2DF","#C1E9FC"]
    ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%', textprops = {'fontsize': 14})
    plt.title("Colesterol sérico de la muestra", fontsize = 18)
    fig.subplots_adjust(top=0.9,bottom=0.01,left=0.008)
    plt.savefig('Exploracion4.png')
    
    
    #"Thalach"
    fig, ax = plt.subplots()
    etiquetas = ["Reposo","Ej Aerobico","Ej Intenso"]
    valores = [(datos["maxbpm"]==1).sum(),(datos["maxbpm"]==2).sum(),(datos["maxbpm"]==3).sum()]
    colores=["#D7F47C", "#12B687","#5EC160"]
    ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%', textprops = {'fontsize': 14})
    plt.title("Frecuencia cardíaca máxima de la muestra", fontsize = 18)
    fig.subplots_adjust(top=0.9,bottom=0.01,left=0.01)
    plt.savefig('Exploracion5.png')
    
    
    
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
    ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=2, fontsize= 14)
    ax.set_title('Edad de las mujeres de la muestra', fontsize = 18)
    fig.subplots_adjust(top=0.9,bottom=0.3)
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
    ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=2, fontsize= 14)
    ax.set_title('Edad de los hombres de la muestra', fontsize = 18)
    fig.subplots_adjust(top=0.9,bottom=0.3)
    plt.savefig('Exploracion8.png')
    
    
    
    
    
    
    ###########################################################################
    
    
    
    
    import seaborn as sns
    Correlacion= datos.corr()
    fig, ax = plt.subplots(figsize=(15,15))
    matriz_redondeada=np.round(Correlacion, decimals=2)
    sns.heatmap(matriz_redondeada, annot=True, cmap='coolwarm', linewidths=1, ax=ax)
    fig.subplots_adjust(top=0.98,bottom=0.05,right=0.95)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=14)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=14)
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
    ax.bar(x, y, color=["#81E2DF","#D7F47C","#DAF6F5", "#F3FCD8"],label="Hombres")
    ax.bar(x, y, color=["#D7F47C","#D7F47C","#DAF6F5", "#F3FCD8"],label="Mujeres")
    ax.bar(x, y, color=["#81E2DF","#D7F47C","#DAF6F5", "#F3FCD8"])
    
    # quitar los bordes del gráfico y los valores del eje y
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().set_yticks([])
    
    for i, v in enumerate(y):
        plt.text(i, v + 3, str(v), color='black', ha='center')
    
    # agregar leyenda
    ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=2, fontsize= 14)
    ax.set_title('Cantidad de personas enfermas y sanas por sexo', fontsize = 18)
    ax.set_xticks(x)
    ax.set_xticklabels(['                         Enfermos','','                         Sanos',''])
    fig.subplots_adjust(top=0.9,bottom=0.2,left=0.08)
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
    #"#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"
    ax.bar(x, y, color=["#99EEF9", "#8AD6F4","#3EAEF4","#81E2DF","#DBF9FD","#CFEFFC","#B3E0FB","#DAF6F5"],label="Jovenes")
    ax.bar(x, y, color=["#8AD6F4", "#8AD6F4","#3EAEF4","#81E2DF","#DFF4FD","#8BBDF5","#CDE9DC","#D8EACC"],label="Adultos")
    ax.bar(x, y, color=["#3EAEF4", "#8AD6F4","#3EAEF4","#81E2DF","#E9FEB4","#EEF8E4","#CDE9DC","#D8EACC"],label="Adultos Mayores")
    ax.bar(x, y, color=["#81E2DF", "#8AD6F4","#3EAEF4","#81E2DF","#E9FEB4","#EEF8E4","#CDE9DC","#D8EACC"],label="Tercera Edad")
    ax.bar(x, y, color=["#99EEF9", "#8AD6F4","#3EAEF4","#81E2DF","#DBF9FD","#CFEFFC","#B3E0FB","#DAF6F5"])
    
    # quitar los bordes del gráfico y los valores del eje y
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().set_yticks([])
    
    for i, v in enumerate(y):
        plt.text(i, v + 1, str(v), color='black', ha='center')
    
    # agregar leyenda
    ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=2, fontsize= 14)
    ax.set_title('Cantidad de personas enfermas y sanas por edad', fontsize = 18)
    ax.set_xticks(x)
    ax.set_xticklabels(['                                      Enfermos','','','','                                     Sanos','','',''])
    fig.subplots_adjust(top=0.9,bottom=0.3)
    plt.savefig('Propension2.png')
    
    
    
    "------------------------------TERCER GRÁFICO-----------------------------------"
    pressure_J1 = datos.loc[(datos['age'] == 1) & (datos['pressure'] == 1)].shape[0]
    pressure_A1 = datos.loc[(datos['age'] == 2) & (datos['pressure'] == 1)].shape[0]
    pressure_AM1 = datos.loc[(datos['age'] == 3) & (datos['pressure'] == 1)].shape[0]
    pressure_T1 = datos.loc[(datos['age'] == 4) & (datos['pressure'] == 1)].shape[0]
    
    
    pressure_J2 = datos.loc[(datos['age'] == 1) & (datos['pressure'] == 2)].shape[0]
    pressure_A2 = datos.loc[(datos['age'] == 2) & (datos['pressure'] == 2)].shape[0]
    pressure_AM2 = datos.loc[(datos['age'] == 3) & (datos['pressure'] == 2)].shape[0]
    pressure_T2 = datos.loc[(datos['age'] == 4) & (datos['pressure'] == 2)].shape[0]
    
    pressure_J3 = datos.loc[(datos['age'] == 1) & (datos['pressure'] == 3)].shape[0]
    pressure_A3 = datos.loc[(datos['age'] == 2) & (datos['pressure'] == 3)].shape[0]
    pressure_AM3 = datos.loc[(datos['age'] == 3) & (datos['pressure'] == 3)].shape[0]
    pressure_T3 = datos.loc[(datos['age'] == 4) & (datos['pressure'] == 3)].shape[0]
    
    pressure_J4 = datos.loc[(datos['age'] == 1) & (datos['pressure'] == 4)].shape[0]
    pressure_A4 = datos.loc[(datos['age'] == 2) & (datos['pressure'] == 4)].shape[0]
    pressure_AM4 = datos.loc[(datos['age'] == 3) & (datos['pressure'] == 4)].shape[0]
    pressure_T4 = datos.loc[(datos['age'] == 4) & (datos['pressure'] == 4)].shape[0]
    
    pressure_J5 = datos.loc[(datos['age'] == 1) & (datos['pressure'] == 5)].shape[0]
    pressure_A5 = datos.loc[(datos['age'] == 2) & (datos['pressure'] == 5)].shape[0]
    pressure_AM5 = datos.loc[(datos['age'] == 3) & (datos['pressure'] == 5)].shape[0]
    pressure_T5 = datos.loc[(datos['age'] == 4) & (datos['pressure'] == 5)].shape[0]
    
    y1 = [pressure_J1, pressure_A1,  pressure_AM1,pressure_T1]
    y2 = [pressure_J2, pressure_A2,  pressure_AM2,pressure_T2]
    y3 = [pressure_J3, pressure_A3,  pressure_AM3,pressure_T3]
    y4 = [pressure_J4, pressure_A4,  pressure_AM4,pressure_T4]
    y5 = [pressure_J5, pressure_A5,  pressure_AM5,pressure_T5]
    
    x1 = ['1','2','3','4']
    x2 = ['5','6','7','8']
    x3 = ['9','10','11','12']
    x4 = ['13','14','15','16']
    x5 = ['17','18','19','20']
    
    
    # Gráfico de líneas
    fig, ax = plt.subplots()
    ax.plot(x1, y1, marker = "o", label = "Presión normal " ,color="#CFEFFC", linewidth=3)
    ax.plot(x2, y2, marker = "o", label = "Prehipertensión",color="#3EAEF4", linewidth=3)
    ax.plot(x3, y3, marker = "o", label = "Hipertensión E1",color="#8AD6F4", linewidth=3)
    ax.plot(x4, y4, marker = "o", label = "Hipertensión E2",color="#81E2DF", linewidth=3)
    ax.plot(x5, y5, marker = "o", label = "Crisis Hipertensiva",color="#0070C0", linewidth=3)
    
    # quitar los bordes del gráfico y los valores del eje y
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().set_yticks([])
    ax.set_xticks([])
    plt.title("Presión arterial según la edad", fontsize = 18)
    #descripcion="El primer punto corresponde a los Jovenes, \nel segundo a los Adultos, el tercero a los Adultos Mayores.\nPor ultimo los Aducltos de la Tercera Edad"
    
    plt.ylim(bottom=0)
    ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.02], ncol=2, fontsize= 14)
    fig.subplots_adjust(top=0.9,bottom=0.3)
    plt.savefig('Propension3.png')
    
    
    "------------------------------CUARTA GRÁFICA-----------------------------------"
    chol_J1 = datos.loc[(datos['age'] == 1) & (datos['chol'] == 1)].shape[0]
    chol_A1 = datos.loc[(datos['age'] == 2) & (datos['chol'] == 1)].shape[0]
    chol_AM1 = datos.loc[(datos['age'] == 3) & (datos['chol'] == 1)].shape[0]
    chol_T1 = datos.loc[(datos['age'] == 4) & (datos['chol'] == 1)].shape[0]
    
    chol_J2 = datos.loc[(datos['age'] == 1) & (datos['chol'] == 2)].shape[0]
    chol_A2 = datos.loc[(datos['age'] == 2) & (datos['chol'] == 2)].shape[0]
    chol_AM2 = datos.loc[(datos['age'] == 3) & (datos['chol'] == 2)].shape[0]
    chol_T2 = datos.loc[(datos['age'] == 4) & (datos['chol'] == 2)].shape[0]
    
    chol_J3 = datos.loc[(datos['age'] == 1) & (datos['chol'] == 3)].shape[0]
    chol_A3 = datos.loc[(datos['age'] == 2) & (datos['chol'] == 3)].shape[0]
    chol_AM3 = datos.loc[(datos['age'] == 3) & (datos['chol'] == 3)].shape[0]
    chol_T3 = datos.loc[(datos['age'] == 4) & (datos['chol'] == 3)].shape[0]
    
    y1 = [chol_J1, chol_A1,  chol_AM1, chol_T1]
    y2 = [chol_J2, chol_A2,  chol_AM2, chol_T2]
    y3 = [chol_J3, chol_A3,  chol_AM3, chol_T3]
    
    x1 = ['1','2','3','4']
    x2 = ['5','6','7','8']
    x3 = ['9','10','11','12']
    
    # Gráfico de líneas
    fig, ax = plt.subplots()
    ax.plot(x1, y1, marker = "o", label = "Deseable " ,color="#D7F47C", linewidth=3)
    ax.plot(x2, y2, marker = "o", label = "Elevado",color="#12B687", linewidth=3)
    ax.plot(x3, y3, marker = "o", label = "Muy Elevado",color="#90E0AE", linewidth=3)
    
    # quitar los bordes del gráfico y los valores del eje y
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().set_yticks([])
    ax.set_xticks([])
    plt.title("Colesterol según la edad", fontsize = 18)
    #descripcion="El primer punto corresponde a los Jovenes, \nel segundo a los Adultos, el tercero a los Adultos Mayores.\nPor ultimo los Aducltos de la Tercera Edad"
    
    plt.ylim(bottom=0)
    ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.02], ncol=3, fontsize= 14)
    plt.savefig('Propension4.png')
    
    
    "------------------------------QUINTO GRÁFICO-----------------------------------"
    maxbpm_J1 = datos.loc[(datos['age'] == 1) & (datos['maxbpm'] == 1)].shape[0]
    maxbpm_A1 = datos.loc[(datos['age'] == 2) & (datos['maxbpm'] == 1)].shape[0]
    maxbpm_AM1 = datos.loc[(datos['age'] == 3) & (datos['maxbpm'] == 1)].shape[0]
    maxbpm_T1 = datos.loc[(datos['age'] == 4) & (datos['maxbpm'] == 1)].shape[0]
    
    maxbpm_J2 = datos.loc[(datos['age'] == 1) & (datos['maxbpm'] == 2)].shape[0]
    maxbpm_A2 = datos.loc[(datos['age'] == 2) & (datos['maxbpm'] == 2)].shape[0]
    maxbpm_AM2 = datos.loc[(datos['age'] == 3) & (datos['maxbpm'] == 2)].shape[0]
    maxbpm_T2 = datos.loc[(datos['age'] == 4) & (datos['maxbpm'] == 2)].shape[0]
    
    maxbpm_J3 = datos.loc[(datos['age'] == 1) & (datos['maxbpm'] == 3)].shape[0]
    maxbpm_A3 = datos.loc[(datos['age'] == 2) & (datos['maxbpm'] == 3)].shape[0]
    maxbpm_AM3 = datos.loc[(datos['age'] == 3) & (datos['maxbpm'] == 3)].shape[0]
    maxbpm_T3 = datos.loc[(datos['age'] == 4) & (datos['maxbpm'] == 3)].shape[0]
    
    y1 = [maxbpm_J1, maxbpm_A1,  maxbpm_AM1,maxbpm_T1]
    y2 = [maxbpm_J2, maxbpm_A2,  maxbpm_AM2,maxbpm_T2]
    y3 = [maxbpm_J3, maxbpm_A3,  maxbpm_AM3,maxbpm_T3]
    
    x1 = ['1','2','3','4']
    x2 = ['5','6','7','8']
    x3 = ['9','10','11','12']
    
    # Gráfico de líneas
    fig, ax = plt.subplots()
    ax.plot(x1, y1, marker = "o", label = "Deseable " ,color="#99EEF9", linewidth=3)
    ax.plot(x2, y2, marker = "o", label = "Elevado",color="#8AD6F4", linewidth=3)
    ax.plot(x3, y3, marker = "o", label = "Muy Elevado",color="#3EAEF4", linewidth=3)
    
    # quitar los bordes del gráfico y los valores del eje y
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().set_yticks([])
    ax.set_xticks([])
    plt.title("Frecuencia cardíaca según la edad", fontsize = 18)
    #descripcion="El primer punto corresponde a los Jovenes, \nel segundo a los Adultos, el tercero a los Adultos Mayores.\nPor ultimo los Aducltos de la Tercera Edad"
    
    plt.ylim(bottom=0)
    ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.02], ncol=3, fontsize= 14)
    plt.savefig('Propension5.png')
    
    
    
    
    
    "------------------------------SEXTO GRÁFICO-----------------------------------"
    pressure_J2 = datos.loc[(datos['age'] == 1) & (datos['oldpeak'] == 2)].shape[0]
    pressure_A2 = datos.loc[(datos['age'] == 2) & (datos['oldpeak'] == 2)].shape[0]
    pressure_AM2 = datos.loc[(datos['age'] == 3) & (datos['oldpeak'] == 2)].shape[0]
    pressure_T2 = datos.loc[(datos['age'] == 4) & (datos['oldpeak'] == 2)].shape[0]
    
    pressure_J3 = datos.loc[(datos['age'] == 1) & (datos['oldpeak'] == 3)].shape[0]
    pressure_A3 = datos.loc[(datos['age'] == 2) & (datos['oldpeak'] == 3)].shape[0]
    pressure_AM3 = datos.loc[(datos['age'] == 3) & (datos['oldpeak'] == 3)].shape[0]
    pressure_T3 = datos.loc[(datos['age'] == 4) & (datos['oldpeak'] == 3)].shape[0]
    
    pressure_J4 = datos.loc[(datos['age'] == 1) & (datos['oldpeak'] == 4)].shape[0]
    pressure_A4 = datos.loc[(datos['age'] == 2) & (datos['oldpeak'] == 4)].shape[0]
    pressure_AM4 = datos.loc[(datos['age'] == 3) & (datos['oldpeak'] == 4)].shape[0]
    pressure_T4 = datos.loc[(datos['age'] == 4) & (datos['oldpeak'] == 4)].shape[0]
    
    y1 = [pressure_J1, pressure_A1,  pressure_AM1,pressure_T1]
    y2 = [pressure_J2, pressure_A2,  pressure_AM2,pressure_T2]
    y3 = [pressure_J3, pressure_A3,  pressure_AM3,pressure_T3]
    y4 = [pressure_J4, pressure_A4,  pressure_AM4,pressure_T4]
    
    x1 = ['1','2','3','4']
    x2 = ['5','6','7','8']
    x3 = ['9','10','11','12']
    x4 = ['13','14','15','16']
    
    
    # Gráfico de líneas
    fig, ax = plt.subplots()
    ax.plot(x1, y1, marker = "o", label = "Normal " ,color="#D7F47C", linewidth=3)
    ax.plot(x2, y2, marker = "o", label = "Ligeramente Elevado",color="#12B687", linewidth=3)
    ax.plot(x3, y3, marker = "o", label = "Moderadamente Elevado",color="#5EC160", linewidth=3)
    ax.plot(x4, y4, marker = "o", label = "Altamente Elevado",color="#90E0AE", linewidth=3)
    
    # quitar los bordes del gráfico y los valores del eje y
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().set_yticks([])
    ax.set_xticks([])
    plt.title("Depresión ST según la edad", fontsize = 18)
    #descripcion="El primer punto corresponde a los Jovenes, \nel segundo a los Adultos, el tercero a los Adultos Mayores.\nPor ultimo los Aducltos de la Tercera Edad"
    
    plt.ylim(bottom=0)
    ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.02], ncol=2, fontsize= 14)
    fig.subplots_adjust(top=0.9,bottom=0.3)
    plt.savefig('Propension6.png')
    
    
    ############
    return None

def estimar(radio1,radio2, radio3, dropdown1, dropdown2, dropdown3, dropdown4, dropdown5, dropdown6, dropdown7, dropdown8, dropdown9, dropdown10):
    from pgmpy.inference import VariableElimination
    from pgmpy.readwrite import BIFReader

    Sex=9
    if radio1 == 'Hombre':
       Sex="1"
    elif radio1 ==  'Mujer':
       Sex="0"
       
    Exang=9
    if radio2 == 'Si':
       Exang="1"
    elif radio2 == 'No':
       Exang="0"
 
       
    Fbs=9
    if radio3 == 'Si':
       Fbs="1"
    elif radio3 ==  'No':
       Fbs="0"
    
    
    edad = 9
    if dropdown1 == "Entre 29 y 39 años":
        edad = "1"
    elif dropdown1 == "Entre 40 y 54 años":
            edad = "2"
    elif dropdown1 == "Entre 55 y 64 años":
        edad = "3"
    elif dropdown1 == "Entre 65 y 79 años":
        edad ="4"
    
    CP = 9
    if dropdown2 == 'Angina típica':
        CP = "1"
    elif dropdown2 == 'Angina atípica':
        CP = "2"
    elif dropdown2 == 'Dolor no anginoso':
        CP = "3"
    elif dropdown2 == 'Asintomático':
        CP = "4"
    
    Trestbps =9
    
    if dropdown3 == 'Entre 94 y 120':
        Trestbps = "1"
    elif dropdown3 == 'Entre 121 y 129':
        Trestbps = "2"
    elif dropdown3 == 'Entre 130 y 139':
        Trestbps = "3"
    elif dropdown3 == 'Entre 140 y 180':
        Trestbps = "4"
    elif dropdown3 == 'Entre 181 y 210':
        Trestbps = "5"
        
    Chol =9
    
    if dropdown4 == 'Deseable':
        Chol = "1"
    elif dropdown4 == 'Elevado':
        Chol = "2"
    elif dropdown4 == 'Muy Elevado':
        Chol = "3"
    
    ecg=9
    if dropdown5 == 'Normal':
        ecg = "0"
    elif dropdown5 =='Anormalidad de la onda ST-T':
        ecg = "1"
    elif dropdown5 =='Hipertrofia ventricular':
        ecg = "2"
        
    maxbpm=9    
    if dropdown6 =='Entre 71 y 139':
        maxbpm="1"
    elif dropdown6 =='Entre 140 y 169':
        maxbpm="2"
    elif dropdown6 =='Entre 170 y 210':
        maxbpm="3"
    
    slope = 9
    if dropdown7 =='Pendiente ascendente':
        slope="1"
    elif dropdown7 =='Plano':
        slope="2"
    elif dropdown7 =='Pendiente descendente':
        slope="3"

    ca=9
    if dropdown8 =='1':
        ca="1"
    elif dropdown8 =='2':
        ca="2"
    elif dropdown8 =='3':
        ca="3"
    
    Oldpeak=9
    if dropdown9 == 'Normal':
        Oldpeak="1"
    elif dropdown9 == 'Lig. Elevada':
        Oldpeak="2"
    elif dropdown9 == 'Mod. Elevada':
        Oldpeak="3"
    elif dropdown9 == 'Alt. Elevada':
        Oldpeak="4"
   
    
    Thal=9
    if dropdown10 == 'Normal':
        Thal="3"
    elif dropdown10 == 'Defecto Fijo':
        Thal="6"
    elif dropdown10 == 'Defecto Reversible':
        Thal="7"
   
    modelo = BIFReader("Modelo.bif").get_model()
    inferencia = VariableElimination(modelo)
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
    
    resultado = inferencia.query(['diagnosis'],evidence=evidencia).values
    return resultado

