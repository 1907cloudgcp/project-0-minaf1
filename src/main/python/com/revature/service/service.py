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
                print(username, '\'s balance is:', acc['amount'])
                logger.info(f'{self.getCurrentTime()}:{username}: has successfully logged in.')
                return True
        try:
            raise LoginError
        except LoginError:
            print('Cannot login with this username/password pair.')
            logger.error(f'failed login using username:password pair.{username}:{password}')
        finally:
            return False

    def saveAccounts(self, data):
        print('Saving back to file')
        global account
        for acc in data['accounts']:
            if acc['username'] == account.getUsername():
                acc['amount'] = account.getAmount()

        with open('resources/accounts.json', 'w') as f:
            json.dump(data, f, indent=2)

        account = None

    def register(self):
        global account
        username = input('Choose your username: ')
        password = input('Choose your password: ')
        amount = 0.0

        data = dao.getAccountData()

        accounts = data['accounts']
        for acc in accounts:
            if acc['username'] == username:
                raise NameError('An account with this username already exists.')

        newAccDeposit = input('would you like to make a deposit in your new account Y/N. ')
        if newAccDeposit.upper() == 'Y':
            amount = float(input('How much do you want to deposit: '))

        account = Account.Account(username, password, amount)
        # accounts += [{"username": username, "password": password, 'amount': amount}]
        accounts += [{"username": account.getUsername(), "password": account.getPassword(), "amount": account.getAmount()}]
        logger.info(f'{self.getCurrentTime()}:{username}: has registered with our bank.')
        self.saveAccounts(data)

    def balance(self):
        print('getting', account.getUsername(), '\'s  balance')
        if account is not None:
            logger.info(f'{self.getCurrentTime()}:{account.getUsername()}: has asked for their balance.')
            return round(float(account.getAmount()), 2)

    def deposit(self, amount: float):
        print('making a deposit')
        if (account is not None) and (float(amount) > 0.0):
            logger.info(f'{self.getCurrentTime()}:{account.getUsername()}: has made a deposit of {amount}.')
            account.setAmount(account.getAmount() + float(amount))
        else:
            logger.error(f'{self.getCurrentTime()}:{account.getUsername()}:tried to deposit negative value of {amount}.')
            print('You cannot deposit a negative number value to your account.\nPlease try again with a bigger value.')
	
	
    def withdraw(self, amount: float) -> bool:
        print('making a withdrawal')
        print('amount:', amount)

        if account is not None:
            print(account.username, account.password, account.amount)

            if float(account.getAmount()) > float(amount):
                account.setAmount(float(account.getAmount()) - float(amount))
                print('the withdrawal is successful. account amount is set to', account.amount)
                logger.info(f'{self.getCurrentTime()}:{account.getUsername()}: has made a withdrawal of $ {amount}.')
                return True
            else:
                logger.error(f'{self.getCurrentTime()}:{account.getUsername()}: has attempted a withdrawal of ' +
                             f'more money than amount in account.{amount}')
                print('withdraw failed. either accounts None or its higher than amount')
                # return False
        return False

    def getAllTransactions(self):
        username = account.getUsername()
        print('Retrieving all transactions for', username)
        transList = dao.getTransactionList(username)
        logger.info(f'{self.getCurrentTime()}:{account.getUsername()} has requested to see their transaction list')
        for trans in transList:
            print(trans, end='')

    def logout(self):
        print('logging out')
        print('Have a nice day')
        logger.info(f'{self.getCurrentTime()}:{account.getUsername()} has successfully logged out.')
        data = dao.getAccountData()
        self.saveAccounts(data)

    def getCurrentTime(self):
        return datetime.datetime.now().strftime('%y-%m-%dT%I:%M:%S')
