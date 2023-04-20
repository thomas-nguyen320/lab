class Account:
    def __init__(self, name: str) -> None:
        '''
        Constructor to create initial state of a Account object.

        :param name: Person's first name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self,amount: float) -> bool:
        '''
        This function will deposit the amount of money the user enters

        :param amount: This is the amount to deposit
        :return: Returns a boolean value if successful or not
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    def withdraw(self,amount: float) -> bool:
        '''
        This function will withdraw the amount of money the user enters

        :param amount: This is the amount to withdraw
        :return: Returns a boolean value if successful or not
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    def get_balance(self) -> float:
        '''
        This function will get display the balance of the user

        :return: Returns the account balance of the user
        '''
        return self.__account_balance
    def get_name(self) -> str:
        '''
        This function will display the name of the user

        :return: Returns the account name of the user
        '''
        return self.__account_name