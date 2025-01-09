#File Watcher with Deamon Thread
import time, os, threading
def sleep_for_a_while(n):
    time.sleep(n)
def last_modification_time(path):
    return os.path.getmtime(path)
class FileWatcher(threading.Thread):
    def __init__(self, path, interval=1):
        super().__init__()
        self.path = path
        self.interval = interval
        self.last_mod_time = \
        last_modification_time(path)
        self.daemon = True
    def run(self):
        while True:
            if last_modification_time(self.path) != \
                    self.last_mod_time:
                print("File has changed")
                self.last_mod_time = \
                    last_modification_time(self.path)
            sleep_for_a_while(self.interval)
if __name__ == "__main__":
    watcher = FileWatcher(path="test.txt", n=1)
    watcher.start()
    while True:
        sleep_for_a_while(1)
        print("Main thread is running")
