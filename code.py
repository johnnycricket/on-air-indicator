from rotary.rotary_init import init_rotary, init_encoder, init_switch
from rotary.rotary_neopixel import init_neopixel, change_color, set_brightness
# from display.display_init import initDisplay

# init rotary knob pins
rotary = init_rotary()
encoder = init_encoder(rotary)
switch = init_switch(rotary)
pixel = init_neopixel(rotary)

# init eink pins
# display = initDisplay()

while True:
    position = -encoder.position

    if position != last_position:
        print(position)

        if switch.value:
            if position > last_position:
                color += 1
            else:
                color -= 1
            color = (color + 256) % 256
            change_color(pixel, color)
        else:
            if position > last_position:
                set_brightness(pixel, bool(True))
            else:
                set_brightness(pixel, bool(False))

    last_position = position