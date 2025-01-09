'''Q3 (25 Points) The Wallet class given in the code below 
will be used in many threads. Modify or rewrite this class to 
be sure that no race condition occurs.'''
import threading
class Wallet:
    def __init__(self): self.balance = 0
    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount): self.balance -= amount
    class Wallet:
        def __init__(self):
            self.balance = 0
            self.lock = threading.Lock()
        def deposit(self, amount):
            with self.lock:
                self.balance += amount
        def withdraw(self, amount):
            with self.lock:
                self.balance -= amount

