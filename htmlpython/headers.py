#!/usr/bin/python
# -*- coding: utf-8 -*-

#FrontFace: Desarrollador Python para HTML
#Desarrollado por Brayan Rodríguez
#Versión 1.0 16/11/2016
#Página: Encapsulados Headers

#Definición Content-Type encabezado de los CGI
def contentType():
        final = "Content-Type = text/html; charset = utf-8\n"
        return final

#Definición de doctype
def doctype(atribute):
        final ="<!DOCTYPE html %s>\n"
        returned = final %atribute
        return returned

#Definición html
def html(content, atribute):
    start = "<html %s>\n"
    middle = start %atribute
    final = middle + "%s\n</html>"
    returned = final %content
    return returned

    
#Definición del encapsulado head se incluye dentro de <html></html>
def head(content):
    final = "\n<head>\n%s\n</head>\n"
    returned = final %content
    return returned

#Definición del encapsulado body se incluye dentro de <html></html>
def body(content, atribute):
    start = "<body %s>\n"
    middle = start %atribute
    final = middle + "%s\n</body>"
    returned = final %content
    return returned
    
#Definición del base, genera la dirección principal al que luego se agrega otros
#<base url="http://<dominio>.com>/index.html
#<a href="varios/otros.html">
def base(source, atribute):
    start = "<base %s %s>"
    middle = start %(source, atribute)
    final = middle + "</base>\n"
    returned = final
    return returned

#Definición del titulo se incluyen dentro de <head></head>
def title(content):
    final = "\n<title>%s</title>\n"
    returned = final %content
    return returned
    
#Definición del script se incluyen dentro de <head></head>
#<script type = "text/<programming_language>" src ="path/script"></script>
#<script> JAVA SCRIPT CODE </script>
def script(content, atribute):
    start = "\n<script %s>\n"
    middle = start %atribute
    final = middle + "%s\n</script>\n"
    returned = final %content
    return returned
    
#Definición del archivos externos pagina se incluyen dentro de <head></head>
def link(atribute):
    final = "<link rel=\"stylesheet\" %s>\n"
    returned = final %atribute
    return returned

#Definición de script


#MetaDatos HTML5 se incluyen dentro de <head></head> 
#Definición de caracteres:
#Definición de caracteres:
def meta(atributes):
    metatag = "<meta %s>\n"
    returnedtag = metatag %atributes
    return returnedtag


def metaCharset(chartype):
    metatag = "<meta charset =\"%s\">\n"
    returnedtag = metatag %chartype
    return returnedtag
    
#Definición de caracteres:
def metaDescription(description):
    metatag = "<meta name =\"description\" content =\"%s\">\n"
    returnedtag = metatag %description
    return returnedtag
    
#Definición de palabras claves:
def metaKeywords(keywords):
    metatag = "<meta name =\"keywords\" content =\"%s\">\n"
    returnedtag = metatag %keywords
    return returnedtag

#Para ejecución directa sin importacion
if __name__ == "__main__":
        print("You should import headers into your main proyect.")
