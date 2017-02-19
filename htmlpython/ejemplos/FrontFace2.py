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
    titlepage = headers.title("FrontFace for Python2")

    #Styles CSS
    style = []

    style.append("* {\n \t margin:0px;\n \t padding: 0px; \n \t} \n")
    style.append("#header {\n \t margin: auto;\n \t width: 500px; \n \t font-family: Arial;\n \t} \n")
    style.append("ul, ol {\n \t list-style: none;\n \t} \n")
    style.append(".nav > li {\n \t float: left; \n \t} \n")
    style.append(".nav li a {\n \t background-color:#000; \n \t color:#fff; \n \t text-decoration:none; \n \t padding: 10px 12px;\n \t display: block;\n \t} \n")
    style.append(".nav li a:hover {\n \t background-color: #434343;\n \t} \n")
    style.append(".nav li ul {\n \t display: none;\n \t position: absolute;\n \t min-width: 140px;\n \t} \n")
    style.append(".nav li:hover > ul {\n \t display: block; \n \t} \n")
    style.append(".nav li ul li {\n \t position: relative; \n \t} \n")
    style.append(".nav li ul li ul {\n \t right: -140px;\n \t top:0px; \n \t} \n")

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

    #Items Menu Principal
    item1 = listing.li(formatting.a("Inicio", "index3.html"),"")

    #Servicios:
    subitemA1 = listing.li(formatting.a("Sub1", ""),"")
    subitemA2 = listing.li(formatting.a("Sub2", ""),"")
    subitemA3 = listing.li(formatting.a("Sub3", ""),"")

    SubMenus = subitemA1 + subitemA2 + subitemA3
    Servicios = formatting.a("Servicios", "") + listing.ul(SubMenus,"")
    item2 = listing.li(Servicios,"")

    #Acerca de:
    subitemB1 = listing.li(formatting.a("Sub1", ""),"")
    subitemB2 = listing.li(formatting.a("Sub2", ""),"")

    subitemC1 = listing.li(formatting.a("Sub1", ""),"")
    subitemC2 = listing.li(formatting.a("Sub2", ""),"")
    subMenusC = subitemC1 + subitemC2

    subitemB3Menu = formatting.a("Sub3", "") + listing.ul(subMenusC,"")
    subitemB3 = listing.li(subitemB3Menu,"")

    SubMenusB = subitemB1 + subitemB2 + subitemB3
    Acercade = formatting.a("Acercade", "") + listing.ul(SubMenusB,"")
    item3 = listing.li(Acercade, "")

    item4 = listing.li(formatting.a("Contacto", ""), "")

    AllItems = item1 + item2 + item3 + item4

    #Definición Ul
    ulDefinition = listing.ul(AllItems, "class =\"nav\"")

    #Defincion Navigator
    div = body.div(ulDefinition, "id =\"header\"")

    #Definición header
    header = body.header(formatting.h1("Front Face for Python2", ""),"")

    #MezclaComponentes
    navheader = merger.mergeTwoComponents(header, div)

    images = image.img(atrb.src_("http://www.estudiantes.info/ciencias_naturales/images/lobo-solo.png"))
    finalbody = navheader + images

    bodyHTML = headers.body(finalbody,"")

    #html = headers.html5Tag(mergeHeadBody(head, body))
    atrbt = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atrbt)

    #Despliega en pantalla
    #print_html.printHtml(html)

    #imprime contenido en un archivo
    #print_html.saveHtml(html, "index2")

    return html

if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "index2")