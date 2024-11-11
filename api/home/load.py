import threading
import random
import time

class Load:
    def __init__(self, max_current):
        print(f"Initializing load with max current: {max_current}") 
        self.max_current = max_current
        self.current = 0
        self.callback = None
        self.load_thread = threading.Thread(target=self.generate_load)
        self.load_thread.daemon = True
        self.load_thread.start()
    
    def generate_load(self):
        while True:
            self.current = random.randint(0, self.max_current * 100) / 100
            if self.callback:
                self.callback()
            time.sleep(1)
            
    def register_callback(self, callback):
        self.callback = callback
