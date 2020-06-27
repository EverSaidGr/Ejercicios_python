nac = ['MX', 'US', 'UK', 'MX', 'MX', 'US', 'UK', 'FR', 'CH', 'CH']

nac.append('JP')
print (nac)
print('Numero de repeticiones de MX: ',nac.count('MX'))
print('El primer UK se encuentra en: ',nac.index('UK'))

nac_copia = nac.copy()

nac_copia.extend(['COL', 'ARG', 'BR'])
print(nac_copia)
nac_copia.remove('CH')
print('Lista sin la palabra CH: ', nac_copia)
