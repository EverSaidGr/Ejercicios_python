nombre = input('Dame el nombre del alumno: ')
calificaciones = []
respuesta = 'Si'
while respuesta == 'Si':
    calif = float(input("Dame la calificación: "))
    calificaciones.append(calif)
    respuesta = input('Quieres añadir otra calificación? ')

contador = 0
for calificacion in calificaciones:
    contador += calificacion

promedio=contador/len(calificaciones)
print('El promedio de '+nombre+' es: ',promedio)
