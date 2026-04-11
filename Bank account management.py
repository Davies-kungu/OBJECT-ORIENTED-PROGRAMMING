class BankAccount:
    def __init__(self, acc_num, holder, initial_balance):
        self.__account_number = acc_num
        self.__holder = holder
        self.__balance = initial_balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def display_account_info(self):
        print("Account Number:", self.__account_number)
        print("Holder:", self.__holder)
        print("Balance:", self.__balance)
