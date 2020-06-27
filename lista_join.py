nombres = []
respuesta = 'Si'
while respuesta == 'Si':
    nombre = input('Dame el nombre: ')
    nombres.append(nombre)
    respuesta = input('Quieres agrgar otro nombre?: ')
#text=','.join(nombres)
#print(text)
print(','.join(nombres))