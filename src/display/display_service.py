def makeSquare(display):
    # make red square
    display.rotation = 3
    display.fill(Adafruit_EPD.WHITE)
    display.fill_rect(20,20,50,60, Adafruit_EPD.RED)
    display.display()