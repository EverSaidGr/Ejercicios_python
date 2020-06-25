edad = int(input('Dame tu edad: '))
promedio = float(input('Dame tu promedio: '))

if edad < 6:
    print('Kinder')
elif edad >= 6 and edad < 12:
    print('Primaria')
    if promedio >= 9.5:
        print('Promedio aceptable')
    else:
        print('Promedio deficiente')
elif edad >= 12 and edad < 15:
    print('Secundaria')
    if promedio >= 9:
        print('Promedio aceptable')
    else:
        print('Promedio deficiente')
elif edad >= 15 and edad < 18:
    print('Bachillerato')
    if promedio >= 8.5:
        print('Promedio aceptable')
    else:
        print('Promedio deficiente')
elif edad >= 18 and edad < 23:
    print('Universidad')
    if promedio >= 8:
        print('Promedio aceptable')
    else:
        print('Promedio deficiente')
else:
    print('Profesionista')
    print('Tu ya no estudias')