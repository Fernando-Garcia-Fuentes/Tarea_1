# Fernando García Fuentes A01800375
# 25 de agosto de 2023

# Función donde se reciben los kilometros
def kilometros(m):
    totKil = m * 1.609

    print(f'{7} millas son {totKil} km')

# Función que pide los datos al usuario
def datos():
    millas = int(input('Dame las millas que corriste: '))
    kilometros(millas)

datos()