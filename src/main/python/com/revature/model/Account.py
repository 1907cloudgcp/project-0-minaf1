class Account:
    def __init__(self):
        pass

    def __init__(self, username: str, password: str, amount: float):
        self.username = username
        self.password = password
        self.amount = amount

    def getUsername(self) -> str:
        return self.username

    def getPassword(self) -> str:
        return self.password

    def getAmount(self) -> float:
        return self.amount

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setAmount(self, amount):
        self.amount = amount

    def toString(self) -> str:
        return self.username + ':' + self.password + ':' + self.amount
