# A program is designed to determine if a number is prime or not.
# A prime number is one that is divisible by 1 and itself.

enteredNumber = int(input('Enter a number to check if it is prime: '))
factorCount = 0

for number in range(1, enteredNumber):
    if enteredNumber % number == 0:
        factorCount += 1

if factorCount > 2 or enteredNumber == 1:
    print(f'The number {enteredNumber} is not prime.')
else:
    print(f'The number {enteredNumber} is prime.')
