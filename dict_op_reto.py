respuesta = 's'
mundo = {}
while respuesta == 's':
    nom_pais = input('Dame el nombre del pais: ')
    cant_personas = int(input('Dame el numero de personas del pais: '))
    mundo[nom_pais] = cant_personas
    respuesta = input('Deseas agregar otro pais? ')
for pais,habitantes in mundo.items():
    print(f'En {pais} hay {habitantes} habitantes')
consulta_pais = input('Que pais quieres consultar? ')
print(f'El pais {consulta_pais} tiene: {mundo[consulta_pais]} personas')
