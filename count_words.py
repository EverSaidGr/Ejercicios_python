texto = 'Este texto tiene algunas palabras Este es otro texto con algunas palabras diferentes'

text_list = texto.split(' ')
palabras = {}
#for palabra in text_list:
#    if palabra in palabras:
#        palabras[palabra] += 1
#    else:
#        palabras[palabra] = 1

for palabra in text_list:
    palabras[palabra] = text_list.count(palabra)
for palabra, valor in palabras.items():
    print(f'En la palabra {palabra} se repite {valor}')
