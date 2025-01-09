#euler number

import random, multiprocessing, os, math

def estimate_e(n, pipe):
    count = 0
    for _ in range(n):
        sum = 0
        while sum <= 1:
            sum += random.random()
            count += 1
    pipe.send(count)
def accuracy(estimated_value):
    return abs(estimated_value - math.e)

if __name__ == "__main__":
    BATCH_SIZE = 100000
    NUM_BATCHES = os.cpu_count()
    total = 0
    number_of_iterations = 0
    while True:
        pipes = []
        processes = []
        for i in range(NUM_BATCHES):
            recv_end, send_end = multiprocessing.Pipe(False)
            pipes.append(recv_end)
            process = multiprocessing.Process(
            target=estimate_e, args=(BATCH_SIZE, send_end)
            )
            processes.append(process)
            process.start()
        for pipe in pipes:
            total += pipe.recv()
        for process in processes:
            process.join()
        number_of_iterations += NUM_BATCHES * BATCH_SIZE
        estimated_value = total / number_of_iterations
        print(f"Estimated value of e is {estimated_value} 
              with {accuracy(estimated_value)}")
        if accuracy(estimated_value) < 1.0e-6:
            break
        