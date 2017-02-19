#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: atributos generales

#Definición de maxlength
def maxlength_(value):
    start = " maxlength =\"%s\""
    returned = start %value
    return returned

#Definición de action en especial para cgi dentro de form
def action_(value):
    start = " action =\"%s\""
    returned = start %value
    return returned

#Definición de lang
def lang_(value):
    start = " lang =\"%s\""
    returned = start %value
    return returned
    
#Definición de size
def size_(value):
    start = " size =\"%s\""
    returned = start %value
    return returned

#Definición de name
def name_(value):
    start = " name =\"%s\""
    returned = start %value
    return returned
    
#Definición de id
def id_(value):
    start = " id =\"%s\""
    returned = start %value
    return returned
    
#Definición de class
def class_(value):
    start = " class =\"%s\""
    returned = start %value
    return returned
    
#Definición de form se incluye dentro de input
def form_(value):
    start = " form =\"%s\""
    returned = start %value
    return returned
    
#Definición de method: "get", "post"
def method_(value):
    start = " method =\"%s\""
    returned = start %value
    return returned
    
#Definición de media: "screen/print and max/min-width <number>px"
def media_(value):
    start = " media =\"%s\""
    returned = start %value
    return returned
    
#Definición de autocomplete: "on", "off"
def autocomplete_(value):
    start = " autocomplete =\"%s\""
    returned = start %value
    return returned
    
#Definición de http-equiv
#Atributo: refresh, se usa dentro de <meta></meta>
def http_equiv_(value):
    start = " http-equiv =\"%s\""
    returned = start %value
    return returned

#Definición de content <int>, se usa dentro de <meta></meta>
def content_(value):
    start = " content =\"%s\""
    returned = start %value
    return returned
    
#Definición de url, se usa dentro de <meta></meta>
def url_(value):
    start = " url =\"%s\""
    returned = start %value
    return returned
  
#Definición de type text, submit, email, search, url, tel, number, range, date
#week, month, time, datetime, datetime-local, color, checkbox, radio, reset
#Viñetas de lista: circle, square, disk
def type_(value):
    start = " type =\"%s\""
    returned = start %value
    return returned
    
#Definición de type text/plain, text/css, etc. Se usa dentro de <form></form>
def enctype_(value):
    start = " enctype =\"%s\""
    returned = start %value
    return returned
    
#Definición de src
def src_(value):
    start = " src =\"%s\""
    returned = start %value
    return returned
    
#Definición de src
def href_(value):
    start = " href =\"%s\""
    returned = start %value
    return returned
    
#Definición de user_scalable
def user_scalable_(value):
    start = " user-scalable =\"%s\""
    returned = start %value
    return returned
    
#Definición de initial_scale
def initial_scale_(value):
    start = " initial-scale =\"%s\""
    returned = start %value
    return returned
    
#Definición de maximum_scale
def maximum_scale_(value):
    start = " maximum-scale =\"%s\""
    returned = start %value
    return returned

#Definición de minimum_scale
def minimum_scale_(value):
    start = " minimum-scale =\"%s\""
    returned = start %value
    return returned

#Definición de width
def width_(value):
    start = " width =\"%s\""
    returned = start %value
    return returned

#Definición de width
def height_(value):
    start = " height =\"%s\""
    returned = start %value
    return returned

#Definición de value, se incluye dentro de input
#Se incluye dentro de option
def value_(value):
    start = " value =\"%s\""
    returned = start %value
    return returned
    
#Definición de label, se incluye dentro de option
def label_(value):
    start = " label =\"%s\""
    returned = start %value
    return returned
    
#Definición de list, se incluye dentro de input
#Referencia una lista creada con <datalist>
def list_(value):
    start = " list =\"%s\""
    returned = start %value
    return returned
    
#Definición de min, se incluye dentro de input con type: "range" o "number"
def min_(value):
    start = " min =\"%s\""
    returned = start %value
    return returned
    
#Definición de max, se incluye dentro de input con type: "range" o "number"
def max_(value):
    start = " max =\"%s\""
    returned = start %value
    return returned
    
#Definición de step, se incluye dentro de input con type: "range" o "number"
def step_(value):
    start = " step =\"%s\""
    returned = start %value
    return returned
    
#Definición de cellspacing (espacio entre celdas dentro de <table></table>)
def cellspacing_(value):
    start = " cellspacing =\"%s\""
    returned = start %value
    return returned
    
#Definición de cellpadding (espacio entre bordes dentro de <table></table>)
def cellpadding_(value):
    start = " cellpadding =\"%s\""
    returned = start %value
    return returned
    
#Definición de colspan, mezcla de una celda en n columnas
def colspan_(value):
    start = " colspan =\"%s\""
    returned = start %value
    return returned
    
#Definición de rowspan, mezcla de una celda en n filas
def rowspan_(value):
    start = " rowspan =\"%s\""
    returned = start %value
    return returned
    
#Definición de cols, dentro de <textarea></textarea>
def cols_(value):
    start = " cols =\"%s\""
    returned = start %value
    return returned
    
#Definición de rows, dentro de <textarea></textarea>
def rowspan_(value):
    start = " rows =\"%s\""
    returned = start %value
    return returned
    
#Definición de style
def style_(value):
    start = " style =\"%s\""
    returned = start %value
    return returned
    
#Definición de align center right left
def align_(value):
    start = " align =\"%s\""
    returned = start %value
    return returned
    
#Definición de valign top bottom
def valign_(value):
    start = " valign =\"%s\""
    returned = start %value
    return returned
    
#Definición de style
def font_(value):
    start = " font =\"%s\""
    returned = start %value
    return returned
    
#Definición de poster se incluye dentro de video corresponde a una imagen
def poster_(value):
    start = " poster =\"%s\""
    returned = start %value
    return returned
    
#Definición de vspace
def vspace_(value):
    start = " vspace =\"%s\""
    returned = start %value
    return returned
    
#Definición de alt (texto alternativo)
def alt_(value):
    start = " alt =\"%s\""
    returned = start %value
    return returned
    
#Definición de vspace
def hspace_(value):
    start = " hspace =\"%s\""
    returned = start %value
    return returned
    
#Definición de title se incluye dentro de input
#En otros creará un titulo flotante
def title_(value):
    start = " title =\"%s\""
    returned = start %value
    return returned
    
#Definición de placeholder, se incluyen dentro de input con type:"search"
def placeholder_(value):
    start = " placeholder =\"%s\""
    returned = start %value
    return returned
    
#Definición de pattern se incluye dentro de input
#pattern = "[<characters allowed>]{<number of characters allowed}"
def pattern_(value):
    start = " title =\"%s\""
    returned = start %value
    return returned
    
#bgcolor= "#<color>"
def bgcolor_(value):
    start = " bgcolor =\"%s\""
    returned = start %value
    return returned
    
#frameborder= <int>/"no"
def frameborder_(value):
    start = " frameborder =\"%s\""
    returned = start %value
    return returned
    
#framespacing= "" espacio entre frames
def framespacing_(value):
    start = " framespacing =\"%s\""
    returned = start %value
    return returned
    
#marginwidth= "" ancho de un frame
def marginwidth_(value):
    start = " marginwidth =\"%s\""
    returned = start %value
    return returned
    
#marginheight= "" altura de un frame
def marginheight_(value):
    start = " marginheight =\"%s\""
    returned = start %value
    return returned
    
#scrolling= "" yes/no/auto
def scrolling_(value):
    start = " scrolling =\"%s\""
    returned = start %value
    return returned
    
#codebase= "" url
def codebase_(value):
    start = " codebase =\"%s\""
    returned = start %value
    return returned
    
#autostart= "true"
def autostart_(value):
    start = " autostart =\"%s\""
    returned = start %value
    return returned
    
#wrap= off/soft/hard
def wrap_(value):
    start = " wrap =\"%s\""
    returned = start %value
    return returned

#target: apunta a otro frame _blank (nuevo) _self (mismo frame) _top (pantalla completa)
def target_(value):
    start = " target =\"%s\""
    returned = start %value
    return returned
    
#noresize
def noresize_():
    start = " noresize"
    returned = start
    return returned
    
#disabled
def disabled_():
    start = " disabled"
    returned = start
    return returned

#readonly
def readonly_():
    start = " readonly"
    returned = start
    return returned
    
#noshade
def noshade_():
    start = " noshade"
    returned = start
    return returned
    
#nowrap
def nowrap_():
    start = " nowrap"
    returned = start
    return returned
    
#ismap
def ismap_():
    start = " ismap"
    returned = start
    return returned
    
#hidden "true"
def hidden_(value):
    start = " hidden =\"%s\""
    returned = start %value
    return returned
    
#shape default rect, circle, polygon se incluye dentro de <map></map>
def shape_(value):
    start = " shape =\"%s\""
    returned = start %value
    return returned
    
#usemap definición del nombre de mapa <map></map>
def usemap_(value):
    start = " usemap =\"#%s\""
    returned = start %value
    return returned
    
#coords (x1, y1, ... , xn, yn) / (x, y, radius) dentro de <map></map>
def coords_(value):
    start = " coords =\"%s\""
    returned = start %(X1, Y1, X2, Y2)
    return returned
    
#nohref
def nohref_():
    start = " nohref"
    returned = start
    return returned
    
#Definición de loop
def loop_():
    start = " loop"
    returned = start
    return returned
    
#Definición de preload: none, metadata, auto
def preload_(value):
    start = " preload =\"%s\""
    returned = start %value
    return returned
    
#Definición de autoplay
def autoplay_():
    start = " autoplay"
    returned = start
    return returned
    
#Definición de required
def required_():
    start = " required"
    returned = start
    return returned
    
#Definición de checked
def checked_():
    start = " checked"
    returned = start
    return returned

#Definición de selected
def selected_():
    start = " selected"
    returned = start
    return returned
    
#Definición de multiple
def multiple_():
    start = " multiple"
    returned = start
    return returned
    
#Definición de multiple
def autofocus_():
    start = " autofocus"
    returned = start
    return returned
    
#Definición de controls
def controls_():
    start = " controls"
    returned = start
    return returned
    
#Definición de novalidate se incluye dentro de form
def novalidate_():
    start = " novalidate"
    returned = start
    return returned
    
#Definición de formnovalidate se incluye dentro de form
def formnovalidate_():
    start = " formnovalidate"
    returned = start
    return returned
    
#Para ejecución directa sin importacion
if __name__ == "__main__":
    print("You should import headers into your main proyect.")