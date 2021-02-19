from imu import MPU6050, MPUException


class Orientation:

    def __init__(self, iic):
        self.iic = iic
        self.sensor = MPU6050(self.iic)

