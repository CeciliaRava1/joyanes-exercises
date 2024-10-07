costeVehiculo = 20000
valorRecuperacion = 2000
aniosTranscurridos = 0
anio = 2005
depreciacionAcumulada= 0

print('***************************************************')
print('Anio | Valor real vehiculo | Depreciacion acumulada')

while aniosTranscurridos <= 6:
    if aniosTranscurridos == 0:
        depreciacionAcumulada = 0
    else:
        depreciacionAcumulada += int((costeVehiculo - valorRecuperacion) / 6)
    valorRealVehiculo = costeVehiculo - depreciacionAcumulada
    print(f'{anio} | {valorRealVehiculo}               | {depreciacionAcumulada}')
    anio+= 1
    aniosTranscurridos +=1


