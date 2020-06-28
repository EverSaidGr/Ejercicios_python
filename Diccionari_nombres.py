nom = input('Dame el nombre: ')
ape = input('Dame los apellidos: ')
ed = int(input('Dame la edad: '))
corr = input('Dame el correo: ')

persona = {
    'nombre' : nom,
    'apellidos': ape,
    'edad' : ed,
    'correo' : corr
}

print(f'Hola! Mi nombre es {persona["nombre"]} {persona["apellidos"]}, tengo {persona["edad"]} anos y mi correo electronico es {persona["correo"]}')