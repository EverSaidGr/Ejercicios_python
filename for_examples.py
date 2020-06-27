#Reto 1
for i in range(2, 301, 2):
    print(i)

#Reto 2
print('Reto 2 Tbala del 15')
for i in range(1, 20):
    resul = i * 15
    print(i, '* 15 =', resul)
#Reto 3
suma_impar=0
for i in range(51, 101, 2):
    suma_impar += i
print('Reto 3 suma de numeros impares entre 50 y 100:', suma_impar)
#Reto 4 
suma_par=0
for i in range(10, 101):
    if i % 2 == 0:
        suma_par += i
print ( 'La suma de los números pares entre el 10 y el 100 es:', suma_par )

