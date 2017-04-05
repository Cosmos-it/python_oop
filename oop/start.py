
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
    def __init__(self, age = 0,full_name ="",occupation ="",accounts=""):
       self.age = age
       self.full_name = full_name
       self.occupation = occupation
       self.accounts = accounts

    def customer_info(self):
       print("Name: " + self.full_name  + "\nOccupation: " +self.occupation)
       print("\nAge: " + str(self.age) + "\nAccounts: "+ self.accounts)

#...........................................................

class Bank():
    ''' Bank class '''
    #functions
    def __init__(self, initial = 0):
        self.saving = 0
        self.checking = initial

    def check_balance(self, account_type = ''):
        #check account balances
        if account_type == 'checking':
            return self.checking #return checking balance
        elif account_type == 'saving':
            return self.saving #return saving balance
        else:
            return 'Error'

    def transfer_amount(self, amount, account_type = ''):
        #move amount from one account to another
        if account_type == 'saving':
            balance = self.saving - amount
            if self.saving >  amount  and balance > amount:
                self.checking = self.checking + amount #update checking balance
                self.saving = balance #update saving balance
                print(amount, ' successfully moved to checking')
            else:
                 print('Saving, insufficient balance: ', str(self.saving))

        if account_type == 'checking':
            balance = self.checking - amount
            if self.checking > amount and balance > amount:
                self.saving = self.saving + amount #update saving balance
                self.checking = balance #update checking balance
                print(amount, ' successfully moved to saving')
            else:
                print('Checking, insufficient balance: ', str(self.checking))

    def make_deposite(self, deposite, account_type =''):
        #choice the account to receive deposite
        if account_type == 'saving':
            result = self.saving + deposite
            self.saving = result #update saving balance
        if account_type == 'checking':
            result = self.checking + deposite
            self.checking = result


# New object
new_customer = Customer(29, "Mark kamanu", "Software Engineer", "Checking and Saving  account")
new_customer.customer_info()
new_account = Bank(200000)
print('Accounts with initials amouns\n')
print('Checking: ',new_account.check_balance('checking'))
print('Saving: ', new_account.check_balance('saving'))
print('\n----------------------------')
print('Make deposites:')
print('To savings')
new_account.make_deposite(309, 'saving')
print('New balance ', new_account.check_balance('saving'))
print('\nTo checking')
new_account.make_deposite(20, 'checking')
print('New balance', new_account.check_balance('checking'))
print('\n----------------------------')
print('\nTransfer money from checking to saving')
new_account.transfer_amount(500, 'checking')
print('New savings balance: ',new_account.check_balance('saving'))
print('New checking balance: ',new_account.check_balance('checking'))











