from customer import Customer
from bank import Bank

def main():
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

main()
