import logging
import json
import os.path

def getLogger():
	logger = logging.getLogger('logging')
	logging.basicConfig(level=logging.DEBUG, filename="resources/transactions.log")
	return logger
	
def getAccountData():
	print('getting file handle')
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, "../../../../resources/accounts.json")
	with open(path) as f:
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
			index = trans.find(username + ':')
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