import time
from machine import Pin
import _thread
from dht import DTH
import pycom
from webhooks import webhooks

# Type 0 = dht11
# Type 1 = dht22
th = DTH('P23', 0)
pycom.heartbeat(False)


def send_env_data():
    while True:
        result = th.read()
        while not result.is_valid():
            time.sleep(.5)
            result = th.read()
        print('Temp:', result.temperature)
        print('RH:', result.humidity)
        try:
            if(result.temperature > 24):
                webhooks.turn_onOff(True)
                webhooks.send_notif(result.temperature, result.humidity)
            else:
                webhooks.turn_onOff(False)
        except:
            pass

        pybytes.send_signal(2,result.temperature)
        pybytes.send_signal(3,result.humidity)

        pycom.rgbled(0x00ff)
        time.sleep(60*30)
        pycom.rgbled(0xff00)

_thread.start_new_thread(send_env_data, ())
