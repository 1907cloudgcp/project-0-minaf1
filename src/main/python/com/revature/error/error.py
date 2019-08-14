class Error(Exception):
    """ Base class for the other errors """

    def toString(self, msg: str):
        return msg


# noinspection PyMethodMayBeStatic
class LoginError(Error):
    """ Log in error : when a user is not found in the system """

    def main(self):
        self.toString('An account with this username already exists. Please choose another one')

    if __name__ == '__main__':
        main()


class WithdrawTooMuchError(ArithmeticError):
    """ withdraw error: when a user tries to withdraw too much money """
    pass
