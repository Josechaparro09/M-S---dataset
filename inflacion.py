import json

# Nombre del archivo JSON en tu proyecto
def getInflacionByAnio(anio):
    nombre_archivo = "Assets/Inflacion.json"
    cadena = json.load(open(nombre_archivo, encoding="utf8"))
    return cadena[str(anio)]
print(getInflacionByAnio(2020))
def getDesempleo(anio,mes):
    nombre_archivo = "Assets/Desempleo.json"
    cadena = json.load(open(nombre_archivo, encoding="utf8"))
    return cadena[str(anio)][mes]
print(getDesempleo(2020,"enero"))
def getPib(anio):
    nombre_archivo = "Assets/pib-años.json"
    cadena = json.load(open(nombre_archivo, encoding="utf8"))
    return cadena[str(anio)]["pib"]
print(getPib(2020))