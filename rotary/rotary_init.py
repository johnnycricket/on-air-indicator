import board 
from adafruit_seesaw import seesaw, rotaryio, digitalio

def init_rotary():
    i2c = board.STEMMA_I2C() 
    newSee = seesaw.Seesaw(i2c, addr=0x36)
    newSee.pin_mode(24, newSee.INPUT_PULLUP)
    return newSee

def init_encoder(seesaw):
    return rotaryio.IncrementalEncoder(seesaw)

def init_switch(seesaw):
    return digitalio.DigitalIO(seesaw, 24)