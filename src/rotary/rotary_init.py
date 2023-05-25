import digitalio
import busio
import board 
from adafruit_seesaw import seesaw, rotaryio, g

def init():
    i2c = board.I2C(
        board.SCL1,
        board.SDA1
    )

    return seesaw.Seesaw(i2c, addr=0x36)

 