"""
    Source: https://micronote.tech/2020/07/I2C-Bus-with-a-NodeMCU-and-MicroPython/
"""
from micropython import const
from machine import I2C, Pin


MPU6050_ADDR = const(0x68)

MPU6050_ACCEL_XOUT_H = const(0x3B)
MPU6050_ACCEL_XOUT_L = const(0x3C)
MPU6050_ACCEL_YOUT_H = const(0x3D)
MPU6050_ACCEL_YOUT_L = const(0x3E)
MPU6050_ACCEL_ZOUT_H = const(0x3F)
MPU6050_ACCEL_ZOUT_L = const(0x40)
MPU6050_TEMP_OUT_H = const(0x41)
MPU6050_TEMP_OUT_L = const(0x42)
MPU6050_GYRO_XOUT_H = const(0x43)
MPU6050_GYRO_XOUT_L = const(0x44)
MPU6050_GYRO_YOUT_H = const(0x45)
MPU6050_GYRO_YOUT_L = const(0x46)
MPU6050_GYRO_ZOUT_H = const(0x47)
MPU6050_GYRO_ZOUT_L = const(0x48)
MPU6050_PWR_MGMT_1 = const(0x6B)

MPU6050_LSBC = const(340.0)
MPU6050_TEMP_OFFSET = const(36.53)
MPU6050_LSBG = const(16384.0)
MPU6050_LSBDS = const(131.0)


def init_imu(i2c):
    i2c.writeto_mem(MPU6050_ADDR, MPU6050_PWR_MGMT_1, bytes([0]))


def combine_register_values(h, l):
    h_one = h[0]
    l_one = l[0]
    if not h_one & 0x80:
        return h_one << 8 | l_one
    return -((h_one ^ 255) << 8) |  (l_one ^ 255) + 1


def get_temp(i2c):
    """
    :param I2C i2c: Bus for the IMU
    :returns int: Temperature in celcius
    """
    temp_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_TEMP_OUT_H, 1)
    temp_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_TEMP_OUT_L, 1)
    return (combine_register_values(temp_h, temp_l) / MPU6050_LSBC) + MPU6050_TEMP_OFFSET


def get_accel(i2c):
    """
    :param I2C i2c: Bus for the IMU
    :returns float[]: x, y, z in g's
    """
    accel_x_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 1)
    accel_x_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_L, 1)
    accel_y_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_H, 1)
    accel_y_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_L, 1)
    accel_z_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_H, 1)
    accel_z_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_L, 1)
    return [
        combine_register_values(accel_x_h, accel_x_l) / MPU6050_LSBG,
        combine_register_values(accel_y_h, accel_y_l) / MPU6050_LSBG,
        combine_register_values(accel_z_h, accel_z_l) / MPU6050_LSBG
    ]


def get_gyro(i2c):
    """
    :param I2C i2c: Bus for the IMU
    :returns float[]: x, y, z in degrees / second
    """
    gyro_x_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_XOUT_H, 1)
    gyro_x_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_XOUT_L, 1)
    gyro_y_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_YOUT_H, 1)
    gyro_y_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_YOUT_L, 1)
    gyro_z_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_ZOUT_H, 1)
    gyro_z_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_ZOUT_L, 1)
    return [
        combine_register_values(gyro_x_h, gyro_x_l) / MPU6050_LSBDS,
        combine_register_values(gyro_y_h, gyro_y_l) / MPU6050_LSBDS,
        combine_register_values(gyro_z_h, gyro_z_l) / MPU6050_LSBDS
    ]


def get_imu_data(i2c):
    return {
        'temp': get_temp(i2c),
        'accel': get_accel(i2c),
        'gyro': get_gyro(i2c)
    }
        

