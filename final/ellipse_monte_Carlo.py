#ellipse using the Monte Carlo                                                            
import random, numpy as np, threading
from numba import jit
class AtomicThread(threading.Thread):
    def __init__(self, n, a, b):
        super().__init__()
        self.n: int = n
        self.a: float = a
        self.b: float = b
        self.count: int = 0
@staticmethod
@jit(nopython=True, nogil=True)
def generate(n, a, b):
    count = 0
    for _ in range(n):
        x = random.uniform(0, a)
        y = random.uniform(0, b)
        if (x**2 / a**2 + y**2 / b**2) <= 1:
            count += 1
    return count
def run(self) -> None:
    self.count = self.generate(self.n, self.a, self.b)
def estimate_area(n, m, a, b):
    count = 0
    threads = []
    for _ in range(m):
        threads.append(AtomicThread(n, a, b))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    for thread in threads:
        count += thread.count
    return (count / (n * m)) * (4 * a * b)
def main():
    a, b = 2, 3
    estimated_area, calculated_area = estimate_area(100000, 8, a, b), np.pi * a * b
    print(f"Estimated area: {estimated_area} | Calculated area: {calculated_area}")
    print(f"Error: {abs(estimated_area - calculated_area)}")
if __name__ == "__main__":
    main()