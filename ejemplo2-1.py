# Calcular la paga neta de un trabajador conociendo el número de horas trabajadas, la tarifa horaria y la tasa de impuestos.

# Ingreso de entrada
ingresoTrabajadores = True
nombreTrabajador = []
horasTrabajadas = []
ingresoHorasTrabajadas = []
sueldoNeto = []
posicion = 0

correcto = False
while correcto is False:
    pagaPorHora = int(input('Ingrese la paga por hora '))
    if pagaPorHora <= 0:
        print('El monto debe ser positivo y distinto de cero')
    else:
        correcto = True

correcto = False
while correcto is False:
    tasaImpositiva = int(input('Ingrese la tasa impositiva en porcentaje del 0-100 '))
    if tasaImpositiva < 0 or tasaImpositiva > 100:
        print('El monto debe ser positivo, distinto de cero y menor que 100')
    else:
        correcto = True

while ingresoTrabajadores is True:
    nombreTrabajador.append(input('Ingrese el nombre del trabajador '))
    correcto = False

    while correcto is False:
        horasTrabajadas.append(int(input(f'Ingrese la cantidad de horas que trabajo {nombreTrabajador[posicion]} ')))
        if horasTrabajadas[posicion] <= 0:
            print('La cantidad de horas debe ser positiva y distinta de cero')
        else:
            correcto = True

    # Procesamiento de entradas
    ingresoHorasTrabajadas.append(horasTrabajadas[posicion] * pagaPorHora) 
    sueldoNeto.append(int(ingresoHorasTrabajadas[posicion] - (ingresoHorasTrabajadas[posicion] * tasaImpositiva) / 100))

    correcto = False
    while correcto is False:
        continuar = int(input('Ingrese 0 si desea terminar el programa. 1 para continuar '))
        if continuar == 0:
            ingresoTrabajadores = False
            correcto = True
        elif continuar == 1:
            posicion +=1
            correcto = True

        else:
            print('Ingrese 1 para continuar, 0 para finalizar')

print('\n')
print('*********************************')
# print('Trabajador | Horas | Sueldo bruto | Impuestos | Sueldo Neto')
posicion = 0
for i in nombreTrabajador:
    print(f'Trabajador: {nombreTrabajador[posicion]} \n  Horas: {horasTrabajadas[posicion]}')
    print(f'  Sueldo bruto: $ {ingresoHorasTrabajadas[posicion]} \n  Impuestos: {tasaImpositiva}%')       
    print(f'  Sueldo neto: $ {sueldoNeto[posicion]}')
    posicion += 1
    print('---------------------------------')