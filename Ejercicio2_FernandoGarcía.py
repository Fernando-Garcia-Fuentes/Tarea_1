# Fernando García Fuentes A01800375
# 25 de agosto de 2023
# Modulos
from math import pow

# Función donde se calcula el BMI
def calculo(p , e):
    bmi = round(p / pow(e, 2) ,2)

    print(f'Tu BMI es {bmi}')

# Función que pide los datos al usuario
def modyMass():
    peso = int(input('Dame tu peso en kilogramos: '))
    estatura = float(input('Dame tu estatura en metros: '))
    calculo(peso, estatura)

modyMass()