# Fernando García Fuentes A01800375
# 25 de agosto de 2023

# Función donde se reciben los kilometros
def cowboys(a,b,c):
    totBoletos = a+b+c
    totCosto = a * 1050 + b * 750 + c * 450

    print(f'El total a pagar por {totBoletos} es de ${totCosto}')

# Función que pide los datos al usuario
def datos():
    claseA = int(input('Cuantos boletos para la clase A: '))
    claseB = int(input('Cuantos boletos para la clase B: '))
    claseC = int(input('Cuantos boletos para la clase C: '))
    cowboys(claseA, claseB, claseC)

datos()