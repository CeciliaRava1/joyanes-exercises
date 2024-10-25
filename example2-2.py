# Calculate the value of the sum 1+2+3+...+100
numberToAdd = 0
counter = 0
resultSum = 0

while counter < 100:
    numberToAdd += 1
    resultSum += numberToAdd
    counter += 1

print(resultSum)
