#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Imagenes y gráficos encapsuladas

#Definición de img (inclusión de imagenes)
def img(atribute):
    start = "\n<img %s"
    middle = start %atribute
    final = middle + "></img>"
    returned = final
    return returned
    
#Definición de canvas (html5)
def canvas(content, atribute):
    start = "\n<canvas %s>"
    middle = start %atribute
    final = middle + "\n%s\n</canvas>\n"
    returned = final %content
    return returned

#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")
