#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: frames

#Definición de frameset, cols= "%<int> ... %<int>" similar a <body></body>
def frameset(content, atribute):
    start = "\n<frameset %s>"
    middle = start %atribute
    final = middle + "\n%s\n</frameset>\n"
    returned = final %content
    return returned
    
#Definición de noframes, cuando no es soportado similar a <body></body>
def noframes(content, atribute):
    start = "\n<noframes %s>"
    middle = start %atribute
    final = middle + "\n%s\n</noframes>\n"
    returned = final %content
    return returned
    
#Definición de frame se incluye dentro de <frameset></frameset>
def frame(content, atribute):
    start = "\n<frame %s>"
    middle = start %atribute
    final = middle + "\n%s\n</frame>\n"
    returned = final %content
    return returned

#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")