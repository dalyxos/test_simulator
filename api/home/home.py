from .power_meter import PowerMeter
from .circuit_breaker import CircuitBreaker
from .load import Load

def_config = {
    "power_meter": {
        "sn": "123456",
        "voltage": 230,
        "udp_host": "0.0.0.0",
        "udp_port": 5000
    },
    "circuit_breaker": {
        "max_current": 100
    }
}
class Home:
    def __init__(self, config=None):
        self.config = config if config else def_config
        self.circuit_breaker = CircuitBreaker(self.config['circuit_breaker']) 
        self.power_meter = PowerMeter(config=self.config['power_meter'])
        self.load = Load(self.circuit_breaker.get_max_current() / 10) # 10% of max current
        self.load.register_callback(self.current_updated)
        
    def current_updated(self):
        total_current = self.load.current
        if self.circuit_breaker.is_on() and total_current < self.circuit_breaker.get_max_current():
            self.power_meter.update_current(total_current)
        else:
            self.power_meter.update_current(0)
