#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Controles y Formularios

#Definición de formulario (html5)
def form(content, atribute):
    start = "\n<form %s>"
    middle = start %atribute
    final = middle + "\n%s\n</form>\n"
    returned = final %content
    return returned
    
#Definición de input (html5)
def input_(atribute):
    start = "\n<input %s></input>"
    returned = start %atribute
    return returned
    
#Definición de output (html5)
def output(content, atribute):
    start = "\n<output %s>"
    middle = start %atribute
    final = middle + "\n%s\n</output>\n"
    returned = final %content
    return returned
    
#Definición de progress (html5)
def progress(content, atribute):
    start = "\n<progress %s>"
    middle = start %atribute
    final = middle + "\n%s\n</progress>\n"
    returned = final %content
    return returned
    
#Definición de meter (html5)
def meter(content, atribute):
    start = "\n<meter %s>"
    middle = start %atribute
    final = middle + "\n%s\n</meter>\n"
    returned = final %content
    return returned

#Definición de boton (html5)
def button(content, atribute):
    start = "\n<button %s>"
    middle = start %atribute
    final = middle + "\n%s\n</button>\n"
    returned = final %content
    return returned
    
#Definición de textarea
def textarea(content, atribute):
    start = "\n<textarea %s>"
    middle = start %atribute
    final = middle + "\n%s\n</textarea>\n"
    returned = final %content
    return returned  
    
#Definición de select (tipo de menu)
def select(content, atribute):
    start = "\n<select %s>"
    middle = start %atribute
    final = middle + "\n%s\n</select>\n"
    returned = final %content
    return returned  
    
#Definición de option va dentro de <select></select>
#Atributo: selected para indicar la opción default
#Atributo: multiple size = <numero> para indicar eñ numero de opciones visibles
def option(content, atribute):
    start = "\n<option %s>"
    middle = start %atribute
    final = middle + "\n%s\n</option>\n"
    returned = final %content
    return returned  

#Listas para ser referenciadas con list = "id"
#Definición de datalist (html5)
def datalist(content, atribute):
    start = "\n<datalist %s>"
    middle = start %atribute
    final = middle + "\n%s\n</datalist>\n"
    returned = final %content
    return returned
    
#Definición de option (html5) se incluye dentro de <datalist></datalist>
def option(content, atribute):
    start = "\n<option %s>"
    middle = start %atribute
    final = middle + "\n%s\n</option>\n"
    returned = final %content
    return returned

#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")
