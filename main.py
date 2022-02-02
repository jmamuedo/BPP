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