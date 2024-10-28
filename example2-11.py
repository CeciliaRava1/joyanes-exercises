# EXAMPLE 2.11. Given three numbers, determine if the sum of any pair of them is equal to the third number. 
# If this condition is met, write "Equal"; otherwise, write "Different."

numbers = []
numberInput = 0
correctInput = False

while not correctInput:
    try:
        for i in range (0, 3):
            numberInput = int(input('Type a number'))
            numbers.append(numberInput)

        if numbers[0] + numbers[1] == numbers[2]:
            print('Equal')
        else:
            print('Different')
            
        correctInput = True

    except ValueError:
        print('Invalid input. Please type a number')

