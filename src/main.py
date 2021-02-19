import os
import upip
from micropython import const
from machine import I2C, Pin
from time import sleep_ms, sleep
import pycom
from imu import init_imu, get_imu_data



THOUSAND = const(1000)
TIMEOUT = const(1000 * 100)

i2c = I2C(0, I2C.MASTER)


def wait():
    sleep(3)


red = 0x0F0000
green = 0x000F00
blue = 0x00000F
yellow = 0x7f7f00


def render():
    scan = i2c.scan()
    print(scan)
    if len(scan):
        data = get_imu_data(i2c)
        print(data)
    color = (
        green if len(scan)
        else blue
    )
    return color


def test_imu():
    try:    
        pycom.rgbled(yellow)  # Yellow
        wait()
        init_imu(i2c)
        color = render()
        pycom.rgbled(color)
        wait()
    except Exception as err:
        print(err)
        pycom.rgbled(red)
        wait()
    return True


pycom.heartbeat(False)

# App runtime
# ################
def run_app():
    lib = os.listdir('lib')
    if not 'collections' in lib:
        upip.install('micropython-collections', 'lib')
        upip.install('micropython-uasyncio', 'lib')
    return start()


def start():
    from run import runtime
    return runtime()


if __name__ == "__main__":
    run_app()

