import json
import datetime
import logging
from ioDAO import ioDAO
from model import Account
from error import error

dao = ioDAO
LoginError = error.LoginError
WithdrawTooMuchError = error.WithdrawTooMuchError

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("resources/transactions.log")
logger.addHandler(file_handler)


# noinspection PyMethodMayBeStatic
class Service:
    global account

    def login(self, username, password) -> bool:
        print('logging in...')

        data = dao.getAccountData()
        for acc in data['accounts']:
            if acc['username'] == username and acc['password'] == password:
                print('successfully logged in')
                global account
                account = Account.Account(str(username), str(password), float(acc['amount']))
                logger.info(f'{self.getCurrentTime()}:INFO:{username}: has successfully logged in.')
                return True
        try:
            raise LoginError
        except LoginError:
            print('Cannot login with this username/password pair.')
            logger.error(f'{self.getCurrentTime()}:ERROR:Failed login using username:password pair.{username}:{password}')
        finally:
            return False

    def saveAccounts(self, data):
        """
        :param data: receives the object representing the json file holding accounts
        this method saves all the locally persisted (changes to account variable) to the file
        """
        print('Saving your transactions.')
        global account
        for acc in data['accounts']:
            if acc['username'] == account.getUsername():
                # setting the account's amount field in the json file:
                acc['amount'] = account.getAmount()
        try:
            with open('resources/accounts.json', 'w') as f:
                json.dump(data, f, indent=2)
        finally:
            account = None

    def register(self):
        global account
        username = input('Choose your username: ')
        password = input('Choose your password: ')
        amount = 0.0
        data = dao.getAccountData()

        accounts = data['accounts']  # returns accounts array
        for acc in accounts:
            """ check if the user already exists. 
            if yes, tell the user, 
            else ask about initial deposit """

            if acc['username'] == username:
                try:
                    raise LoginError()
                except LoginError:
                    print('An account with this username already exists.')
                    return
                finally:
                    logger.error(f'{self.getCurrentTime()}:ERROR:user: has attempted to register with an existing username.')
        newAccDeposit = input('Would you like to make a deposit in your new account Y/N. ')
        if newAccDeposit.upper() == 'Y':
            amount = float(input('How much do you want to deposit: '))

        account = Account.Account(username, password, amount)
        # accounts += [{"username": username, "password": password, 'amount': amount}]
        accounts += [{"username": account.getUsername(), "password": account.getPassword(), "amount": account.getAmount()}]
        logger.info(f'{self.getCurrentTime()}:INFO:{username}: has registered with our bank.')
        self.saveAccounts(data)

    def balance(self):
        print('getting', account.getUsername(), '\'s  balance')
        if account is not None:
            logger.info(f'{self.getCurrentTime()}:INFO:{account.getUsername()}: has asked for their balance.')
            return self.currencyFormat(float(account.getAmount()))  # round(float(account.getAmount()), 2)

    def deposit(self, amount: float):
        print('making a deposit')
        if (account is not None) and (float(amount) > 0.0):
            logger.info(f'{self.getCurrentTime()}:INFO:{account.getUsername()}: has made a deposit of {amount}.')
            account.setAmount(account.getAmount() + float(amount))
        else:
            logger.error(f'{self.getCurrentTime()}:ERROR:{account.getUsername()}:tried to deposit negative value of {amount}.')
            print('You cannot deposit a negative number value to your account.\nPlease try again with a bigger value.')

    def withdraw(self, amount: float) -> bool:
        print('making a withdrawal')
        print('amount:', amount)

        if account is not None:
            print(account.username, account.password, account.amount)

            if float(account.getAmount()) > float(amount):
                account.setAmount(float(account.getAmount()) - float(amount))
                print('The withdrawal is successful. account amount is set to ', self.currencyFormat(account.amount))
                logger.info(f'{self.getCurrentTime()}:INFO:{account.getUsername()}: has made a withdrawal of $ {amount}.')
                return True
            else:
                logger.error(f'{self.getCurrentTime()}:ERROR:{account.getUsername()}: has attempted a withdrawal of ' +
                             f'more money than amount in account.{amount}')
                print('withdraw failed. either accounts None or its higher than amount')
        return False

    def getAllTransactions(self):
        username = account.getUsername()
        print('Retrieving all transactions for', username)
        transList = dao.getTransactionList(username)
        logger.info(f'{self.getCurrentTime()}:INFO:{account.getUsername()} has requested to see their transaction list')
        for trans in transList:
            print(trans, end='')

    def logout(self):
        global account
        print('logging out')
        print('Have a nice day')
        logger.info(f'{self.getCurrentTime()}:INFO:{account.getUsername()} has successfully logged out.')
        data = dao.getAccountData()
        self.saveAccounts(data)
        account = None

    def getCurrentTime(self):
        return datetime.datetime.now().strftime('%y-%m-%dT%I:%M:%S')

    def currencyFormat(self, num: float):
        return '$ {:,.2f}'.format(num)
