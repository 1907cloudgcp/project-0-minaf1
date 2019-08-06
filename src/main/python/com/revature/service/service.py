from ioDAO import ioDAO
from model import Account
from error import error
import json
import datetime

dao = ioDAO
LoginError = error.LoginError
WithdrawTooMuchError = error.WithdrawTooMuchError
logger = dao.getLogger()
global account

def login(username, password):
	print('logging in...')
	
	data = dao.getAccountData()
	for acc in data['accounts']:
		if acc['username'] == username and acc['password'] == password:
			print('successfully logged in')
			global account
			account = Account.Account(str(username), str(password), float(acc['amount']))
			print(username, '\'s balance is:', acc['amount'])
			logger.info(f'{getCurrentTime()}:{username}: has successfully logged in.')
			return True	
	try:
		raise LoginError
	except LoginError:
		print('Cannot login with this username/password pair.')
		logger.error(f'failed login using username:password pair.{username}:{password}')
	finally:
		return False

def saveAccounts(data):
	print('Saving back to file')
	
	for acc in data['accounts']:
		if acc['username'] == account.getUsername():
			acc['amount'] = account.getAmount()
	
	with open('accounts.json', 'w') as f:
		json.dump(data, f, indent=2)
	
def register():
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
	accounts += [{"username":username, "password":password, 'amount':amount}]
	logger.info(f'{getCurrentTime()}:{username}: has registered with our bank.')
	saveAccounts(data)

def balance():
	print('getting', account.getUsername(), '\'s  balance')
	if account != None:
		logger.info(f'{getCurrentTime()}:{account.getUsername()}: has asked for their balance.')
		return round(float(account.getAmount()), 2)
		
def deposit(amount):
	print('making a deposit')
	if account != None:
		logger.info(f'{getCurrentTime()}:{account.getUsername()}: has made a deposit of {amount}.')
		account.setAmount(account.getAmount() + float(amount))
	
def withdraw(amount):
	print('making a withdrawal')
	amount = float(amount)
	
	if account != None:
		if account.amount > amount:
			account.setAmount(account.getAmount() - amount)
			logger.info(f'{getCurrentTime()}:{account.getUsername()}: has made a withdrawel of $ {amount}.')
		else:
			logger.error(f'{getCurrentTime()}:{account.getUsername()}: has attempted a withdrawal of more money than amount in account.{amount}')
			print('withdraw failed. either accounts None or its higher than amount')
	return False
	
def getAllTransactions():
	username = account.getUsername()
	print('Retreiving all transactions for', username)
	transList = dao.getTransactionList(username)
	for trans in transList:
		print(trans, end='')

def logout():
	print('logging out')
	print('Have a nice day')
	logger.info(f'{getCurrentTime()}:{account.getUsername()} has successfully logged out.')
	data = dao.getAccountData()
	saveAccounts(data)
	
def getCurrentTime():
	return datetime.datetime.now().strftime('%y-%m-%dT%I:%M:%S')
