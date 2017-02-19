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
    titlepage = headers.title("FrontFace for Python3")

    #Styles CSS
    style = []

    style.append("* {\n\t margin:0px;\n\t padding: 0px;\n\t} \n")
    style.append("#agrupar {\n\t width: 960px;\n\t margin: 15px auto;\n\t text-align: left;\n\t} \n")
    style.append("h1 {\n\t font: bold 20px verdana, sans-serif;\n\t text-align: center;\n\t}\n")
    style.append("h2 {\n\t font: bold 14px verdana, sans-serif;\n\t}\n")
    style.append("footer {\n\t display: block; \n\t}\n")
    style.append("#image {\n\t display: block; \n\t margin-left: auto; \n\t margin-right: auto; \n\t}\n")
    style.append("body {\n\t background: #999999; \n\t}\n")
    style.append("#cabecera {\n\t background: #FFFBB9; \n\t border: 1px solid #999999; \n\t padding: 20px; \n\t}\n")
    style.append("#menu {\n\t background: #CCCCCC; \n\t padding: 5px 15px; \n\t}\n")
    style.append("#menu li {\n\t display: inline-block; \n\t list-style: none; \n\t padding: 5px; \n\t}\n")
    style.append("#columna {\n\t float: left; \n\t width: 220px; \n\t margin: 20px 0px; \n\t background: #CCCCC;}\n")
    style.append("#seccion {\n\t float: left; \n\t width: 660px; \n\t margin: 20px; \n\t}\n")
    style.append("#pie {\n\t clear: both; \n\t text-align: center; \n\t padding: 20px; \n\t border-top: 2px solid #DDDDDD; \n\t}\n")
    style.append("div {\n\t width: 100px; \n\t margin: 20px; \n\t padding: 10px; \n\t border: 1px solid #000000; \n\t -moz-box-sizing: border-box; \n\t}\n")

    allStyles = ""

    for i in range(len(style)):
        allStyles = allStyles + style[i]

    style = styles.style(allStyles,"")

    #Definición de cabecera
    finalhead = merger.mergeTitleStyle(titlepage, style)

    #Definición de meta
    metachar = headers.metaCharset("iso-8859-1")
    metadesc = headers.metaDescription("Ejemplo HTML5")
    metakeyw = headers.metaKeywords("html5, css3")

    metaLine = metachar + metadesc + metakeyw
    finalhead = finalhead + metaLine

    #Definición de HTML
    #Cabecera:
    head = headers.head(finalhead)

    #Cuerpo

    #Items List
    item1 = listing.li(formatting.a("Principal", "index.html"), "")
    item2 = listing.li("Fotos","")
    item3 = listing.li("Videos","")
    item4 = listing.li("Contacto","")

    AllItems = item1 + item2 + item3 + item4

    #Definición Ul
    ulDefinition = listing.ul(AllItems, "")

    #Defincion Navigator
    navigator = body.nav(ulDefinition, "id = \"menu\"")

    #Definición header
    header = body.header(formatting.h1("Front Face for Python3", ""), "id = \"cabecera\"")

    myFooter = body.footer("Derechos reservados &copy 2016", "id = \"pie\"")
    headerArt = formatting.h1("Titulo1", "")
    imgsource = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Tizian_-_Danae_receiving_the_Golden_Rain_-_Prado.jpg/800px-Tizian_-_Danae_receiving_the_Golden_Rain_-_Prado.jpg"
    image2 = image.img(atrb.src_(imgsource))

    artic = headerArt + image2 + myFooter
    myArticle = body.article(artic, "")

    mySection1 = body.section("hola", "id = \"seccion\"")
    myAside = body.aside(formatting.a("hola", "index4.html"), "id = \"columna\"")


    AllDiv = header + navigator + mySection1 + myAside + myArticle
    #Definición del div
    div = body.div(AllDiv, "id = \"agrupar\"")
    bodyHTML = div

    #html = headers.html5Tag(mergeHeadBody(head, body))
    atrbt = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atrbt)

    #Despliega en pantalla
    #print_html.printHtml(html)

    #imprime contenido en un archivo
    #print_html.saveHtml(html, "index3")
    return html

if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "index3")