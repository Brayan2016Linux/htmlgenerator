#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: body_components
#Se incluye dentro de <body></body>

#atributes: id = "identificator" style = ""
#atribute: put "" if don't want to have any

#Definición del header
def header(content, atribute):
    start = "\n<header %s>\n"
    middle = start %atribute
    final = middle + "%s\n</header>\n"
    returned = final %content
    return returned
    
#Definición del div (con identificador)
def div(content, atribute):
    start = "\n<div %s>\n"
    middle = start %atribute
    final = middle + "%s\n</div>\n"
    returned = final %content
    return returned
    
#Definicion HGroup (Agrupa Headers desde h1 a h6, HTML5)
def hgroup(content, atribute):
    start = "\n<hgroup %s>\n"
    middle = start %atribute
    final = middle + "%s\n</hgroup>\n"
    returned = final %content
    return returned
    
#Definición figure para especificar más una figura con figcaption HTML5
def figure(content, atribute):
    start = "\n<figure %s>\n"
    middle = start %atribute
    final = middle + "%s\n</figure>\n"
    returned = final %content
    return returned
    
#Definición figcaption dentro de <figure></figure> HTML5
def figcaption(content, atribute):
    start = "\n<figcaption %s>\n"
    middle = start %atribute
    final = middle + "%s\n</figcaption>\n"
    returned = final %content
    return returned
    
#Definición del nav
def nav(content, atribute):
    start = "\n<nav %s>\n"
    middle = start %atribute
    final = middle + "%s\n</nav>\n"
    returned = final %content
    return returned
  
#Definición de applet
#<applet code ="java.class" atribute></applet>
def applet(content, atribute):
    start = "\n<applet %s>\n"
    middle = start %atribute
    final = middle + "%s\n</applet>\n"
    returned = final %content
    return returned
    
#<param atribute></param> se incluye dentro de <applet></applet>
def param(content, atribute):
    start = "\n<param %s>\n"
    middle = start %atribute
    final = middle + "%s\n</param>\n"
    returned = final %content
    return returned  

def section(content, atribute):
    start = "\n<section %s>\n"
    middle = start %atribute
    final = middle + "%s\n</section>\n"
    returned = final %content
    return returned
    
#Definición de article (html5)
#Se incluye dentro de <section></section>
def article(content, atribute):
    start = "\n<article %s>\n"
    middle = start %atribute
    final = middle + "%s\n</article>\n"
    returned = final %content
    return returned
    
#Definición de aside (columna de texto al lado derecho html5)
def aside(content, atribute):
    start = "\n<aside %s>\n"
    middle = start %atribute
    final = middle + "%s\n</aside>\n"
    returned = final %content
    return returned
    
#Definición de footer (html5)
def footer(content, atribute):
    start = "\n<footer %s>\n"
    middle = start %atribute
    final = middle + "%s\n</footer>\n"
    returned = final %content
    return returned
    
#Definición de address (html5)
#Se incluye dentro de <footer></footer>
def address(content, atribute):
    start = "\n<adress %s>\n"
    middle = start %atribute
    final = middle + "%s\n</address>\n"
    returned = final %content
    return returned
    
#Definición de comentarios 
def comment(content):
    final = "\n<!-- %s -->\n"
    returned = final %content
    return returned
       
#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")
