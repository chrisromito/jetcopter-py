from machine import Pin, PWM
from .servo import Servo
from .utils import clamp, microsec_to_duty, scale


class Esc(Servo):
    """
    Esc controller class
    All gas, no brakes

    :param Pin pin: Pin object for the ESC control wire
    :param int pulse_min: Min pulse width in microsec. You can set this
    in your BLHeli config
    :param int pulse_max: Max pulse width in microsec. You can set this
    in your BLHeli config
    :param int freq: PWM signal frequency in hertz.  Most ESCs are 50hz
    """
    def __init__(self, pin, pulse_min=1040, pulse_max=1960, freq=50):
        super().__init__(pin, 100, pulse_min, pulse_max, freq)

    def throttle(self, value):
        """
        :param int value: Throttle value from 0-100
        0 = 0% throttle
        100 = 100% (max) throttle
        """
        return self.to(value)

