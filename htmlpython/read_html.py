#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Print_HTML
#Despliega en pantalla o crea documento html

#leer documento html en una lista
def readHtml(content):
    try:
        files = open(content, "r")
        document = files.read()
        files.close()
    except:
        print("Error reading your file: ", name)
    return document

#impresion del documento en lineas
def printreadHtml(name):
    try:
        files = open(name, "r")
        document = files.read()
        print (document)
    except:
        print("Error displaying your file: ", name)
    return False

#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")