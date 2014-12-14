import threading
import time
import csv

class Logger(threading.Thread):
    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.kill_me = False
        self.filename = filename
    
    def get_time(self):
        pass
    
    def run(self):
        self.file = open(self.filename, 'w')
        self.csv = csv.writer(self.file)        
        while not self.kill_me:
            print("running thread!")
            self.csv.writerow(['a', 'b', 'c'])
            time.sleep(1)
        else:
            self.file.close()

    def kill(self):
        self.kill_me = True

if __name__ == '__main__':
    thread = Logger('log.csv')

    thread.start()

    while thread.isAlive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            thread.kill()
            break