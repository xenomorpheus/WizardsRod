#!/usr/bin/python3

import smbus
import math

class AccelerometerDemo:

    # 0x68 This is the address value read via the i2cdetect command
    address = 0x68

    # Power management registers
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    def __init__(self, bus_num:int, address:int) -> None:
        self.bus = smbus.SMBus(bus_num)
        self.address = address

    def read_byte(self, adr:int):
        return self.bus.read_byte_data(self.address, adr)

    def read_word(self, adr:int):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(self, adr:int):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, AccelerometerDemo.dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, AccelerometerDemo.dist(x,z))
        return math.degrees(radians)

    def run(self) -> None:
        # Now wake the 6050 up as it starts in sleep mode
        self.bus.write_byte_data(self.address, AccelerometerDemo.power_mgmt_1, 0)

        print("gyro data")
        print("---------")

        gyro_xout = self.read_word_2c(0x43)
        gyro_yout = self.read_word_2c(0x45)
        gyro_zout = self.read_word_2c(0x47)

        print("gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131))
        print("gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131))
        print("gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131))

        print()
        print("accelerometer data")
        print("------------------")

        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0

        print("accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled)
        print("accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled)
        print("accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled)

        print("x rotation: " , AccelerometerDemo.get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
        print("y rotation: " , AccelerometerDemo.get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))

if __name__ == "__main__":
    # bus_num=1 for Revision 2 boards
    ad = AccelerometerDemo(bus_num=1, address=AccelerometerDemo.address)
    ad.run()

