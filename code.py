import digitalio
import busio
import board 
from adafruit_epd.epd import Adafruit_EPD
from adafruit_epd.ssd1680 import Adafruit_SSD1680 
from adafruit_seesaw import seesaw, rotaryio, g

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

display = Adafruit_SSD1680(
    122,
    250,
    spi,
    cs_pin=cs,
    dc_pin=dc,
    sramcs_pin=srcs,
    rst_pin=reset,
    busy_pin=busy
)

# make red square
display.rotation = 3
display.fill(Adafruit_EPD.WHITE)
display.fill_rect(20,20,50,60, Adafruit_EPD.RED)
display.display()
