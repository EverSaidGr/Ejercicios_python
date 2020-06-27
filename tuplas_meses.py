meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
respuesta = 'Si'
while respuesta == 'Si':
    mes = int(input('Dame el numero del mes que quieres ver: '))
    if mes > 0 and mes <= 12:
        mes_str = meses[mes-1]
        print('El mes es : ',mes_str)
    else:
        print('Numero incorrecto')
    respuesta = input('Quieres agrgar otro nombre?: ')