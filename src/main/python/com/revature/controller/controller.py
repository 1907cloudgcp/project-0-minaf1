from service import service
from ioDAO import ioDAO

class Controller:
    dao = ioDAO
    service = service.Service()
    def __init__(self):
        pass

    def action(self, username, password):
        while True:
            print('1. Get balance')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. View all tranactions')
            print('5. Log out')

            choice = int(input('Make your choice: '))
            if choice == 1:
                print('Your balance is: $ ', self.service.balance(), '\n')
            elif choice == 2:
                amount = input('How much do you want to deposit:')
                self.service.deposit(amount)
            elif choice == 3:
                amount = input('How much do you want to withdraw:')
                self.service.withdraw(amount)
            elif choice == 4:
                self.service.getAllTransactions()
            else:
                if input('Are you sure you want to logout? Y / N. ').upper() == 'Y':
                    self.service.logout()
                break

    def start(self):
        hasAccount = input('Do you have an account with us. Y / N. ')

        if hasAccount.upper() == 'Y':
            login = input('Would you like to log in? Y / N. ')
            if login.upper() == 'Y':
                username = input('Username: ')
                password = input('Password: ')
                if self.service.login(username, password):
                    self.action(username, password)
                else:
                    print('We cannot find an account with the username/password you have provided.')

        else:
            wantsToRegister = input('Would you like to register? Y / N.')
            if wantsToRegister.upper() == 'Y':
                self.service.register()
