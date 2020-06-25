edad = int(input('Dame tu edad: '))

if edad < 6:
    print('Kinder')
elif edad >= 6 and edad < 12:
    print('Primaria')
elif edad >= 12 and edad < 15:
    print('Secundaria')
elif edad >= 15 and edad < 18:
    print('Bachillerato')
elif edad >= 18 and edad < 23:
    print('Universidad')
else:
    print('Profesionista')