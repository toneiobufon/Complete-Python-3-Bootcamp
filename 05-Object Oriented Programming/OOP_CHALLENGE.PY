#CREATE A BANK ACCOUNT CLASS AND AN OBJECT OF THE CLASS
#SUCH ACCOUNT SHOULD HAVE A NAME, BALANCE, BE ABLE TO WITHDRAW, DEPOSIT, AND PREVENT WITHDRAWALS IF NOT ENOUGH FUNDS


class Bank_Account():
    #class object attributes
   


    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account owner :  {self.owner} \n 
        Account Balance: ${self.balance}'

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print( 'Your deposit has been accepted!')

    def withdraw(self, withdaw_amount):

        if self.balance < withdaw_amount:
            print('Not enough funds to process your withdrawl!')
        else:
            self.balance -+ withdaw_amount
            print('Your withdrawal was done!')

account = Bank_Account('ton', 200)

print(account)