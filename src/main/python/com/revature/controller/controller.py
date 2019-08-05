import service as serv
import ioDAO as dao

def action(username, password):
	while True:
		print('1. Get balance')
		print('2. Deposit')
		print('3. Withdraw')
		print('4. View all tranactions')
		print('5. Log out')
		
		choice = int(input('Make your choice: '))
		if choice == 1:
			print('Your balance is: $ ', serv.balance(username, password), '\n')
		elif choice == 2:
			amount = input('How much do you want to deposit:')
			serv.deposit(username, password, amount)
		elif choice == 3:
			amount = input('How much do you want to withdraw:')
			serv.withdraw(username, password, amount)
		elif choice == 4:
			serv.getAllTransactions(username)
		else:
			if input('Are you sure you want to logout? Y / N. ').upper() == 'Y':
				serv.logout(username)
			break
	
hasAccount = input('Do you have an account with us. Y / N. ')
logger = dao.getLogger()

if hasAccount.upper() == 'Y':
	login = input('Would you like to log in? Y / N. ')
	if login.upper() == 'Y':
		username = input('Username: ')
		password = input('Password: ')
		if serv.login(username, password):		
			action(username, password)
		else:
			print('We cannot find an account with the username/password you have provided.')
			logger.critical('Attempted login failure:'+username+','+password)
else:
	wantsToRegister = input('Would you like to register? Y / N.')
	if wantsToRegister.upper() == 'Y':
		serv.register()
	

		
		