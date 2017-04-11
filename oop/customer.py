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
