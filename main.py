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