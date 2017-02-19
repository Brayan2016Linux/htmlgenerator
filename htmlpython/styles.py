#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Formato de estilos CSS


#Definición del tipo de estilos para CSS
def style(content, atribute):
    start = "\n<style %s>\n"
    middle = start %atribute
    final = middle + "%s\n</style>\n"
    returned = final  %content
    return returned

#Definición del identificador del estilo
# #nombre { ... }
# <nombre>[atributo^ = "valor"] : para quienes tienen atributo valor al principio
# <nombre>[atributo$ = "valor"] : para quienes tienen atributo valor al final
# <nombre>[atributo* = "valor"] : para quienes tienen atributo valor
# <nombre>:hover{ ... }  cambia cuando el ratón pasa por encima
# <nombre>:nth-last-child{ ... }  cambia apartir del n-esimo elemento de <nombre>
# <nombre>:last-child{ ... }  cambia el ultimo elemento de <nombre>
# <nombre>:checked{ ... }  cambia el elemento seleccionado de <nombre>
# <nombre>:empty{ ... }  cambia los elementos vacios de <nombre>
# <nombre>:not([atributo*="valor"]){ ... }  no cambia los elementos de <nombre> segun que cumplen "valor"
# <nombre>:first-letter{ ... }  cambia la primera letra de  <nombre>
# <nombre>:selection{ ... }  cambia  <nombre> es seleccionado
def styleDefinition(identificator, content):
    startDefinition = "\n" + identificator + " { %s"
    finalDefinition = startDefinition %content
    returnedDefinition = finalDefinition + "}\n"
    return returnedDefinition
    
#Definición de los atributos dentro de <identificador>{...}

#text-align: right, left, center
def text_align(atribute):
    start = "text-align: %s; "
    final = start %atribute
    return final
    
#text-decoration: atribute none
def text_decoration(atribute):
    start = "text-decoration: %s; "
    final = start %atribute
    return final
    
#display: 
#Lista atributos: block, inline, none, inline-block, list-item
#compact, run-in, table, inline-table, table-caption, etc
def display(atribute):
    start = "display: %s; "
    final = start %atribute
    return final
    
#width: integer px
def width(atribute):
    start = "width: %s; "
    final = start %atribute
    return final
    
#max-height: integer px initial inherit
def height(atribute):
    start = "height: %s; "
    final = start %atribute
    return final
    
#max-width: integer px  initial inherit
def max_width(atribute):
    start = "max-width: %s; "
    final = start %atribute
    return final

#max-height: integer px initial inherit
def max_height(atribute):
    start = "max-heigth: %s; "
    final = start %atribute
    return final
    
#min-width: integer px  initial inherit
def min_width(atribute):
    start = "min-width: %s; "
    final = start %atribute
    return final

#min-height: integer px initial inherit
def min_height(atribute):
    start = "min-height: %s; "
    final = start %atribute
    return final
    
#margin: atribute px [auto]
def margin(atribute):
    start = "margin: %s; "
    final = start %atribute
    return final
    
#margin-top: atribute px
def margin_top(atribute):
    start = "margin-top: %s; "
    final = start %atribute
    return final
    
#margin-right: atribute px
def margin_right(atribute):
    start = "margin-right: %s; "
    final = start %atribute
    return final
    
#margin-botton: atribute px
def margin_botton(atribute):
    start = "margin-botton: %s; "
    final = start %atribute
    return final
    
#margin-left: atribute px
def margin_left(atribute):
    start = "margin-left: %s; "
    final = start %atribute
    return final
    
#padding: atribute px
def padding(atribute):
    start = "padding: %s; "
    final = start %atribute
    return final
    
#border: atribute px solid #<color_number>
def border(atribute):
    start = "border: %s; "
    final = start %atribute
    return final
    
#background: #<color_number>
#background: atributo especial-linear-gradient(top, #<color1>, #<color2>)
#background: radiant-gradient(center, circle, #<color> <int>%, #<color> <int>%)

def background(atribute):
    start = "background: %s; "
    final = start %atribute
    return final
    
#float_: none, left, right, initial, inherit
def float_(atribute):
    start = "font: %s; "
    final = start %atribute
    return final
    
#font: <bold, italic> size px type1, type2
def font(atribute):
    start = "font: %s; "
    final = start %atribute
    return final
    
#box-shadow: rgb(V1, V2, V3)  <value>px <value>px <value>px <value>px inset #color
def box_shadow(atribute):
    start = "box-shadow: %s; "
    final = start %atribute
    return final
    
#text-shadow: rgb(V1, V2, V3) <value>px <value>px <value>px
#text-shadow: rgba(V1, V2, V3) <value>px <value>px <value>px
def text_shadow(atribute):
    start = "text-shadow: %s; "
    final = start %atribute
    return final
    
#color: hsla(<int>, <int>%, <int>%, 0.<value>)
def color(atribute):
    start = "color: %s; "
    final = start %atribute
    return final

#Outline y outline-offset  
#outline: <int>px dashed #<color>
def outline(atribute):
    start = "outline: %s; "
    final = start %atribute
    return final
    
#outline-offset: <int>px
def outline_offset(atribute):
    start = "outline-offset: %s; "
    final = start %atribute
    return final
    
#FontFace
def font_face(name, type_font):
    NewFontName = "font-family: \'" + name + "\'; "
    sourceFont = "src: url(\'" + type_font+ "\'); "
    content = NewFontName + sourceFont
    returned = styleDefinition("@font-face", content)
    return returned
    
#Media  screen/print and  (max-width/min-width: <>px)
def media(media, type_width, value_width, content):
    start = "@media %s and (%s-width: %spx) {\n"
    middle = start %(media, type_width, value_width)
    final = middle + "%s\n }"
    returned = final %content
    return returned

#list-style: none
def list_style(atribute):
    start = "list-style: %s; "
    final = start %atribute
    return final

#Overflow, cuando algo sobrepasa la ventana: por default es visible
#overflow: visible, hidden, scroll, auto
def overflow(atribute):
    start = "overflow: %s; "
    final = start %atribute
    return final
    
#overflow-x: visible, hidden, scroll, auto, initial, inherit
def overflow_x(atribute):
    start = "overflow-x: %s; "
    final = start %atribute
    return final
    
#overflow-y: visible, hidden, scroll, auto, initial, inherit
def overflow_y(atribute):
    start = "overflow-y: %s; "
    final = start %atribute
    return final
    
#Border-top:  <>px solid #<color>;
def border_top(atribute):
    start = "border-top: %s; "
    final = start %atribute
    return final
    
#Border-bottom: <>px solid #<color>;
def border_bottom(atribute):
    start = "border-top: %s; "
    final = start %atribute
    return final
    
#Border-left:  <>px solid #<color>;
def border_left(atribute):
    start = "border-left: %s; "
    final = start %atribute
    return final
    
#Border-bottom: <>px solid #<color>;
def border_right(atribute):
    start = "border-right: %s; "
    final = start %atribute
    return final
    
#Font-size: <>px;
def font_size(atribute):
    start = "font-size: %s; "
    final = start %atribute
    return final
    
#Font-style: bold italic underline normal;
def font_style(atribute):
    start = "font-style: %s; "
    final = start %atribute
    return final
    
#Font-weight: normal;
def font_weight(atribute):
    start = "font-weight: %s; "
    final = start %atribute
    return final
    
#Font-style: name of font;
def font_family(atribute):
    start = "font-family: %s; "
    final = start %atribute
    return final
    
#face: name of font-family;, se utiliza con font
def face(atribute):
    start = "face: %s; "
    final = start %atribute
    return final
    
#Position: static, absolute, fixed, relative, initial, inherit
def position(atribute):
    start = "outline-offset: %s; "
    final = start %atribute
    return final
    
#Clear: both
def clear(atribute):
    start = "clear: %s; "
    final = start %atribute
    return final
    
#opacity: value   0< value <1
def opacity(atribute):
    start = "opacity: %s; "
    final = start %atribute
    return final
   
#rgba: (red, green, blue, alpha)  0 < alpha < 1
def rgba(red, green, blue, alpha):
    start = "rgba(%s %s %s %s); "
    final = start %(red, green, blue, alpha)
    return final

#hsla: (hue, saturation, light, alpha)  0 < alpha < 1
def hsla(hue, saturation, light, alpha):
    start = "hsla(%s %s %s %s); "
    final = start %(hue, saturation, light, alpha)
    return final

#hsla: (hue, saturation, light)
def hsl(hue, saturation, light):
    start = "hsla: (%s %s %s); "
    final = start %(hue, saturation, light)
    return final
    
#border-radius: (top-left, top-right , bottom-left, botton-right)
def border_radius(tl, tr, bl, br):
    start = "border-radius: %spx %spx %spx %spx; "
    final = start %(tl, tr, bl, br)
    return final
    
#border-radius: (top-left, top-right , bottom-left, botton-right)
def border_width(tl, tr, bl, br):
    start = "border-width: %spx %spx %spx %spx; "
    final = start %(tl, tr, bl, br)
    return final

#url: (object)
def url(atribute):
    start = "url(%s); "
    final = start %atribute
    return final
    
#background-image: url(object)
def background_image(atribute):
    start = "background-image: %s; "
    final = start %atribute
    return final
    
#background-position: atribute
def background_position(atribute):
    start = "background-position: %s; "
    final = start %atribute
    return final
    
#background-repeat: no-repeat/repeat
def background_position(atribute):
    start = "background-repeat: %s; "
    final = start %atribute
    return final
    
#background-color: <color>
def background_color(atribute):
    start = "background-color: %s; "
    final = start %atribute
    return final
    
#border-image: atribute url() percent% no-repeat/repeat
def border_image(atribute):
    start = "border-image: %s; "
    final = start %atribute
    return final

#Atributos especiales
    
#Lista:
#atribute: box-sizing value: border-box 
#atribute: border-radius: <all> px [<top-right>px <top-left>px <botton-left>px <botton-right>px]  
#atribute: border-image: url("<image>.png") <int> stretch
#atribute: transform: scale(<int>) scaleX(<int>) scaleY(<int>)
#atribute: transform: scale(<intX>, intY>)
#atribute: transform: rotate(<int>deg)
#atribute: transform: skew(<int>deg)
#atribute: transform: translate(<int>px) translateX(<int>px) translateY(<int>px)
#atribute: transition: -atributoespecial-transform ls ease-in-out 0.5s;
# ease, linear, ease-in, ease-out, ease-in-out
#atribute: column-count: <numero columnas>
#atribute: column-width: <ancho columnas>px
#atribute: column-gap: <espacio entre columnas>px

#Mozilla:
def moz(atribute, value):
    start = "-moz-%s: "
    middle = start %atribute
    final = middle + "%s;"
    returned = final %value
    return returned
    
#Safari - Chrome:
def webkit(atribute, value):
    start = "-webkit-%s: "
    middle = start %atribute
    final = middle + "%s;"
    returned = final %value
    return returned
    
#Opera:
def o(atribute, value):
    start = "-o-%s: "
    middle = start %atribute
    final = middle + "%s;"
    returned = final %value
    return returned

#Konqueror:
def khtml(atribute, value):
    start = "-khtml-%s: "
    middle = start %atribute
    final = middle + "%s;"
    returned = final %value
    return returned  
    
#Internet Explorer:
def ms(atribute, value):
    start = "-ms-%s: "
    middle = start %atribute
    final = middle + "%s;"
    returned = final %value
    return returned 
    
#Google Chrome:
def chrome(atribute, value):
    start = "-chrome-%s: "
    middle = start %atribute
    final = middle + "%s;"
    returned = final %value
    return returned 
    
#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")