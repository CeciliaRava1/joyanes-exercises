# EXAMPLE 2.7. Calculate the average of a series of positive numbers, assuming the data is read from a terminal. 
# An input value of zero will indicate that the end of the series of positive numbers has been reached.

average = 0
amountOfNumbers = 0
execution = True
correctInput = False

while execution:
    try: # Allows to manage the error from receive a string input
        inputNumber = int(input('Type a positive number: '))
        if inputNumber > 0:
            correctInput = True
            amountOfNumbers += 1
            average += inputNumber
            correctInput = False

            while not correctInput:
                try: # Allows to manage the error from receive a string input
                    continueExecution = int(input('Continue execution? 1.Yes 0.No: '))
                    if continueExecution == 0 or continueExecution == 1:
                        correctInput = True
                        if continueExecution == 0:
                            execution = False
                    else:
                        print('You must type 1 for yes and 0 for no')
                except ValueError: # Allows to manage the error from receive a string input
                    print("Invalid input. Please enter 1 for yes or 0 for no.")
        else:
            print('The number input must be positive and different from zero')
    except ValueError: # Allows to manage the error from receive a string input
        print("Invalid input. Please enter a positive number.")

if amountOfNumbers > 0:
    average = round((average / amountOfNumbers), 2)
    print(f'The average of the input numbers is {average}')
else:
    print("No positive numbers were entered.")

