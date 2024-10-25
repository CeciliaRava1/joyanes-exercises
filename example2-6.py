# Calculate the sum of all even numbers between 2 and 1,000

sumEvenNumbers = 0

for number in range (2, 1000):
    if number % 2 == 0:
        sumEvenNumbers += number
print(f'The sum of all even numbers between 2 and 1000 is {sumEvenNumbers}')
