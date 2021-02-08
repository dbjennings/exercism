import threading

class BankAccount:
    def __init__(self):
        self.account_open = False
        self.balance = 0
        self._lock = threading.Lock() 

    def get_balance(self):
        if self.account_open:
            return self.balance
        raise ValueError("No balance on a closed account.")

    def open(self):
        if self.account_open: raise ValueError("Account already open.")
        self.account_open = True

    def deposit(self, amount):
        if amount<0: raise ValueError("Can't deposit negative amount")
        if self.account_open:
            with self._lock: self.balance+=amount
            return
        raise ValueError("Can't deposit in a closed account.")

    def withdraw(self, amount):
        if amount<0: raise ValueError("Can't withdraw negative amount")
        if self.account_open:
            if self.balance<amount: raise ValueError("Not enough balance.")
            with self._lock: self.balance-=amount
            return
        raise ValueError("Can't deposit in a closed account.")

    def close(self):
        if not self.account_open: raise ValueError("Account already closed")
        self.account_open = False
        self.balance=0
