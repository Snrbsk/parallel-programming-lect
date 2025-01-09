'''
RandomGenerator should inherit from the Process 
class of the multiprocessing module.
RandomGenerator should be a daemon process.
The main function tries to drain the queue every 
second. RandomGenerator should fill the queue
 with random numbers constantly.'''
import multiprocessing, random, time
class RandomGenerator(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.daemon = True 

    def run(self):
        while True:
            random_number = random.randint(1, 100) 
            self.queue.put(random_number)  
            time.sleep(0.5) 
def main():
    queue = multiprocessing.Queue()
    generator = RandomGenerator(queue)
    generator.start()
    while True:
        while not queue.empty():
            print(queue.get())
        time.sleep(1)
if __name__ == "__main__":
    main()


