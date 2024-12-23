import threading
import time

semaphore = threading.Semaphore(2)

def task