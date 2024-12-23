import threading
import time
import random

barrier = threading.Barrier(3)

def worker(thread_id):
    print(f"T-{thread_id}: Reached the barrier")
    time.sleep(3+ random.random()*10)
    print(f"T-{thread_id} is ready")
    barrier.wait()
    print(f"T-{thread_id}: Passed the barrier")

threads = [
    
]


