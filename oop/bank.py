#...........................................................
# Bank class

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
