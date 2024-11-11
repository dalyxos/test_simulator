import time
from flask import Flask

from home.home import Home

home = Home()

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/load')
def get_load():
    return {'load': home.load.current}

@app.route('/power-meter')
def get_power_meter():
    return {'powerMeter': home.power_meter.read_meter()}

@app.route('/circuit-breaker')
def get_circuit_breaker():
    return {'circuitBreaker': home.circuit_breaker.is_on()}