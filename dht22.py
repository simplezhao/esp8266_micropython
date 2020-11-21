
import dht
from machine import Pin
import time
dht22 = dht.DHT22(Pin(5))
time.sleep(1)

def get_humi_temp():
    dht22.measure()
    print('dht22: {}%, {}℃'.format(dht22.humidity(), dht22.temperature()))


while True:
    get_humi_temp()
    time.sleep(2)