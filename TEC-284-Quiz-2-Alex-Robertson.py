from gpiozero import LED, Button

redLED = LED(23)
greenLED = LED(24)
blueLED = LED(25)

redButton = Button(16)
greenButton = Button(21)
blueButton = Button(20)

def turnRed():
    # turns the LED red
    redLED.on()

def turnBlue():
    # turns the LED blue
    blueLED.on()

def turnGreen():
    # turns the LED green
    greenLED.on()

def clear():
    # clears the LED of all colors
    redLED.off()
    blueLED.off()
    greenLED.off()

while True:
    if redButton.is_pressed:
        turnRed()
    else:
        redLED.off()
        
    if greenButton.is_pressed:
        turnGreen()
    else:
        greenLED.off()
        
    if blueButton.is_pressed:
        turnBlue()
    else:
        blueLED.off()