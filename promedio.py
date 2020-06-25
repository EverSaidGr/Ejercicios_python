nombre = input('Dame el nombre del alumno: ')
calif_1 = float(input("Dame la calificación 1: "))
calif_2 = float(input("Dame la calificación 2: "))
calif_3 = float(input("Dame la calificación 3: "))

promedio = (calif_1 + calif_2 + calif_3)/3

if promedio >= 7:
    print(nombre + ' Aprobaste la materia, pasaste de año')
else:
    print(nombre + 'Reprobaste la materia, Tendras que repetirlo')
