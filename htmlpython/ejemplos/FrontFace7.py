#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Muestra


import headers
import formatting
import styles
import merger
import print_html
import body
import listing
import image
import multimedia
import controls
import atrb

def html():
    #Titulo y definición de estilos
    titlepage = headers.title("FrontFace for Python6")

    #Styles CSS
    style = []

    style.append(".cajas {\r\t display: inline-block;\r\t margin: 10px;\r\t padding: 5px;\r\t border: 1px solid #999999;\r\t} \r")


    allStyles = ""

    for i in range(len(style)):
        allStyles = allStyles + style[i]

    style = styles.style(allStyles,"")

    #Script JavaScript
    script = []

    #funciones embebidas
    script.append("")

    allScript = ""

    for i in range(len(script)):
        allScript = allScript + script[i]

    scripts = headers.script(allScript, atrb.type_("text/javascript")+ atrb.src_("script3.js"))

    #Definición de cabecera
    finalhead = merger.mergeThreeComponents(titlepage, style, scripts)

    #Definición de HTML
    #Cabecera:
    head = headers.head(finalhead)

    #Cuerpo
    address = "http://phyc.net/gallery2/m/25891-3/Chuck+G_4-5-2014-1.mp4"
    source1 = multimedia.source(address, "")
    source2 = multimedia.source(address, "")
    video = multimedia.video(source1 + source2, atrb.id_("medio") + atrb.width_("483") + atrb.height_("272"))
    section1 = body.section(video, atrb.class_("cajas"))

    message = "Su navegador no soporta el elemento"
    canvas = image.canvas(message, atrb.id_("lienzo") + atrb.width_("483") + atrb.height_("272"))
    section2 = body.section(canvas, atrb.class_("cajas"))

    allbodyComponents = section1 + section2 

    bodyHTML = headers.body(allbodyComponents,"")

    #html = headers.html5Tag(mergeHeadBody(head, body))
    atrbt = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atrbt)

    #Despliega en pantalla
    #print_html.printHtml(html)

    #imprime contenido en un archivo
    #print_html.saveHtml(html, "index7")
    
    return html

if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "index7")
