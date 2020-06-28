cellphone = {
    'marca' : 'Motorola',
    'RAM' : 6,
    'almacenamiento' : 32,
    'color' : 'Negro'
}

print(cellphone)
print('La marca es: ',cellphone['marca'])
new_marca = input('Dame de la nueva marca: ')
#Actualizar un valor en el diccionario
cellphone['marca'] = new_marca
print(cellphone)

#Agregar un nuevo elemento a un diccionario

so = input('Dame el sistema operativo: ')
cellphone['so'] = so
print(cellphone)

#Eliminar elemento del diccionario

del cellphone['color'] 
print(cellphone)

#iterar un diccionario
for clave, valor in cellphone.items():
    print(f'La clave es: {clave}, y su valor es: {valor}')

#iterar solo claves en diccionario
for clave in cellphone.keys():
    print(f'la clave es ', clave)
#iterar solo VALORES en diccionario
for valor in cellphone.values():
    print(f'el valor es: ', valor)