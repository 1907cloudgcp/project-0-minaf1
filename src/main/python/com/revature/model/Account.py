class Account:
    def __init__(self):
        pass

    def __init__(self, username, password, amount):
        self.username = username
        self.password = password
        self.amount = amount

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getAmount(self):
        return self.amount

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setAmount(self, amount):
        self.amount = amount

    def toString(self):
        return self.username+':'+self.password+':'+self.amount
