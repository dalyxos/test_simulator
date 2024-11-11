
class CircuitBreaker:
    def __init__(self, config=None):
        self.max_current = config['max_current']
        self.status = True

    def is_on(self):
        return self.status
    
    def turn_off(self):
        self.status = False
        
    def turn_on(self):
        self.status = True
        
    def get_max_current(self):
        return self.max_current
    
    def set_max_current(self, new_current):
        self.max_current = new_current