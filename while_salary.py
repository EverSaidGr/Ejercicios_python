respuesta = 'Si'
while respuesta == 'Si': 
    nombre = input("Dame el nombre: ")
    sueldo = int(input("Dame el salario de "+nombre+":"))

    salario_bruto = sueldo * 0.84

    print('El salario de '+nombre+' es:', salario_bruto)
    respuesta = input("Deseas calcular otro salario? ")
print('Adios gracias por su preferencia')
