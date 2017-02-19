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
    titlepage = headers.title("FrontFace for Python5")

    #Styles CSS
    style = []

    style.append("head {\n\t background: #DDDDDD;\n\t} \n")
    style.append("body {\n\t text-align: center;\n\t background: #DDDCCC;\n\t} \n")
    style.append("div {\n\t background: #CCCCCC;\n\t} \n")
    style.append("img {\n\t border: 2px solid #000000;\n\t} \n")
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

    scripts = headers.script(allScript, atrb.type_("text/javascript")+ atrb.src_("script.js"))

    #Definición de cabecera
    finalhead = merger.mergeThreeComponents(titlepage, style, scripts)

    #Definición de HTML
    #Cabecera:
    head = headers.head(finalhead)

    #Cuerpo

    firstLine = formatting.p("Hacer Click", "")
    secondLine = formatting.p("No se puede hacer click", "")
    divContent  = firstLine + secondLine
    div = body.div(divContent, atrb.id_("principal"))
    comentario = body.comment("Hola esto es un simple comentario")


    videoatributes = atrb.id_("medio") + atrb.width_("720") + atrb.height_("400") + atrb.preload_("metadata") + atrb.controls_() + atrb.loop_() + atrb.poster_("http://minkbooks.com/content/poster.jpg") 
    source1 = multimedia.source("http://phyc.net/gallery2/m/25891-3/Chuck+G_4-5-2014-1.mp4","")
    source2 = multimedia.source("http://phyc.net/gallery2/m/25891-3/Chuck+G_4-5-2014-1.mp4","")

    video1 = multimedia.video(source1 + source2, videoatributes)
    button1 = controls.button("Reproducir", atrb.type_("button") + atrb.width_("500") + atrb.id_("reproducir"))
    div1 = body.div(button1, atrb.id_("botones"))
    divA = body.div("",atrb.id_("progreso"))
    div2 = body.div(divA, atrb.id_("barra"))
    div3 = body.div("", atrb.style_("clear: both"))
    nav1 = body.nav(comentario + div1 + div2 + div3, "")
    atrbute = atrb.id_("busqueda") + atrb.type_("search") + atrb.name_("busqueda") + atrb.form_("formulario")
    input1= controls.input_(atrbute)
    nav2 = body.nav(input1, "")
    section1 = body.section(video1 + nav1, atrb.id_("reproductor"))

    input2 = controls.input_(atrb.type_("text") + atrb.name_("nombre") + atrb.id_("nombre"))
    input3 = controls.input_(atrb.type_("submit") + atrb.value_("Enviar"))
    atrbform = atrb.name_("formulario") + atrb.id_("formulario") + atrb.method_("get")
    form1 = controls.form(input2 + input3, atrbform)

    htmlImagen ="http://fravega.vteximg.com.br/arquivos/ids/287736-1000-1000/780642_1.jpg"
    imagen2 = image.img(atrb.src_(htmlImagen) + atrb.width_("100") + atrb.height_("100"))
    section3 =  body.section(imagen2, "")

    section2 = body.section(form1, "")
    break_ = formatting.br("")

    allbodyComponents = div + nav2 + section1 + break_ + section2 + break_ +section3

    bodyHTML = headers.body(allbodyComponents,"")

    #html = headers.html5Tag(mergeHeadBody(head, body))
    atrbt = atrb.lang_("es")
    html = headers.html(merger.mergeHeadBody(head, bodyHTML), atrbt)

    #Despliega en pantalla
    #print_html.printHtml(html)

    #imprime contenido en un archivo
    #print_html.saveHtml(html, "index5")

    return html

if __name__ == '__main__':
    document = html()
    print_html.printHtml(document)
    print_html.saveHtml(document, "index5")