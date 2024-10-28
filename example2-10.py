# Example 2.10. Suppose a sequence of numbers is provided, such as 5 3 0 2 4 4 0 0 2 3 6 0 2,  
# and you want to count and print the number of zeros in the sequence

amountOfZeros = 0
correctInput = False
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while not correctInput:
        sequenceOfNumbers = input('Input a sequence of numbers ')

        for number in sequenceOfNumbers:
            if number in numbers:
                if number == '0':
                    amountOfZeros += 1
                    correctInput = True

            else:
                print('Invalid input. Please input a sequence of numbers')
                break

if correctInput:
    print(f'The amount of zeros of the seequence is {amountOfZeros}')

