#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Merger
#Mezcla componentes para la impresión final

#Mezcla Title - Styles
def mergeTitleStyle(title, style):
    mergingreturned = title +"\n"+ style
    return mergingreturned

#Mezcla Head-Body
def mergeHeadBody(head, body):
    mergingreturned = head + "\n" + body
    return mergingreturned
    
#Mezcla dosComponentes
def mergeTwoComponents(component1, component2):
    mergingreturned = component1 + "\n" + component2
    return mergingreturned
    
#Mezcla tresComponentes
def mergeThreeComponents(component1, component2, component3):
    mergingreturned = component1 + "\n" + component2 + "\n" + component3
    return mergingreturned
    
#Para ejecución directa sin importacion
if __name__ == "__main__":
        print("You should import headers into your main proyect.")
