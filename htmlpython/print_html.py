#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Print_HTML
#Despliega en pantalla o crea documento html

#impresión del html en consola
def printHtml(content):
    print(content)

#impresion del documento html
def saveHtml(content, name):
    try:
        namefile = name + ".html"
        fileHandler = open(namefile, "w")
        fileHandler.write(content)
        fileHandler.close()
    except:
        print("Error saving your file: ", name, ".html")
    return False
    
#impresion del documento css
def saveCss(content, name):
    try:
        namefile = name + ".css"
        fileHandler = open(namefile, "w")
        fileHandler.write(content)
        fileHandler.close()
    except:
        print("Error saving your file: ", name, ".css")
    return False
    
#impresion del documento js
def saveJs(content, name):
    try:
        namefile = name + ".js"
        fileHandler = open(namefile, "w")
        fileHandler.write(content)
        fileHandler.close()
    except:
        print("Error saving your file: ", name, ".js")
    return False

#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")