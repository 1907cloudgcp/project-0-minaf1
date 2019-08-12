# Testing
import sys
import os
# lib_path = os.path.abspath(os.path.join(__file__, '..', 'service'))
# sys.path.append(lib_path)
# sys.path.insert(0, "src/main/python/com/revature")
# import revature
# from service.service import Service

# global TESTS_EXECUTED, TESTS_PASSED
# TESTS_EXECUTED = 0
# TESTS_PASSED = 0




class Tests:
    # serv = Service()
    TESTS_EXECUTED = 0
    TESTS_PASSED = 0
    # serv = None


    def __init__(self, service):
        self.serv = service

    def Test(self, to_decorate_function):
        def test_function(test_value):
            global TESTS_EXECUTED, TESTS_PASSED
            TESTS_EXECUTED += 1
            to_decorate_function(test_value)
            TESTS_PASSED += 1

        return test_function

    def LoginTest(self, to_decorate_function):
        def test_function2(test_value1, test_value2):
            global TESTS_EXECUTED, TESTS_PASSED
            TESTS_EXECUTED += 1
            to_decorate_function(test_value1, test_value2)
            TESTS_PASSED += 1

        return test_function2

    @LoginTest
    def testLoginSuccessful(self, username, password):
        # myLog = logging.setLogger(__name__)
        assert self.serv.login(username, password) is True, 'Login Failed. Please try a different username/password.'
        # myLog.info('successful logged in')


    @LoginTest
    def testLoginFailure(self, username, password):
        # myLog = logging.setLogger(__name__)
        assert self.serv.login(username, password) == False, 'Login Failed. Please try a different username/password.'

    @Test
    def testWithdrawalSuccess(self, amount):
        # myLog = logging.setLogger(__name__)
        assert self.serv.withdraw(amount), 'You cannot take out more money than you have on the account.'
        # myLog.info('blabla')


    @Test
    def testWithdrawalFailure(self, amount):
        # myLog = logging.setLogger(__name__)
        assert self.serv.withdraw(amount) == False, 'You cannot take out more money than you have on the account.'
