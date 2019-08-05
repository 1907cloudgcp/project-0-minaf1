import logging
import json


def getLogger():
	logger = logging.getLogger('logging') #filename: C:/Users/minaf/Desktop/Revature/projects/project0/version2/
	logging.basicConfig(level=logging.DEBUG, filename="transactions.log")
	return logger
	
def getAccountData():
	print('getting file handle')
	with open('accounts.json') as f:
		data = json.load(f)
	return data
	
def checkAccountExists(username, password):
	data = getAccountData()
	for acc in data['accounts']:
		if acc['username'] == username and acc['password'] == password:
			return (data, acc)
	print('returning False from checkAccountExists:')
	#return False
	
def getTransactionList(username):
	transList = []
	with open('transactions.log') as f:
		for trans in f:
			index = trans.find(username+':')
			if index != -1:
				transList.append(trans[index:])
	return transList
	
def login(username, password):
	with open('accounts.json') as f:
		data = json.load(f)
	for acc in data['accounts']:
		if acc['username'] == username and acc['password'] == password:
			return True
	else:
		return False