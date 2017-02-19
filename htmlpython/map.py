#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Mapas y figuras encapsuladas

#Definición de map
def map_(content, atribute):
    start = "\n<map %s>"
    middle = start %atribute
    final = middle + "\n%s\n</map>\n"
    returned = final %content
    return returned
    
#Definición de area shape="" coords ="" href ="", se incluye dentro de <map></map>
def area(content, atribute):
    start = "\n<area %s>"
    middle = start %atribute
    final = middle + "\n%s\n</area>\n"
    returned = final %content
    return returned

#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")