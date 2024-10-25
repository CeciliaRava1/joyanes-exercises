# Un cliente ejecuta un pedido a una fábrica. La fábrica examina en su banco de datos la ficha del cliente, si el clien-
# te es solvente entonces la empresa acepta el pedido; en caso contrario, rechazará el pedido. Redactar el algoritmo
# correspondiente.

saldoDeudorCliente = int(input('Ingrese el saldo deudor del cliente'));
saldoAcreedorCliente = int(input('Ingrese el saldo acreedor del cliente'));
if(saldoAcreedorCliente - saldoDeudorCliente >= 0):
    print('El pedido ha sido aceptado')
else:
    print('El pedido ha sido rechazado por la empresa porque el cliente no es solvente')



