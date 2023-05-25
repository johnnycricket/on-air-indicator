import digitalio
import busio
import board 
from adafruit_epd.epd import Adafruit_EPD
from adafruit_seesaw import seesaw, rotaryio, g
from display.display_init import initDisplay
from display.display_service import makeSquare

# init rotary knob pins
i2c = board.I2C(
    board.SCL1,
    board.SDA1
)

# init eink pins
spi = busio.SPI(
    board.SCK,
    MOSI=board.MOSI,
    MISO=board.MISO
)
cs = digitalio.DigitalInOut(board.RX)
dc = digitalio.DigitalInOut(board.TX)
reset = digitalio.DigitalInOut(board.D4)
busy = digitalio.DigitalInOut(board.D5)
srcs = None

display = initDisplay()

makeSquare(display)