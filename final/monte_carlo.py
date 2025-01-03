import random
import math 

inner = 0
total = 0
def calculate_pi():
    global inner, total
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    r2 = x**2 + y**2
    r = math.sqrt(r2)

    total = total + 1
    if r < 1:
        inner += 1
        
    return inner, total

for i in range(10000000):
    calculate_pi()
    print(inner)
pi = 4 * inner / total

print(pi)