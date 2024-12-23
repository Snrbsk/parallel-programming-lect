import threading
import time
import random

#class fork (threading.Lock): custom lock demeseydi

class Fork:
    def __init__(self, index: int):
        self.index = index
        self.lock = threading.Lock()
        self.picked_up = False
        self.owner = -1
        
    def __enter__(self):
        return self

    def __call__(self, owner: int, *args, **kwargs):
        if self.lock.acquire():
            self.owner = owner
            self.picked_up = True
            print(self)
        return self
    
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.lock.release() #kilidi geri bırak
        self.picked_up = False
        self.owner = -1

    def __str__(self):
        return f"F{self.index:2d} {self.owner:2d}"
    
class Philosopher(threading.Thread):
    def __init__(
            self,
            index: int,
            left_fork: Fork, 
            right_fork: Fork,
            spagetti: int
        ):
            super().__init__(name=f"Philosopher {index:2d}")
            self.index = index
            self.left_fork = left_fork
            self.right_fork = right_fork
            self.spagetti = spagetti
            self.eating = False

    def run(self):
        while self.spagetti > 0:
            self.think()
            self.eat_with_odd()

    def think(self):
        time.sleep(3 + random.random() * 3)

    def eat(self):
        #with kullanarak context manager, parantezlerle callable kullandık
        with self.left_fork(self.index):
            time.sleep(5 + random.random()*5)
            with self.right_fork(self.index):
                self.spagetti -= 1
                self.eating = True
                print(self)
                time.sleep(5 + random.random()*5)
                self.eating = False

    def eat_with_odd(self):
        if self.index % 2 == 0:
            first_fork = self.left_fork
            second_fork = self.right_fork
        else:
            first_fork = self.right_fork
            second_fork = self.left_fork
        with first_fork(self.index):
            time.sleep(5 + random.random()*5)
            with second_fork(self.index):
                self.spagetti -= 1
                self.eating = True
                print(self)



    def __str__(self):
        return f"P{self.index:2d} {self.spagetti:2d}"

if __name__ == "__main__":
    n = 5
    m = 7

    forks = [Fork(i) for i in range(n)]
    philosophers = [
        Philosopher(i, forks[i], forks[(i+1) % n], m) 
        for i in range(n)
    ]
    for philosopher in philosophers:
        philosopher.start()
    for philosopher in philosophers:
        philosopher.join()