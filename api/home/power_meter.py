import threading
import socket
import time


default_voltage = 230

class PowerMeter:
    def __init__(self, config, current=0):
        self.serial_number = config['sn']
        self.current = current
        self.udp_host = config['udp_host']
        self.udp_port = config['udp_port']
        self.start_streaming()

    def read_meter(self):
        return {'current': self.current, 'power': self.current * default_voltage, 'voltage': default_voltage}

    def update_current(self, new_reading):
        self.current = new_reading

    def start_streaming(self):
        thread = threading.Thread(target=self.stream_data)
        thread.daemon = True
        thread.start()
        
    def stream_data(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            data = f"Serial: {self.serial_number}, Current: {self.read_meter()}"
            sock.sendto(data.encode(), (self.udp_host, self.udp_port))
            time.sleep(1)
