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
import atrb

def html():
    #Titulo y definición de estilos
    titlepage = headers.title("FrontFace for Python4")

    #Styles CSS
    style = []

    style.append("body {\n\t text-align: center;\n\t} \n")
    style.append("#principal {\n\t display: block; \n\t #DDDDDD; \n\t background: #DDDDDD; \n\t border: 1px solid #999999; \n\t padding: 15px; \n\t}\n")
    style.append("#titulo {\n\t color: #999999; \n\t font: bold 36px verdana, sans-serif; \n\t text-shadow:rgb(0,0,150) 3px 3px 5px; \n \t}\n")

    allStyles = ""

    for i in range(len(style)):
        allStyles = allStyles + style[i]

    style = styles.style(allStyles,"")

    #Definición de cabecera
    finalhead = merger.mergeTitleStyle(titlepage, style)

    #Definición de HTML
    #Cabecera:
    head = headers.head(finalhead)

    #Cuerpo
    spann = formatting.span(formatting.a("Estilos CSS", "index5.html"), "id = \"titulo\"")

    #Definición header
    header = body.header(spann, "id = \"principal\"")

    bodyHTML = headers.body(header,"")

    #html = headers.html5Tag(mergeHeadBody(head, body))
    atrbt = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atrbt)

    #Despliega en pantalla
    #print_html.printHtml(html)

    #imprime contenido en un archivo
    #print_html.saveHtml(html, "index4")

    return html

if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "index4")