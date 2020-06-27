respuesta = 'Si'
while respuesta == 'Si':
    numero = int(input('que tabla de multiplicar quieres? '))
    contador = 1
    while contador <= 25:
        #multi = contador * numero
        #print(numero, '*', contador, '=', multi)
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1
    respuesta = input("Deseas hacer otra tabla de multiplicar? ")
print('Adios gracias por su preferencia')
