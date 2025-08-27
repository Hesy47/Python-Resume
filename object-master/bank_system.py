class Bank:
    def __str__(self):
        return f" welcome back {self.owner}"

    def __init__(self, owner: str, balance: float):
        if not "".join(owner.split()).isalpha():
            print("please inter a valid owner name")

        if balance < 0:
            print("The balance can not be a negative number")

        self._owner = owner
        self._balance = balance

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner: str):
        if not "".join(new_owner.split()).isalpha():
            print("please inter a valid owner name")

        self._owner = new_owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            print("The balance can not be a negative number")

        self._balance = new_balance

    def deposit(self):
        pass

    def withdraw(self):
        pass
