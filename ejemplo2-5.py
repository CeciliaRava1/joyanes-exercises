# Se desea diseñar un algoritmo para saber si un número es primo o no.
# Un numero primo es aquel que es divisible entre 1 y si mismo

numeroIngresado = int(input('Ingrese un numero para saber si es primo: '))
cantidadFactores = 0


for numero in range(1, numeroIngresado):
    if numeroIngresado % numero == 0:
        cantidadFactores += 1
    
if cantidadFactores > 2 or numeroIngresado == 1:
    print(f'El numero {numeroIngresado} no es primo')
else: 
    print(f'El numero {numeroIngresado} es primo')