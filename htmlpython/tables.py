#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: tablas

#Definición de la tabla
def table(content, atribute):
    start = "\n<table %s>\n"
    middle = start %atribute
    final = middle + "%s\n</table>\n"
    returned = final %content
    return returned
    
#Definición del titulo de tabla
#Se incluye dentro de <table></table>
#Align = "bottom" crea un pie
#Align = "top" crea un titulo puede ser omitido
def caption(content, atribute):
    start = "\n<caption %s>\n"
    middle = start %atribute
    final = middle + "%s\n</caption>\n"
    returned = final %content
    return returned
    
#Definición de cada fila de la tabla
#Se incluye dentro de <table></table>
def tr(content, atribute):
    start = "\n<tr %s>\n"
    middle = start %atribute
    final = middle + "%s\n</tr>\n"
    returned = final %content
    return returned
 
#Definición de los nombres de columnas 
#Se incluye dentro de <tr></tr>
def th(content, atribute):
    start = "<th %s>"
    middle = start %atribute
    final = middle + "%s</th>"
    returned = final %content
    return returned

#Definición de cada celda de la tabla   
#Se incluye dentro de <tr></tr>
def td(content, atribute):
    start = "<td %s>"
    middle = start %atribute
    final = middle + "%s</td>"
    returned = final %content
    return returned
    



#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")