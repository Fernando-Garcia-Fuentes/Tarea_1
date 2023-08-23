# Fernando García Fuentes A01800375
# Variables
parcialUno = float(input('Calificación primer parcial: '))
parcialDos = float(input('Calificación segundo parcial: '))
parcialTres = float(input('Calificación tercer parcial: '))
final = float(input('Calificación examen final: '))

# Operaciones
calificacion = (((parcialUno + parcialDos + parcialTres)/3) * 0.70) + ( final * 0.30)

# Prints
print(f'Tu calificación final es {calificacion}')