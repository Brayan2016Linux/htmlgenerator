#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Formato textos

#Definición del enmarcado h1
def h1(content, atribute):
    start = "<h1 %s>"
    middle = start %atribute
    final = middle + "%s</h1>"
    returned = final %content
    return returned
    
#Definición del enmarcado h2
def h2(content, atribute):
    start = "<h2 %s>"
    middle = start %atribute
    final = middle + "%s</h2>"
    returned = final %content
    return returned
    
#Definición del enmarcado h3
def h3(content, atribute):
    start = "<h3 %s>"
    middle = start %atribute
    final = middle + "%s</h3>"
    returned = final %content
    return returned
    
#Definición del enmarcado h4
def h4(content, atribute):
    start = "<h4 %s>"
    middle = start %atribute
    final = middle + "%s</h4>"
    returned = final %content
    return returned
    
#Definición del enmarcado h5
def h5(content, atribute):
    start = "<h5 %s>"
    middle = start %atribute
    final = middle + "%s</h5>"
    returned = final %content
    return returned
    
#Definición del enmarcado h6
def h6(content, atribute):
    start = "<h6 %s>"
    middle = start %atribute
    final = middle + "%s</h6>"
    returned = final %content
    return returned
    
#Bloque de párrafos
def p(content, atribute):
    start = "\n<p %s>\n"
    middle = start %atribute
    final = middle + "%s\n</p>\n"
    returned = final %content
    return returned
    
#Basefont
def basefont(content, atribute):
    start = "\n<basefont %s>\n"
    middle = start %atribute
    final = middle + "%s\n</basefont>\n"
    returned = final %content
    return returned
    
#Bloque de entrecomillado
#Atributo cite = "url"
def blockquote(content, atribute):
    start = "<blockquote %s>"
    middle = start %atribute
    final = middle + "%s</blockquote>"
    returned = final %content
    return returned
    
#Bloque de resaltado HTML5
def mark(content):
    final = "<mark>%s</mark>"
    returned = final %content
    return returned
    
#Bloque de enfasis antiguo <i> HTML5
def em(content):
    final = "<em>%s</em>"
    returned = final %content
    return returned
    
#Bloque de importancia HTML5
def strong(content):
    final = "<strong>%s</strong>"
    returned = final %content
    return returned
    
#Bloque de ejemplos de codigo HTML5
def code(content):
    final = "<code>%s</code>"
    returned = final %content
    return returned
    
#Bloque de salida de computadora HTML5
def samp(content):
    final = "<samp>%s</samp>"
    returned = final %content
    return returned
    
#Bloque de input del teclado HTML5
def kbd(content):
    final = "<kbd>%s</kbd>"
    returned = final %content
    return returned
    
#Bloque de variable HTML5
def var(content):
    final = "<var>%s</var>"
    returned = final %content
    return returned
    
#Bloque de variable HTML5
def dfn(content):
    final = "<dfn>%s</dfn>"
    returned = final %content
    return returned
    
#Bloque de negrita -en desuso-
def b(content):
    final = "<b>%s</b>"
    returned = final %content
    return returned
    
#Bloque de cursiva -en desuso-
def i(content):
    final = "<i>%s</i>"
    returned = final %content
    return returned
    
#Bloque de subrayado -en desuso-
def u(content):
    final = "<u>%s</u>"
    returned = final %content
    return returned
    
#Bloque de disminuir tamaño HTML5
def small(content):
    final = "<small>%s</small>"
    returned = final %content
    return returned
    
#Bloque de resaltado de titulos de libros, películas, etc HTML5
def cite(content):
    final = "<cite>%s</cite>"
    returned = final %content
    return returned
    
#Bloque salto de párrafo
def br(atribute):
    final = "<br %s></br>"
    returned = final %atribute
    return returned
    
#Bloque salto de temático: align left/center/right noshade size <>px width <>px
def hr(atribute):
    final = "<hr %s></hr>"
    returned = final %atribute
    return returned

    
#Referencia agrupar elementos en líneas cortas HTML5
def span(content, atribute):
    start = "\n<span %s>\n"
    middle = start %atribute
    final = middle + "%s\n</span>\n"
    returned = final %content
    return returned
    
#Preformateado Courier
def pre(content, atribute):
    start = "\n<pre %s>\n"
    middle = start %atribute
    final = middle + "%s\n</pre>\n"
    returned = final %content
    return returned
    
#Preformateado tachado
def strike(content, atribute):
    start = "\n<strike %s>\n"
    middle = start %atribute
    final = middle + "%s\n</strike>\n"
    returned = final %content
    return returned
    
#Preformateado agrandar
def big(content, atribute):
    start = "\n<big %s>\n"
    middle = start %atribute
    final = middle + "%s\n</big>\n"
    returned = final %content
    return returned
    
#Formateado en forma de Maquina de Escribir
def tt(content, atribute):
    start = "\n<tt %s>\n"
    middle = start %atribute
    final = middle + "%s\n</tt>\n"
    returned = final %content
    return returned
    
#Formateado superindice
def sup(content, atribute):
    start = "\n<sup %s>\n"
    middle = start %atribute
    final = middle + "%s\n</sup>\n"
    returned = final %content
    return returned
    
#Formateado subindice
def sub(content, atribute):
    start = "\n<sub %s>\n"
    middle = start %atribute
    final = middle + "%s\n</sub>\n"
    returned = final %content
    return returned
    
#Referencia a un html externo
#Admite url y href
#Admite #<marca> enlace interno 
#Salto: <a href="#marca">texto</a> Destino: <a name="marca"></a>
#Correo: <a href=mailto:correo>texto</a>
def a(content, atribute):
    start = "\n<a %s>\n"
    middle = start %atribute
    final = middle + "%s\n</a>\n"
    returned = final %content
    return returned
    
#formateo de fecha date: yyyy-MM-dd  HTML5
def time(content, date):
    start_a = "<time datetime=\"%s\" pubdate>"
    middle_a = start_a %date
    final_a = middle_a + "%s</time>\n"
    returned_a = final_a %content
    return returned_a

#Para ejecución directa sin importacion
if __name__ == "__main__":
        print("You should import headers into your main proyect.")
