'''
Creator: Taban Cosmos
Date: 03/31/2017
Purpose: For learning
Anyone can grab the code and modify the code
Bank and Customer Python object oriented example
'''

#...........................................................

class Customer():
    ''' Customer class '''

    def __init__(self, age=0, full_name="", occupation="", accounts=""):
        self.age = age
        self.full_name = full_name
        self.occupation = occupation
        self.accounts = accounts

    def customer_info(self):
        print("Name: " + self.full_name + "\nOccupation: " + self.occupation)
        print("\nAge: " + str(self.age) + "\nAccounts: " + self.accounts)

#...........................................................

class Bank():
    ''' Bank class '''
    # functions

    def __init__(self, initial=0):
        self.savings = 0
        self.checking = initial

    def check_balance(self, account_type=''):
        # check account balances
        if account_type == 'checking':
            return self.checking  # return checking balance
        elif account_type == 'savings':
            return self.savings  # return savings balance
        else:
            return 'Error'

    def withdraw_money(self, withdraw, account_type):
        #savings
        if account_type == 'savings':
            if withdraw >= self.savings:
                print("\nInsufficient funds\n - Balance is: ", self.savings, " but you requested: ", withdraw)
            else:
                self.savings = self.savings - withdraw
                print("\nAmount withdrawn: ", withdraw, "\n - Current balance: ", self.savings)

        #checking
        if account_type == 'checking':
            if withdraw >= self.checking:
                print("\nInsufficient funds\n - Balance is: ", self.checking, " but you requested: ", withdraw)
            else:
                self.checking = self.checking - withdraw
                print("\nAmount withdrawn: ", withdraw, "\n - Current balance: ", self.checking)

    def transfer_amount(self, amount, account_type=''):
        # move amount from one account to another
        if account_type == 'savings':
            balance = self.savings - amount
            if self.savings > amount and balance > amount:
                self.checking = self.checking + amount  # update checking balance
                self.savings = balance  # update savings balance
                print(amount, ' successfully moved to checking')
            else:
                print('savings, insufficient funds: ', str(self.savings))

        if account_type == 'checking':
            balance = self.checking - amount
            if self.checking > amount and balance > amount:
                self.savings = self.savings + amount  # update savings balance
                self.checking = balance  # update checking balance
                print(amount, ' successfully moved to savings')
            else:
                print('Checking, insufficient funds: ', str(self.checking))

    def make_deposite(self, deposite, account_type=''):
        # choice the account to receive deposite
        if account_type == 'savings':
            result = self.savings + deposite
            self.savings = result  # update savings balance
        if account_type == 'checking':
            result = self.checking + deposite
            self.checking = result


new_customer = Customer(
29, "Mark kamanu", "Software Engineer", "Checking and savings  account")
new_customer.customer_info()
new_account = Bank(200000)
print('Accounts with initials amouns\n')
print('Checking: ', new_account.check_balance('checking'))
print('savings: ', new_account.check_balance('savings'))
print('\n----------------------------')
print('Make deposites:')
print('To savingss')
new_account.make_deposite(309, 'savings')
print('New balance ', new_account.check_balance('savings'))
print('\nTo checking')
new_account.make_deposite(20, 'checking')
print('New balance', new_account.check_balance('checking'))
print('\n----------------------------')
print('\nTransfer money from checking to savings')
new_account.transfer_amount(500, 'checking')
print('New savingss balance: ', new_account.check_balance('savings'))
print('New checking balance: ', new_account.check_balance('checking'))

print("\nWithdrawing from Savings account:")
new_account.withdraw_money(819, 'savings')
print("\nWithdrawing from Checking account:")
new_account.withdraw_money(819, 'checking')
