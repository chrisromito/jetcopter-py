
def mm_to_m(mm):
    return mm / 1000

# EVERYTHING IN METERS
COPTER_WIDTH = const( mm_to_m(269) )
COPTER_HEIGHT = const( mm_to_m(238) )

"""
COPTER_MOTOR_DISTANCE - Distance from one arm to the center of the copter
Ex. from the tip of the front-right arm to the center of the body

sqrt( square(COPTER_WIDTH / 2) + square(COPTER_HEIGHT / 2) )
"""
COPTER_MOTOR_DISTANCE = const( mm_to_m(180) )

# Weight in Grams = ~1000
COPTER_WEIGHT = const(1000)
