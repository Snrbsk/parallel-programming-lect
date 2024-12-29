import multiprocessing
import os
import string
import hashlib
import aiohttp
import asyncio
import requests
import time
import threading
import sys

class BruteForcer:
    def __init__(self, set_start_method='fork'):
        self.set_start_method = set_start_method
        self.num_processes = os.cpu_count()
        self.pool = []
        self.result = None
        

    def queue_control(self, q):
        while not self.result:
            if not q.empty():
                password = q.get()
                if asyncio.run(self.check_password(password)):
                    self.result = password
                    break
            else:
                time.sleep(1)   

    def __enter__(self):
        self.get_hashed_password()
        multiprocessing.set_start_method(self.set_start_method)
        q = multiprocessing.Queue()

        # queue_control fonksiyonunu ayrı bir thread'de çalıştır
        threading.Thread(target=self.queue_control, args=(q,), daemon=True).start()

        for length in range(3,6):
            self.batch_size = self.calculate_batch_size(self.num_processes, length)
            for i in range(self.num_processes):
                process = multiprocessing.Process(target=self.brute_force, args=(q, self.batch_size, i, length))
                process.start()
                self.pool.append(process)      
            for process in self.pool:
                process.join()

        return self
    
    def get_hashed_password(self):
        response = requests.get('http://127.0.0.1:5000/get_password')
        if response.status_code == 200:
            json_response = response.json()
            self.password = json_response.get('password')
        else:
            raise Exception('Failed to get password')

    async def check_password(self, password):
        async with aiohttp.ClientSession() as session:
            async with session.post('http://127.0.0.1:5000/check_password', json={'password': password}) as response:
                if response.status == 200:
                    json_response = await response.json()
                    return json_response.get('message') == 'Success'
                else:
                    raise Exception('Failed to check password')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Çıkış yapıldığında tüm süreçleri sonlandır
        self.terminate_processes()

    def terminate_processes(self):
        # Tüm süreçleri sonlandır
        for process in self.pool:
            process.terminate()
        print("Tüm süreçler sonlandırıldı.")

    def brute_force(self, q, batch_size, offset, length):
        current = self.calculate_start(batch_size, offset, length)
        print(f'Process {os.getpid()} started with start: {current} \n')
        for i in range(batch_size):
            hashed_current = hashlib.md5(current.encode()).hexdigest()
            if self.password == hashed_current:
                q.put(current)
            current = self.increment(current)

    def calculate_start(self, batch_size, offset, length):
        def to_base_62(num):
            chars = string.digits + string.ascii_letters
            if num == 0:
                return chars[0]
            result = []
            while num > 0:
                result.append(chars[num % 62])
                num = num // 62
            return "".join(result[::-1])

        # Başlangıç numarasını hesapla
        start_num = batch_size * offset
        
        # Taban 62'ye çevir ve uzunluğa göre sıfırlarla doldur
        start_num = to_base_62(start_num).rjust(length, string.digits[0])
        return start_num

    @staticmethod
    def calculate_batch_size(num_processes, length):
        total_combinations = 62 ** length
        combination_per_process = total_combinations // num_processes
        return combination_per_process

    @staticmethod
    def increment(str):
        chars = list(string.digits + string.ascii_letters)
        list_str = list(str)
        for i in range(len(list_str)-1, -1, -1):
            if list_str[i] == chars[-1]:
                list_str[i] = chars[0]
                if i == 0:
                    list_str.insert(0, chars[0])
            else:
                list_str[i] = chars[chars.index(list_str[i]) + 1]
                break
        return ''.join(list_str)


if __name__ == '__main__':
    with BruteForcer() as bf:
        print(f'Found password: {bf.result}')
