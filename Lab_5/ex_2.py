from validator import Validator


class Account:
    def __init__(self, acc_number, balance=0.0):
        if type(acc_number) is not str:
            raise InvalidAccNumber("Account number must be a string")

        if Validator.is_positive_number(balance) is False:
            balance = 0.0

        self._account_number = acc_number
        self._balance = balance

    def deposit(self, amount):
        """
        :param amount:
        :return: True if operation was successful, False otherwise
        """
        if Validator.is_positive_number(amount) is False:
            print("Invalid amount")
            return False

        self._balance += amount
        return True

    def withdraw(self, amount):
        """
        :param amount:
        :return: True if the operation was successful, False otherwise
        """
        if Validator.is_positive_number(amount) is False:
            print("Invalid amount")
            return False

        if amount > self._balance:
            print("Insufficient funds")
            return False

        self._balance -= amount
        return True

    def get_balance(self):
        return self._balance

    def calculate_interest(self):
        pass


class CheckingAccount(Account):
    def __init__(self, acc_number, balance=0):
        super().__init__(acc_number, balance)
        self.__max_amount_to_withdraw = 1000

    def calculate_interest(self):
        return 0

    def withdraw(self, amount):
        if amount > self.__max_amount_to_withdraw:
            print("You cannot withdraw more than 1000")
            return False
        else:
            return super().withdraw(amount)


class SavingsAccount(Account):

    INTEREST = 0.02

    def __init__(self, acc_number, balance=0):
        super().__init__(acc_number, balance)
        self.__max_monthly_withdraws = 5

    def calculate_interest(self):
        return self._balance * SavingsAccount.INTEREST

    def withdraw(self, amount):
        if self.__max_monthly_withdraws > 0:
            if super().withdraw(amount):
                self.__max_monthly_withdraws -= 1
                return True
            return False
        else:
            print("You reached your maximum withdraws this month")
            return False

    def reset_max_withdraws(self):
        self.__max_monthly_withdraws = 5


class InvalidAccNumber(Exception):
    pass


# tests
# checking_account = CheckingAccount("12345", 1000.0)
# checking_account.deposit(500.0)
# checking_account.withdraw(200.0)
# print(f"Balance = {checking_account.get_balance()}")
# # will always be 0 for this example
# interest_checking = checking_account.calculate_interest()
# print(f"Interest on Checking Account: {interest_checking}")
#
# # Create a Savings Account
# savings_account = SavingsAccount("54321", 2000.0)
#
# # Deposit into Savings Account
# savings_account.deposit(1000.0)
#
#
# savings_account.withdraw(500.0)
# savings_account.withdraw(200.0)
# savings_account.withdraw(100.0)
# savings_account.withdraw(300.0)
# savings_account.withdraw(150.0)
#
# # Try to withdraw more than the allowed monthly limit
# savings_account.withdraw(50.0)
#
# # Calculate interest on Savings Account
# interest_savings = savings_account.calculate_interest()
# print(f"Interest on Savings Account: {interest_savings}")
#
# # Reset
# savings_account.reset_max_withdraws()
#
# savings_account.withdraw(50.0)
# print(savings_account.get_balance())
