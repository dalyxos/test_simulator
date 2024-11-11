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
        self.start_streaming(self, self.udp_host, self.udp_port)

    def read_meter(self):
        return self.current

    def update_current(self, new_reading):
        self.current = new_reading

    def start_streaming(self, ip='255.255.255.255', port=5000):
        thread = threading.Thread(target=self.stream_data, args=(self, ip, port))
        thread.daemon = True
        thread.start()
        
    def stream_data(self, power_meter, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            data = f"Serial: {power_meter.serial_number}, Current: {power_meter.read_meter()}"
            sock.sendto(data.encode(), (ip, port))
            time.sleep(1)
