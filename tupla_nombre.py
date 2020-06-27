nombres = input('Dame los nombres: ')

lista = nombres.replace(' ','').split(',')
print(lista)
tupla = tuple(lista)
print(tupla)
print('Cantidad de nombres: ', len(tupla))
print('Valor maximo: ', max(tupla))
print('Valor minimo: ', min(tupla))

