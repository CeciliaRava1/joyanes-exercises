# A customer places an order with a factory. The factory checks the customer’s file in its database; if the customer
# is solvent, then the company accepts the order; otherwise, it will reject the order. Write the corresponding algorithm.

debtorBalance = int(input('Enter the customer\'s debtor balance: '))
creditorBalance = int(input('Enter the customer\'s creditor balance: '))
if (creditorBalance - debtorBalance >= 0):
    print('The order has been accepted.')
else:
    print('The order has been rejected by the company because the customer is not solvent.')


