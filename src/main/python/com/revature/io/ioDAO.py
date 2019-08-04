import logging
import json

def getLogger():
	logger = logging.getLogger('logging')
	logging.basicConfig(level=logging.DEBUG, filename="C:/Users/minaf/Desktop/Revature/projects/project0/attempt3/transactions.log")
	return logger
	
def getAccountData():
	print('getting file handle')
	with open('accounts.json') as f:
		data = json.load(f)
	return data
	
def checkAccountExists(username, password):
	data = getAccountData()
	for acc in data['accounts']:
		if acc['username'] == username:
			print('username', username, 'matched. Comparing password') 
			if acc['password'] == password:
				return (data, acc)
	return False
	
def getTransactionList(username):
	transList = []
	with open('transactions.log') as f:
		for trans in f:
			index = trans.find(username+':')
			if index != -1:
				transList.append(trans[index:])
	return transList