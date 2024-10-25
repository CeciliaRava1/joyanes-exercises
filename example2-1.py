# Calculate the net pay of a worker given the number of hours worked, the hourly rate, and the tax rate.

# Input section
workerInput = True
workerNames = []
hoursWorked = []
hourlyIncome = []
netSalary = []
position = 0

valid = False
while not valid:
    hourlyRate = int(input('Enter the hourly rate '))
    if hourlyRate <= 0:
        print('The amount must be positive and non-zero')
    else:
        valid = True

valid = False
while not valid:
    taxRate = int(input('Enter the tax rate as a percentage from 0-100 '))
    if taxRate < 0 or taxRate > 100:
        print('The amount must be positive, non-zero, and less than 100')
    else:
        valid = True

while workerInput:
    workerNames.append(input('Enter the name of the worker '))
    valid = False

    while not valid:
        hoursWorked.append(int(input(f'Enter the number of hours {workerNames[position]} worked ')))
        if hoursWorked[position] <= 0:
            print('The number of hours must be positive and non-zero')
        else:
            valid = True

    # Processing input data
    hourlyIncome.append(hoursWorked[position] * hourlyRate) 
    netSalary.append(int(hourlyIncome[position] - (hourlyIncome[position] * taxRate) / 100))

    valid = False
    while not valid:
        continueInput = int(input('Enter 0 to end the program. 1 to continue '))
        if continueInput == 0:
            workerInput = False
            valid = True
        elif continueInput == 1:
            position += 1
            valid = True
        else:
            print('Enter 1 to continue, 0 to end')

print('\n')
print('*********************************')
# print('Worker | Hours | Gross Pay | Taxes | Net Pay')
position = 0
for i in workerNames:
    print(f'Worker: {workerNames[position]} \n  Hours: {hoursWorked[position]}')
    print(f'  Gross Pay: $ {hourlyIncome[position]} \n  Taxes: {taxRate}%')       
    print(f'  Net Pay: $ {netSalary[position]}')
    position += 1
    print('---------------------------------')
