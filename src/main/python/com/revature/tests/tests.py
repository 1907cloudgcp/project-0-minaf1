#Testing
import service

def testLoginSuccessful():
	assert service.login('john', 'smith') == True
	
def testLoginFailure():
	assert service.login('john', 'smithhh')
	
def testWithdrawalSuccess():
	assert service.withdrawal('john', 'smith', 20) == True

def testWithdrawalFailure():
	assert service.withdrawal('john', 'smith', 200) == False
	
def main():
	testLoginSuccessful()
	testLoginFailure()
	
if __name__ == '__main__':
	main()