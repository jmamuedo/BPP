# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:08:20 2022

@author: josemaria.amuedo
"""

class Error(Exception):
    """Error.
        Hereda la clase por defecto de python Exception.
    """
    pass
class FicheroAnual(Error):
    """FicheroAnual.
        Se va a encargar de ver si el fichero contiene 12 Meses.
    """
    pass
class HayContenido(Error):
    """HayContenido.
        Se va a encargar de ver que el mes en cuestión contiende datos.
    """
    pass

# Genero todas las funciones de calculo que me servirán
# Balance() calcula las diferencias entres gastos e ingresos
def Balance(result_mes):
    """Método Balance.
        Se encarga de sumar toda la serie que se le pasa del mes a calcular.
            Ejemplo:
                Inputs: result_mes
                    Si pasamos una serie dada como result_mes = [-760, 223, -872, 111]
                    pasamos le método de python que suma una serie de datos sum()
                Ouputs: balance
                    En el caso de ejemplo es -1298
    """
    balance = sum(result_mes)
    return balance
# Gastos() calcula los gastos del mes
def Gastos(result_mes):
    """Método Gastos.
        Se encargaa de sumar solo los datos negativos de toda la serie que se le pasa del mes a calcular.
            Ejemplo:
                Inputs: result_mes
                    Si pasamos una serie dada como result_mes = [-760, 223, -872, 111]
                    los valores que va a sumar van a ser [-760,-872]
                    pasamos le método de python que suma una serie de datos sum()
                Ouputs: gasto
                    En el caso de ejemplo es -1632
    """
    lst_gasto=[]
    for i in result_mes:
        if i < 0:
            lst_gasto.append(i)
        gasto = sum(lst_gasto)
    return gasto
# Ingresos () calcula los ingresos del mes
def Ingresos(result_mes):
    """Método Ingresos.
        Se encarga de sumar solo los datos positivos de toda la serie que se le pasa del mes a calcular.
            Ejemplo:
                Inputs: result_mes
                    Si pasamos una serie dada como result_mes = [-760, 223, -872, 111]
                    los valores que va a sumar van a ser [223,111]
                    pasamos le método de python que suma una serie de datos sum()
                Ouputs: ingreso
                    En el caso de ejemplo es 334
    """
    lst_ingreso=[]
    for i in result_mes:
        if i >= 0:
            lst_ingreso.append(i)
        ingreso = sum(lst_ingreso)
    return ingreso

# ConclusionMensaje() valora si en el me se ha ahorrado o se ha tenido pérdidas
def ConclusionMensaje(result_mes):
    """Método ConclusionMensaje.
        Se encarga de valorar el resultado del método Balance() para poder valorar que supone el resultado en nuestra gestión:
                Si el restultado de Balance es mayor a 0 : 'has ahorrado.'
                Si el restultado de Balance es menor a 0 : 'tienes perdidas.'
                Si el restultado de Balance es igual a 0 : 'sin perdidas.'
        Ejemplo:
            Inputs: result_mes
                Si pasamos una serie dada como result_mes = [-760, 223, -872, 111]
            Outputs: mensaje
                En este caso el valor es -1632 y por tanto mensaje = 'tienes perdidas.'

    """
    if Balance(result_mes) >= 0:
        mensaje = 'has ahorrado.'
    elif Balance(result_mes) < 0:
        mensaje = 'tienes perdidas.'
    else:
        mensaje = 'sin perdidas.'
    return mensaje

def func_pp():
    # leo mi archivo csv
    try:
        df = pd.read_csv('finanzas2020.csv', sep='\t')
        # genero una lista con los meses que aparecen en el archivo
        meses = list(df.columns)
    except IOError as err:
        print("El fichero no puede ser encontrado")
    else:
        print("Fichero leido correctammente")

    # declaro listas vacias
    lista_balance=[]
    lista_gasto=[]
    lista_ingreso=[]
    # Accedemos al dataframe para ir recorriendo los datos por columna
    for column in df:
        try:
            contenido = df[column]
            cont_lst = list(contenido.values)
            result_mes=[]
            # Valoramos si mi archivo tien 12 columnas y si tiene contenido cada mes
            if len(contenido)==12:
                    raise FicheroAnual
        except FicheroAnual:
            print("Tu archivo no tiene 12 columnas")
        try:
            if len(cont_lst)==0:
                raise HayContenido
        except HayContenido:
            print("No hay contenido para el mes")
        # Recorro la lista creada que contiene los valores de un mes
        for i in cont_lst:
            # Primero convierto el valor a string por dos motivos:
            # 1.-Me aseguro que mi valor parte de ser string
            # 2.-Para poder manejar todos los casos a tratar

            i = str(i)
            # Segundo intento eliminar las comillas que pueden darme problemas
            # para manerja mi valor
            i = i.replace("'", "")
            # Tercero convierto a entero, si no puedo lo igualo a cero
            try:
                i = int(i)
            except:
                i = 0
            # Cuarto, voy almacenando mi valor tratado a una lista
            result_mes.append(i)
        # Genero tres variables nuevas para almacenar el resultado de aplicar las funciones
        b = Balance(result_mes)
        g = Gastos(result_mes)
        h = Ingresos(result_mes)
        # Almaceno todo en una lista para poder darle salida mas tarde
        lista_balance.append(b)
        # print("En el mes de ", column ,": ", ConclusionMensaje(result_mes))
        lista_gasto.append(g)
        lista_ingreso.append(h)


    # Genero nuevos dataframes que contienen el total de ingresos, gastos y su Balance
    # de cada mes a lo largo del año
    df_ingreso =  pd.DataFrame([lista_ingreso], columns=meses)
    df_gasto = pd.DataFrame([lista_gasto], columns=meses)
    df_balance = pd.DataFrame([lista_balance], columns=meses)
    # Respondo a las preguntas accediendo a mis nuevos dataframes
    # Obtengo tanto el dato com el mes con mayor ganancia
    maxs_b=df_balance.max(axis=1)
    mes_maxb = df_balance.idxmax(axis=1)
    # Obtengo tanto el dato com el mes con mayor perdida
    mins_B = df_balance.min(axis=1)
    mes_minb = df_balance.idxmin(axis=1)
    # Obtengo tanto el dato concreto del mayor gasto como su mes
    maxs_g=df_gasto.min(axis=1)
    mes_maxg = df_gasto.idxmin(axis=1)
    # Obtengo tanto el dato concreto del mayor ingreso como su mes
    mins_i = df_ingreso.max(axis=1)
    mes_mini = df_ingreso.idxmax(axis=1)
    # Obtengo la media de los gastos del año
    mean_g = df_gasto.mean(axis=1)
    