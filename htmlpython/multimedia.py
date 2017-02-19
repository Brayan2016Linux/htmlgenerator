#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Imagenes encapsuladas

#Definición de video (html5)
def video(content, atribute):
    start = "\n<video %s>"
    middle = start %atribute
    final = middle + "\n%s\n</video>\n"
    returned = final %content
    return returned
    
#Definición de audio (html5)
def audio(content, atribute):
    start = "\n<audio %s>"
    middle = start %atribute
    final = middle + "\n%s\n</audio>\n"
    returned = final %content
    return returned
    
#Definición de bgsound
def bgsound(content, atribute):
    start = "\n<bgsound %s>"
    middle = start %atribute
    final = middle + "\n%s\n</bgsound>\n"
    returned = final %content
    return returned
    
#Definición de source (html5) se incluye dentro de <video></video>
def source(source, atributes):
    start = "\n<source src=\"%s\""
    middle = start %source
    final = middle + "%s>\n"
    returned = final %atributes
    return returned
    
#Definición de embed height src type width
def embed(source, atributes):
    start = "\n<embed src=\"%s\""
    middle = start %source
    final = middle + "%s>\n"
    returned = final %atributes
    return returned
    
#Definición de bgsound
def noembed(content, atribute):
    start = "\n<noembed %s>"
    middle = start %atribute
    final = middle + "\n%s\n</noembed>\n"
    returned = final %content
    return returned

#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")
