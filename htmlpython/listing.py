#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Tags para crear Listas y Menus

#Definición de ul lista sin ordenar
#Se incluye generalmente dentro de <div></div>
def ul(content, atribute):
    start = "\n<ul %s>\n"
    middle = start %atribute
    final = middle + "%s\n</ul>\n"
    returned = final %content
    return returned
    
#Definición de ol lista ordenada
#Se incluye generalmente dentro de <div></div>
def ol(content, atribute):
    start = "\n<ol %s>\n"
    middle = start %atribute
    final = middle + "%s\n</ol>\n"
    returned = final %content
    return returned
    
#Definición del enmarcado li (items de listas)
#Se incluye dentro de <ul></ul> o <ol></ol>
def li(content, atribute):
    start = "\n<li %s>"
    middle = start %atribute
    final = middle + "%s</li>\n"
    returned = final %content
    return returned
    
#Definición de dl lista de definición
def dl(content, atribute):
    start = "\n<dl %s>\n"
    middle = start %atribute
    final = middle + "%s\n</dl>\n"
    returned = final %content
    return returned
    
#Definición de dt lista de definición de término
def dt(content, atribute):
    start = "\n<dt %s>\n"
    middle = start %atribute
    final = middle + "%s\n</dt>\n"
    returned = final %content
    return returned
    
#Definición de dd lista de definición sobre el termino
def dd(content, atribute):
    start = "\n<dd %s>\n"
    middle = start %atribute
    final = middle + "%s\n</dd>\n"
    returned = final %content
    return returned
    
#Definición de tt listado
def tt(content, atribute):
    start = "\n<tt %s>\n"
    middle = start %atribute
    final = middle + "%s\n</tt>\n"
    returned = final %content
    return returned
    

#Para ejecución directa sin importacion
if __name__ == "__main__":
        print("You should import headers into your main proyect.")
