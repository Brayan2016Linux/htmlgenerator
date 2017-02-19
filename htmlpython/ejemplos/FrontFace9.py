#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: PythonStatistics


import headers
import formatting
import styles
import merger
import print_html
import body
import listing
import image
import atrb
import controls
import read_html


def html():
    #Definición de estilos
    #Styles CSS
    style = []

    style.append("* { margin 0px; padding: 0px;}\n")
    
    allStyles = ""
    
    for i in range(len(style)):
        allStyles = allStyles + style[i]
        
        cssScripts = styles.style(allStyles, atrb.type_("text/css"))
        
        
        #Titulo y definición de estilos
        titlepage = headers.title("Canvas")
        
        
        #definición de head
        head = headers.head(titlepage + cssScripts)
        

    #definición barra navegacion
    
    #elementos de header
    
    #header
    text = formatting.h1("Canvas!","")
    header = body.header(text, atrb.id_("header") + atrb.style_(styles.text_align("center")))
    
    #Canvas
    canvasatrb = atrb.id_("myCanvas") + atrb.width_("300") + atrb.height_("150") + atrb.style_(styles.border("1px solid #d3d3d3;"))
    canvas = image.canvas("", canvasatrb)

    #SCript
    scriptlist = []
    
    scriptlist.append("var c = document.getElementById(\"myCanvas\");\n")
    scriptlist.append("var ctx = c.getContext(\"2d\");\n")
    scriptlist.append("ctx.beginPath();\n")
    scriptlist.append("ctx.moveTo(20,20);\n")
    scriptlist.append("ctx.lineTo(20,100);\n")
    scriptlist.append("ctx.lineTo(70,100);\n")
    scriptlist.append("ctx.strokeStyle=\"red\";\n")
    scriptlist.append("ctx.stroke();\n")

    script = ""    
    for i in range(len(scriptlist)):
        script = script + scriptlist[i]
        
    myScript = headers.script(script, "")
    
    #body
    allbodyComponents = canvas + myScript
    bodyHTML = headers.body(allbodyComponents, "")
    
    #Definición doctype y html (preprocesadores)
    doctype = headers.doctype("")
    atribute = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atribute)
    
    #documento
    document = doctype + html

    

    return document
    
if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "index9")
