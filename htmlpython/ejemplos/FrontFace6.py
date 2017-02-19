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
    
    style.append("head {\n\t background: #DDDDDD;\n\t} \n")
    style.append("body {\n\t text-align: center;\n\t background: #DDDCCC;\n\t} \n")
    style.append("div {\n\t background: #CCCCCC;\n\t} \n")
    style.append("section {\n\t background: #EEEEEE;\n\t} \n")
    style.append("header, section, nav {\n\t display: block;\n\t} \n")
    style.append("nav {\n\t margin: 5px 0px;\n\t background: #999999 \n\t} \n")
    style.append("#reproducir {\n\t width: 100px;\n\t text-align: center;\n\t } \n")
    style.append("#principal {\n\t display: block; \n\t border: 1px solid #999999; \n\t padding: 15px; \n\t}\n")
    style.append("#reproductor {\n\t width: 720px; \n\t margin: 20px auto; \n\t -moz-border-radius: 5px; \n\t \n\t background: #999999;\n\t border: 1px solid #666666; \n\t}\n")
    style.append("#barra {\n\t positin: relative; \n\t float: left; \n\t width: 600px; \n\t \n\t height: 16px; \n\t padding: 2px; \n\t border: 1px solid #CCCCCC; \n\t background: #EEEEEE; \n\t}\n")
    style.append("#botones {\n\t float: left; \n\t width: 100px;\n\t  height: 20px; \n\t}\n")
    style.append("#progreso {\n\t position: absolute; \n\t width: 0px;\n\t  height: 16px; \n\t background: rgba(0,0,150,0.2); \n\t}\n")

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

    scripts = headers.script(allScript, atrb.type_("text/javascript")+ atrb.src_("script2.js"))

    #Definición de cabecera
    finalhead = merger.mergeThreeComponents(titlepage, style, scripts)

    #Definición de HTML
    #Cabecera:
    head = headers.head(finalhead)

    #Cuerpo
    message = "Su navegador no soporta el elemento"
    canvas = image.canvas(message, atrb.id_("lienzo") + atrb.width_("500") + atrb.height_("300"))
    section = body.section(canvas, atrb.id_("cajalienzo"))


    allbodyComponents = section 

    bodyHTML = headers.body(allbodyComponents,"")

    #html = headers.html5Tag(mergeHeadBody(head, body))
    atrbt = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atrbt)

    #Despliega en pantalla
    #print_html.printHtml(html)

    #imprime contenido en un archivo
    #print_html.saveHtml(html, "index6")

    return html

if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "index6")