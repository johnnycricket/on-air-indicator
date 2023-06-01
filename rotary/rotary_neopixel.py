from rainbowio import colorwheel
from adafruit_seesaw import neopixel
from rotary.rotary_color_enum import Color

def init_neopixel(seesaw):
    return neopixel.NeoPixel(seesaw, 6, 1)

def change_color(pixel: neopixel, color: float):
    pixel.fill(colorwheel(color))

def set_brightness(pixel: neopixel, intensity: bool):
    if(intensity):
        pixel.brightness = min(1.0, pixel.brightness + 0.1)
    else:
        pixel.brightness = max(0, pixel.brightness - 0.1)