#Testing
import service
import unittest
from error import LoginError
from error import WithdrawTooMuchError

TESTS_EXECUTED = 0
TESTS_PASSED = 0

def Test(to_decorate_function):
	def test_function(test_value):
		global TESTS_EXECUTED, TESTS_PASSED
		TESTS_EXECUTED += 1
		to_decorate_function(test_value)
		TESTS_PASSED += 1
	return test_function

def LoginTest(to_decorate_function):
	def test_function(test_value1, test_value2):
		global TESTS_EXECUTED, TESTS_PASSED
		TESTS_EXECUTED += 1
		to_decorate_function(test_value1, test_value2)
		TESTS_PASSED += 1
	return test_function

@LoginTest
def testLoginSuccessful(username, password):
	assert service.login(username, password), 'Login Failed. Please try a different username/password.'

@LoginTest	
def testLoginFailure(username, password):
	assert service.login(username, password) == False

@Test
def testWithdrawalSuccess(amount):
	assert service.withdraw('john', 'smith', amount), 'You cannot take out more money than you have on the account.'
	
@Test
def testWithdrawalFailure(amount):
	assert service.withdraw('john', 'smith', amount) == False, 'You cannot take out more money than you have on the account.'
	
def main():
	try:
		print(testLoginSuccessful('john', 'smith'), end='\n\n')
		print(testWithdrawalSuccess(20.0), end='\n\n')
		
		print(testWithdrawalFailure(20000.0), end='\n\n')
		print(testLoginFailure('john', 'smithhh'))
	except Exception as e:
		print(e)
	finally:
		print('{} tests passed out of {} executed.'.format(str(TESTS_PASSED), str(TESTS_EXECUTED)))
	
if __name__ == '__main__':
	main()