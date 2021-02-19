
MILLION = const(1000000)

MAX_DUTY = const(1023)


def scale(from_min, from_max, to_min, to_max):
    to_diff = to_max - to_min
    from_diff = from_max - from_min
    def _scale(value):
        return value - from_min * to_diff / from_diff + to_min
    return _scale


def clamp(lower, upper, value):
    return max(lower, min(value, upper))


def microsec_to_duty(freq, pulse_min, pulse_max, microsec):
    width = clamp(pulse_min, pulse_max, microsec)
    return ((width * MAX_DUTY) * freq) // MILLION

