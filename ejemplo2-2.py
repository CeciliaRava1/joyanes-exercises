# Calcular el valor de la suma 1+2+3+...+100
nroASumar = 0
contador = 0
resultadoSuma = 0

while contador < 100:
    nroASumar +=1
    resultadoSuma += nroASumar
    contador += 1

print(resultadoSuma)