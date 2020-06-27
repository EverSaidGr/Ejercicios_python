text = "Martin_8/9$Juan_5/4/9/8$Francisco_10/10/10/9"
students_list = text.split('$')
for student in students_list:
    values = student.split('_')
    name = values[0]
    califs = values[1].split('/')
    suma = 0
    for calif in califs:
        suma += float(calif)
    avg = suma / len(califs)
    print(f'La calificación final de {name} es: {avg}')