from tests.tests import Tests
from service.service import Service


def main():
    global serv
    serv = Service()

    bankTest = Tests(serv)
    print(type(bankTest))
    # try:
    print('testing successful login:')
    bankTest.testLoginSuccessful('john', 'smith')
    print()

    print('testing successful withdrawal:')
    bankTest.testWithdrawalSuccess(20.0)
    print()

    print('testing failed withdrawal:')
    bankTest.testWithdrawalFailure(20000.0)
    print()

    print('')
    bankTest.testLoginFailure('john', 'smithhh')
    # except Exception as ex:
    #     # print(ex.with_traceback())
    #     print('Exception!!! ', ex.__cause__, ex.__traceback__)


    # except Exception as e:
    #     print('problem: ', e.__cause__, '\n\n', e.__context__, 'error args:')
    # finally:
    print(f'{bankTest.TESTS_PASSED} tests passed out of {bankTest.TESTS_EXECUTED} executed.')


if __name__ == '__main__':
    main()
