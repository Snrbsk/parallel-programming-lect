import multiprocessing
import os
import string
import hashlib
import time
import threading


class BruteForcer:
    def __init__(self, password, set_start_method='fork'):
        self.set_start_method = set_start_method
        self.num_processes = os.cpu_count()
        self.pool = []
        self.result = None
        self.password = password

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.terminate_processes()

    def __enter__(self):
        multiprocessing.set_start_method(self.set_start_method, force=True)
        q = multiprocessing.Queue()

        threading.Thread(target=self.queue_control, args=(q,), daemon=True).start()

        for length in range(1, 7):
            if self.result:
                break
            self.batch_size = self.calculate_batch_size(self.num_processes, length)
            for i in range(self.num_processes):
                process = multiprocessing.Process(target=self.brute_force, args=(q, self.batch_size, i, length))
                process.start()
                self.pool.append(process)
            for process in self.pool:
                process.join()
        return self

    def brute_force(self, q, batch_size, offset, length):
        current = self.calculate_start(batch_size, offset, length)
        print(f'Process {os.getpid()} started with start: {current}')
        for i in range(batch_size):
            hashed_current = hashlib.md5(current.encode()).hexdigest()
            if self.password == hashed_current:
                q.put(current)
                return  # Şifre bulunduğunda işlemi sonlandır
            current = self.increment(current)

    def queue_control(self, q):
        while not self.result:
            if not q.empty():
                self.result = q.get()
                print(f'Password found: {self.result}')
            else:
                time.sleep(1)
        self.terminate_processes()

    def terminate_processes(self):
        for process in self.pool:
            if process.is_alive():
                process.terminate()
        print("Tüm süreçler sonlandırıldı.")

    @staticmethod
    def calculate_start(batch_size, offset, length):
        def to_base_27(num):
            chars = string.ascii_lowercase + ' '
            if num == 0:
                return chars[0]
            result = []
            while num > 0:
                result.append(chars[num % 27])
                num = num // 27
            return ''.join(result[::-1])

        start_num = batch_size * offset
        return to_base_27(start_num).rjust(length, 'a')

    @staticmethod
    def calculate_batch_size(num_processes, length):
        total_combinations = 27 ** length
        combination_per_process = total_combinations // num_processes
        return combination_per_process

    @staticmethod
    def increment(base27_str):
        chars = string.ascii_lowercase + ' '
        list_str = list(base27_str)
        for i in range(len(list_str) - 1, -1, -1):
            if list_str[i] == chars[-1]:
                list_str[i] = chars[0]
                if i == 0:
                    list_str.insert(0, chars[0])
            else:
                list_str[i] = chars[chars.index(list_str[i]) + 1]
                break
        return ''.join(list_str)


if __name__ == '__main__':
    start_time = time.time()
    with BruteForcer('4015e9ce43edfb0668ddaa973ebc7e87') as bf:
        print(f'Found password: {bf.result}')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Time taken: {elapsed_time} seconds')
