from account import *

class Test:
    def setup_method(self):
        self.account1 = Account('Jane', 10)
        self.account2 = Account('John', 20)

    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'Jane'
        assert self.account2.get_name() == 'John'
        assert self.account1.get_balance() == 10
        assert self.account2.get_balance() == 20

    def test_deposit(self):
        assert self.account1.deposit(10) is True
        assert self.account1.get_balance() == 20
        assert self.account2.deposit(10) is True
        assert self.account2.get_balance() == 30

        assert self.account1.deposit(10.5) is True
        assert self.account1.get_balance() == 30.5
        assert self.account2.deposit(10.5) is True
        assert self.account2.get_balance() == 40.5

        assert self.account1.deposit(0) is False
        assert self.account1.get_balance() == 30.5
        assert self.account2.deposit(0) is False
        assert self.account2.get_balance() == 40.5

        assert self.account1.deposit(-1) is False
        assert self.account1.get_balance() == 30.5
        assert self.account2.deposit(-1) is False
        assert self.account2.get_balance() == 40.5

    def test_withdraw(self):
        assert self.account1.withdraw(5) == True
        assert self.account1.get_balance() == 5
        assert self.account2.withdraw(5) == True
        assert self.account2.get_balance() == 15

        assert self.account1.withdraw(2.5) == True
        assert self.account1.get_balance() == 2.5
        assert self.account2.withdraw(2.5) == True
        assert self.account2.get_balance() == 12.5

        assert self.account1.withdraw(0) == False
        assert self.account1.get_balance() == 2.5
        assert self.account2.withdraw(0) == False
        assert self.account2.get_balance() == 12.5

        assert self.account1.withdraw(-1) == False
        assert self.account1.get_balance() == 2.5
        assert self.account2.withdraw(-1) == False
        assert self.account2.get_balance() == 12.5


