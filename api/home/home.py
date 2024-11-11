from .power_meter import PowerMeter
from .circuit_breaker import CircuitBreaker
from .load import Load

class Home:
    def __init__(self, config=None):
        self.circuit_breaker = CircuitBreaker(config['circuit_breaker'] if config else None)
        self.power_meter = PowerMeter(serial_number=config['power_meter']['sn'] if config else "123456")
        self.voltage = config['power_meter']['voltage'] if config else 230
        self.load = Load(self.circuit_breaker.get_max_current() / 10) # 10% of max current
        self.load.register_callback(self.current_updated)
        
    def current_updated(self):
        total_current = self.load.current
        if self.circuit_breaker.is_on() and total_current < self.circuit_breaker.get_max_current():
            self.power_meter.update_current(total_current)
        else:
            self.power_meter.update_current(0)
