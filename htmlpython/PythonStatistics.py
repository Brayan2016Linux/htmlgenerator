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

    style.append("* { margin:0px; padding: 0px;} \n")
    style.append("p { font-size: 12px;} \n")
    style.append("h1 h2 { font-size: 15px;} \n")
    style.append("body {background-color: #F5DEB3; overflow: hidden; height: 100px}")
    style.append("#header {background-color: #CD853F; height: 80px; overflow: hidden; border-bottom: 2px solid #000000;}\n")
    style.append("#headtext {color: #FFFFFF; font: bold; font-size: 15px;}\n")
    style.append("#imgdiv { text-align: left; float: left;}\n")
    style.append("#inputdiv {text-align: right; float:right; font-style: italic;}\n")
    style.append("#headerdiv {display: inline-block;}\n")
    style.append("#column {overflow:hidden; float:right; height: 500px; width: 300px; text-align:right}\n")
    style.append("#section {overflow:hidden;  height: 500px; width: 500px;}\n")
    style.append(".boxeshead { display: inline-block; margin:0px; padding: 2px;}\n")
    style.append(".boxes {clear: both; display: inline-block; margin:1px; padding: 2px; height: 100px; width: 200px;}\n")
    style.append(".input{ border-radius: 0px; border: none; height: 20px; }\n")
    style.append("#footertext {height: 500px vertical-align: middle; color: #CD853F; }\n")
    style.append("#footer {text-align: center; padding: 20px; border-top: 2px solid #000000; display: block; overflow: hidden; font-style: italic; color: #FFFFFF;}\n")
    style.append("#login { background-color: #8B4513; border: 1px solid #8B4513; width: 100px; height: 22px; padding: 0px; font: bold; color: #FFFFFF; }\n")
    style.append(".register {background-color: #006400; height: 30px; width: 100px; color: #FFFFFF; border-radius: 50px;}\n")
    style.append("#nav {background-color: #F5DEB3; height: 20px; width: 100%; color: #FFFFFF; border-bottom: 2px solid #000000;}\n")
    
    allStyles = ""
    
    for i in range(len(style)):
        allStyles = allStyles + style[i]
        
        cssScripts = styles.style(allStyles, atrb.type_("text/css"))
        
        
        #Titulo y definición de estilos
        titlepage = headers.title("Estad&iacutestica con Python")
        
        scriptFiles = headers.script("", atrb.type_("text/javascript")+ atrb.src_("scripts/statpy.js"))
        
        #definición de head
        head = headers.head(titlepage + cssScripts + scriptFiles)
        

    #definición barra navegacion
    
    #elementos de header
    #Image
    imageatrb = atrb.id_("headimage") + atrb.src_("images/head.png") + atrb.title_("Hola")
    headimage = image.img(imageatrb)
    imgdiv = body.div(headimage, atrb.id_("imgdiv") + atrb.class_("boxeshead"))
    
    #UserInput
    textoU = formatting.span("Usuario:", atrb.id_("headtext"))
    inputatrb = atrb.id_("usuario") + atrb.type_("text") + atrb.maxlength_("20") + atrb.class_("input")
    inputU = controls.input_(inputatrb)
    
    #PassInput
    textoP = formatting.span("Password:", atrb.id_("headtext"))
    inputatrb2 = atrb.id_("password") + atrb.type_("password") + atrb.maxlength_("10") + atrb.class_("input")
    inputP = controls.input_(inputatrb2)
    
    #ButtonLogin
    inputatrb3 = atrb.id_("login") + atrb.type_("submit")
    submit = controls.button("Login", inputatrb3)
    
    space = formatting.span(" ","")
    headercont = textoU + inputU + space + textoP + inputP + space + submit
    inputdiv = body.div(headercont, atrb.id_("inputdiv") + atrb.class_("boxeshead"))
    
    #header
    header = body.header(imgdiv + inputdiv, atrb.id_("header"))
    
    #nav
    nav = body.nav("", atrb.id_("nav"))
    
    
    #Section
    
    h1 = formatting.h1("PythonStatistics", atrb.style_(styles.text_align("center")))
    
    ps1text = """Python Statistics es un proyecto experimental 
de integraci&oacute;n desarrollo web con 
an&aacute;lisis de datos descriptivos, 
inferenciales y modelaje tanto en Machine 
Learning, Big Data, as&iacute; como Bussiness Intelligence"""

    ps1 = formatting.p(ps1text,atrb.style_(styles.text_align("justify")))

    section1 = body.section(h1 + ps1, atrb.id_("section") + atrb.class_("boxes"))

    #Aside
    h2 = formatting.h3("Reg&iacute;strese", atrb.style_(styles.text_align("center")))
    psa = """Para acceder a nuestros servicios debe crear una cuenta, es gratis,
favor leer nuestros t&eacute;rminos y condiciones, y aprobarlos al final de su registro.
Aseguramos completa confidencialidad de sus datos. """
    ahref = formatting.a("T&eacute;rminos y Condiciones.", "")
    finaltext = h2 + formatting.p(psa + ahref, atrb.style_(styles.text_align("justify")))

    textobutton = formatting.span("Sign up", atrb.font_(styles.face("verdana")))
    asidebutton = controls.button(textobutton, atrb.class_("register") + atrb.style_(styles.text_align("center")))
    salto = formatting.br("")

    aside = body.aside(finaltext + salto + asidebutton , atrb.id_("column") + atrb.class_("boxes"))

    #Div
    div = body.div(formatting.span(section1  + aside,""), atrb.style_(styles.background("#FFFFFF") + styles.overflow("hidden")))
    
    
    #Footer
    footerimage = image.img(atrb.id_("footerimage") + atrb.src_("images/footer.png"))
    footertext = formatting.span("Derechos reservados &copy 2016", atrb.id_("footertext"))
    footercont = footerimage + formatting.br("") + footertext
    footer = body.footer(footercont, atrb.id_("footer"))
    
    
    #body
    allbodyComponents = header + nav + div + footer
    bodyHTML = headers.body(allbodyComponents, "")
    
    #Definición doctype y html (preprocesadores)
    doctype = headers.doctype("")
    atribute = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atribute)
    
    #documento
    document = doctype + html

    #Despliega en pantalla
    #print_html.printHtml(document)

    #imprime contenido en un archivo para pruebas
    #print_html.saveHtml(document, "statpy")

    #imprime linea por linea:
    #read_html.printreadHtml("statpy.html")

    return document
    
if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "statpy")
