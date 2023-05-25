import digitalio
import busio
import board
from adafruit_epd.ssd1680 import Adafruit_SSD1680 

def initDisplay():
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

    return Adafruit_SSD1680(
        122,
        250,
        spi,
        cs_pin=cs,
        dc_pin=dc,
        sramcs_pin=srcs,
        rst_pin=reset,
        busy_pin=busy
    )

