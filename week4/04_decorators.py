import time
import tracemalloc

def performance(func):
    performance.counter = 0
    performance.time = 0
    performance.memory_usage = 0 

    def _dec(*args, **kwargs):
        performance.counter += 1
        start_time = time.time()
        tracemalloc.start()

        snapshot1 = tracemalloc.take_snapshot()

        result = func(*args, **kwargs)

        snapshot2 = tracemalloc.take_snapshot()
        tracemalloc.stop()

        end_time = time.time()

        performance.time += end_time-start_time
        performance.memory_usage += snapshot2.compare_to(snapshot1, "lineno")[0].size_diff

        print(f"Function calls: {performance.counter}")
        print(f"Total execution time: {performance.time:.6f} seconds")
        print(f"Memory usage difference: {performance.memory_usage} bytes")
        return result
    
    return _dec

@performance
def say_hi():
    for i in range(1,100):
        for j in range(1,100):
            print("",end="")

say_hi()
say_hi()