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
    style.append("html { max-width 500px; max-height: 550px;}\n")
    style.append("body {margin 0px, padding: 0px; background: linear-gradient(blue, white);}\n")
    style.append("#header { margin 0px; padding: 0px; background: linear-gradient(blue, white); height: 80px; width: 100%; overflow: hidden; border-bottom: 1px solid #000000; color: red; text-shadow: 5px 5px 5px #000000;}\n")
    style.append("#footer { margin 0px; padding: 0px; height: 80px; width: 100%; overflow: hidden; border-top: 1px solid #000000;}\n")
    style.append(".textbox {width: 200px; height: 20px; border: 1px solid #000000; border-radius: 5px; box-shadow: 5px 5px 10px #888888;}\n")
    style.append("#div { margin 0px; padding: 0px;  width: 100%; height: 600px; }\n")
    style.append(".nav { margin 0px; padding: 0px; width: 100%; height: 20px; text-align: center; background: gray; border-bottom: 1px solid #000000;}\n")
    style.append("#button { width: 70px; height: 20px; float: left; border: 1px solid #000000; border-radius: 2px; box-shadow: 5px 5px 10px #888888; transform: translate(550%, 50%);}\n")
    style.append("#section1 { margin: 5px; padding: 5px; width: 500px; height: 100px; overflow: hidden; border: 1px solid #000000; text-align: center; border-radius: 5px; box-shadow: 10px 10px 5px #888888; transform: translate(35%, 0%);}\n")
    style.append("#section2 { margin: 5px; padding: 5px; width: 500px; height: 350px; overflow: hidden; border: 1px solid #000000; text-align: center; border-radius: 5px; box-shadow: 10px 10px 5px #888888; transform: translate(35%, 0%);}\n")
    
    allStyles = ""
    
    for i in range(len(style)):
        allStyles = allStyles + style[i]
        
        cssScripts = styles.style(allStyles, atrb.type_("text/css"))
        
        
        #Titulo y definición de estilos
        titlepage = headers.title("Ingreso datos usuario")
        
        scriptFiles = headers.script("", atrb.type_("text/javascript")+ atrb.src_("scripts/statpy.js"))
        
        #definición de head
        head = headers.head(titlepage + cssScripts + scriptFiles)
        

    #definición barra navegacion
    
    #elementos de header
    
    #header
    text = formatting.h1("Python Rules!","")
    header = body.header(text, atrb.id_("header") + atrb.style_(styles.text_align("center")))
    
    #nav
    nav = body.nav(" ", atrb.class_("nav"))
    
    
    #Section
    
    h1 = formatting.h1("Registro:", atrb.style_(styles.text_align("center")))
    
    ps1text = "Favor complete los siguientes campos con la informaci&oacute;n solicitada."
    ps1 = formatting.p(ps1text,atrb.style_(styles.text_align("justify") + styles.font_style("italic") + styles.font_size("15px")))

    ps2 = formatting.p("Nombre Usuario:", "")
    input1 = controls.input_(atrb.id_("nombre") + atrb.type_("text") + atrb.class_("textbox"))
    
    ps3 = formatting.p("E-mail:", "")
    input2 = controls.input_(atrb.id_("correo") + atrb.type_("email") + atrb.class_("textbox"))
    
    ps4 = formatting.p("Ingresar password:", "")
    input3 = controls.input_(atrb.id_("password1") + atrb.type_("password") + atrb.class_("textbox"))
    
    ps5 = formatting.p("Confirmar password:", "")
    input4 = controls.input_(atrb.id_("password2") + atrb.type_("password") + atrb.class_("textbox"))
    
    button = formatting.p(controls.button("Registrar", atrb.id_("button")), atrb.style_(styles.float_("center")))
    
    components = ps2 + input1 + ps3 + input2 + ps4 + input3 + ps5 + input4
    
    section1 = body.section(h1 + ps1, atrb.id_("section1"))
    section2 = body.section(components + button, atrb.id_("section2") + atrb.class_("boxes"))


    #Salto
    salto = formatting.br("")

    #Div
    div = body.div(salto + section1 + salto + section2 + salto , atrb.id_("div") + atrb.style_(styles.background("#FFFFFF") + styles.text_align("center")))
    
    
    #Footer
    footertext = formatting.span("Derechos reservados &copy 2016", atrb.id_("footertext") )
    footercont = formatting.br("") + footertext
    footer = body.footer(footercont, atrb.id_("footer") + atrb.style_(styles.text_align("center")))
    
    
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
    print_html.saveHtml(document, "index8")
