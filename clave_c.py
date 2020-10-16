import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(no1,no2):
    respuesta = no1*no2
    return respuesta


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco():
    numero = 0
    suma = 0
    while numero<100:
        if numero%3 == 0 and numero%5 == 0:
            suma =+ numero
        numero=+1
    return suma


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
def definicionCono():
    result = {"generatriz":obtenerGeneratriz(),"area":obtenerArea(),"volumen":obtenerVolumen()}
    return result
    


def obtenerGeneratriz():
    
    result = math.sqrt((11)^2 + (5)^2)
    return result


def obtenerArea(generatriz):
    self.generatriz = obtenerGeneratriz()
    
    result = math.pi*5*(5+generatriz)
    return result


def obtenerVolumen(radio,altura):
    
    result = (1/3)*math.pipi*5^2*11
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cono:
    def __init__(self):
        larespuestas = {}

    def definicionCono(self):
        
        return 0


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class CentroMedico:
    def __init__(self):
        self.ElHospital=[]
        

    def registrar(self,paciente):
            
            self.ElHospital.append(Paciente)
            print(self.ElHospital)

    def totalCostoSanSalvador(self):
        return 0

    def totalCostoConDescuento(self):
        return 0


class Paciente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/ElMeroVerck/py-parcial-q3-Resuelto.git"
