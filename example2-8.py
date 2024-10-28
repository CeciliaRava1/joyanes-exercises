# EXAMPLE 2.8. Sum of the even numbers between 2 and 100. even: 0 odd: 1

sumEvenNumbers = 0

for number in range (2, 101):
    if number % 2 == 0:
        sumEvenNumbers += number

print(f'The sum of even numbers between 2-100 is {sumEvenNumbers}')
