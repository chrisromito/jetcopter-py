from machine import Pin, PWM
from .utils import clamp, microsec_to_duty


class Servo:
    """
    Params
    :param Pin pin: Pin object for the Servo control wire
    :param int angle: Max angle of the servo.  Ex. my cheapo servo goes from 0-160,
    so I used 160 as the default
    :param int pulse_min: Min pulse width in microsec
    :param int pulse_max: Max pulse width in microsec
    :param int freq: PWM signal frequency in hertz.  Most servos are 50hz
    """
    def __init__(self, pin, angle=160, pulse_min=600, pulse_max=2400, freq=50):
        self.pin = pin
        self.pwm = PWM(self.pin, freq=freq, duty=0)
        self.angle = angle
        self.value = 0
        self.pulse_min = pulse_min
        self.pulse_max = pulse_max
        self.freq = freq

    def to(self, degrees):
        """
        Set the servo angle to "degrees"
        """
        if self.value == degrees:
            return self
        degrees = clamp(0, self.angle, degrees)
        self.value = degrees
        total_range = self.pulse_max - self.pulse_min
        microsec = (total_range * degrees // self.angle) + self.pulse_min
        return self.write_microsec(microsec)

    def write_microsec(self, microsec):
        """
        PWM write a signal "microsec" long
        Pass in a falsy value to disable PWM
        """
        self.pwm.duty(
            microsec_to_duty(self.freq, self.pulse_min, self.pulse_max, microsec)
        )
        return self
