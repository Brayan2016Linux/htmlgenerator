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
    titlepage = headers.title("FrontFace for Python")

    #Styles CSS
    style1 = "* { margin:0px; padding: 0px; } \n"
    style2 = "p { font-size: 20px; } \n"
    style3 = "nav { font-size: 20px; } \n"
    style4 = "div { font-size: 20px; } \n"

    allStyles = style1 + style2 + style3

    style = styles.style(allStyles, "")

    #Definición de cabecera
    finalhead = merger.mergeTitleStyle(titlepage, style)

    #Definición de HTML
    #Cabecera:
    head = headers.head(finalhead)

    #Cuerpo

    #Items List
    item1 = listing.li("Principal","")
    item2 = listing.li("Fotos","")
    item3 = listing.li("Videos","")
    item4 = listing.li("Contacto","")

    AllItems = item1 + item2 + item3 + item4

    #Definición Ul
    ulDefinition = listing.ul(formatting.span(AllItems,""),"")

    #Defincion Navigator
    navigator = body.nav(body.div(ulDefinition, ""),"")

    #Definición header
    header = body.header(formatting.h1("Front Face for Python", ""),"")

    #Definición de articulos
    #Articulo 1
    titulo11 = formatting.h1("Titulo mensaje1", "")
    titulo12 = formatting.h2("Subtitulo mensaje1", "")
    textop1 = formatting.p(formatting.time("publicado 16-11-2016", "2016-11-16"),"")
    message1 = merger.mergeThreeComponents(titulo11,titulo12,textop1)
    headerA1 = body.header(message1,"")
    textoA1 = "Este es el texto primer Mensaje"
    footerA1 = body.footer(formatting.p("Primer comentario",""),"")
    image1 = image.img(atrb.src_("http://www.estudiantes.info/ciencias_naturales/images/lobo-solo.png"))
    figcaption1 = body.figcaption("Esta es la imagen 1", "")
    figures = image1 + figcaption1
    figure = body.figure(figures, "")
    articuloTexto1 = headerA1 + textoA1 + footerA1 + figures
    articulo1 = body.article(articuloTexto1, "")

    #Articulo2
    titulo21 = formatting.h1("Titulo mensaje2", "")
    titulo22 = formatting.h2("Subtitulo mensaje2", "")
    textop2 = formatting.p("publicado 16-11-2016","")
    message2 = merger.mergeThreeComponents(titulo21,titulo22,textop2)
    headerA2 = body.header(message2,"")
    address2 = "index2.html"
    textoA2 = formatting.a("Este es el texto segundo Mensaje", address2)
    footerA2 = body.footer(formatting.p("Segundo comentario",""),"")
    articuloTexto2 = headerA2 + textoA2 + footerA2
    articulo2 = body.article(articuloTexto2, "")

    mergedArt = merger.mergeTwoComponents(articulo1, articulo2)

    #Definición sección
    mySection = body.section(mergedArt,"")

    #Definición de lado derecho
    bloque1= formatting.blockquote("texto numero 1", "")
    bloque2= formatting.blockquote("texto numero 2", "")
    myAside = body.aside(merger.mergeTwoComponents(bloque1, bloque2),"")

    #Definición del footer
    myFooter = body.footer(formatting.small("Derechos Reservados &copy 2016"),"")

    #MezclaComponentes
    navheader = merger.mergeTwoComponents(navigator, header)
    sectaside = merger.mergeTwoComponents(mySection, myAside)

    bodyHTML = headers.body(merger.mergeTwoComponents(navheader, sectaside),"")

    #html = headers.html5Tag(mergeHeadBody(head, body))
    atrbt = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atrbt)

    #Despliega en pantalla
    #print_html.printHtml(html)

    #imprime contenido en un archivo
    #print_html.saveHtml(html, "index")

    return html

if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "index1")