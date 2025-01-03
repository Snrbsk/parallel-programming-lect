import time
import tracemalloc

def performance(func):

    setattr(performance, 'counter', 0)
    setattr(performance, 'total_time', 0.0)
    setattr(performance, 'total_memory', 0.0)

    def _performance(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        setattr(performance, 'counter', getattr(performance,'counter') + 1)
        setattr(performance, 'total_time', getattr(performance,'total_time') + (end_time-start_time))
        setattr(performance, 'total_memory', getattr(performance,'total_memory') + peak_memory)
        return result
    return _performance

@performance
def for_dongusu():
    for i in range(100):
        for i in range(100):
            for i in range(100):
                i = i ** 17

for_dongusu()
for_dongusu()

# Display results
print(f"Function was called {performance.counter} times")
print(f"Total execution time: {performance.total_time:.6f} seconds")
print(f"Total memory used: {performance.total_memory:.6f} MB")