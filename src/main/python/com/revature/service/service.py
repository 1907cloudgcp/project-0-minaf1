import json
import ioDAO as dao
from error import LoginError
from error import WithdrawTooMuchError

logger = dao.getLogger()
#account = Account()

def saveAccounts(data):
	print('saving back to file')
	with open('accounts.json', 'w') as f:
		json.dump(data, f, indent=2)
	
def register():
	username = input('Choose your username')
	password = input('Choose your password')
	amount = 0.0
	
	data = dao.getAccountData()
	accounts = data['accounts']
	for acc in accounts:
		pass
	
	newAccDeposit = input('would you like to make a deposit in your new account: ')
	if newAccDeposit:
		amount = float(input('How much do you want to deposit: '))
	accounts += [{"username":username, "password":password, 'amount':amount}]
	logger.info(username + ': has registered with our bank.')
	saveAccounts(data)

def balance(username, password):
	print('getting', username, '\'s  balance')
	_, acc = dao.checkAccountExists(username, password)
	if acc:
		logger.info(username + ': has asked for their balance.')
		return round(float(acc['amount']), 2)
		
def deposit(username, password, amount):
	print('making a deposit')
	data, acc = dao.checkAccountExists(username, password)
	if acc != False:
		acc['amount'] = acc['amount'] + float(amount)
		logger.info(username + ': has made a deposit of ' + amount + '.')
		print('You have deposited: $', round(float(amount), 2))
				
	saveAccounts(data)
	
def withdraw(username, password, amount):
	print('making a withdrawal')
	data, acc = dao.checkAccountExists(username, password)
	if acc:
		if float(acc['amount']) < float(amount):
			print('You can\'t withdraw more than you have in the account')
			print('Please try again with a reasonable amount')
			logger.error(username + ': has attempted a withdrawal of more money than amount in account.' + amount)
			try:
				raise WithdrawTooMuchError
			except ArithmeticError:
				print('You cannot take out more money than you have on the account.')
		else:
			acc['amount'] = acc['amount'] - float(amount)
			logger.info(username + ': has made a withdrawel of $ ' + amount +'.')
			print('You have withdrawn: $ ', round(float(amount), 2))
	saveAccounts(data)

def getAllTransactions(username):
	print('Retreiving all transactions for', username)
	transList = dao.getTransactionList(username)
	for trans in transList:
		print(trans, end='')
		

def login(username, password):
	print('logging in...')
	
	# data = dao.getAccountData()
	# for acc in data['accounts']:
		# if acc['username']==username:
			# if acc['password'] == password:
			
	data, acc = dao.checkAccountExists(username, password)
	if acc:
		logger.info(username + ': has logged in.')
		return True
	else:
		try:
			raise LoginError
		except LoginError:
			print('Cannot login with this username/password pair.')
			logger.error('failed login using username:password pair.'+username+':'+password)
			return False
			
def logout():
	print('logging out')
	print('Have a nice day')
	#break
	
