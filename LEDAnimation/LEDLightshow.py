# HW 1: LED ASSIGNMENT - FALL 2022
# DESERT MEDIA ART
# CODE BY: MAITHA ALGHFELI
# MORSE CODE LIGHT SHOW

# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# START ----------------------------->

# CODE DEVELOPED FROM: CircuitPython Essentials Internal RGB LED red, green, blue example
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

# I WANT THE LED TO BE VERY BRIGHT
led.brightness = 0.3


# FUNCTION DEFINITION

# TAKE USER INPUT FOR THE MORSE LIGHT SHOW
def userInput():
    global phrase
    print("Turn your text into Morse here: https://morsecode.world/international/translator.html then copy it into your input.")
    print()
    phrase = input("Enter your Morse code: ")

#FUNCTION DEFINITION

# SHORT MORSE IS JUST A DOT, IT LOOKS LIKE THIS "."
def shortMorse():
    led[0] = (255, 53, 184)
    time.sleep(0.2)
    led[0] = (0, 0, 0)
    time.sleep(0.1)

# LONG MORSE IS A DASH, AND IT LOOKS LIKE THIS "-"
def longMorse():
    led[0] = (255, 53, 184)
    time.sleep(0.7)
    led[0] = (0, 0, 0)
    time.sleep(0.1)

# JUMP MORSE IS A FORWARD FACING SLASH, AND IT LOOKS LIKE THIS "/"
def jumpMorse():
    led[0] = (0, 0, 0)
    time.sleep(0.7)

# SPACE MORSE IS SIMPLY A SPACE BETWEEN EACH MORSE SET, AND IT LOOKS LIKE THIS " "
def spaceMorse():
    led[0] = (0, 0, 0)
    time.sleep(0.3)


# FIRST STEP IS TAKING THE INPUTED PHRASE
userInput()

# NOW THAT WE HAVE THE PHRASE, THE MORSE CODE LIGHT SHOW BEGINS!!
while True:

#   READ EACH CHARACTER IN THE MORSE STRING
    for i, v in enumerate(phrase):
#       CHECK HOW EACH CHARACTER RELATES TO OUR FUNCTIONS
        if v == "-":
            longMorse() #DISPLAY FUNCTION
            phrase = phrase[1:] #REMOVE THE CHARACTER FROM THE MORSE STRING
            print(phrase) #PRINT THE NEW MORSE STRING FOR REFERENCE
#       THE SAME REPEATS FOR EVERY CHARACTER AND FUNCTION
        elif v == ".":
            shortMorse()
            phrase = phrase[1:]
            print(phrase)
        elif v == " ":
            spaceMorse()
            phrase = phrase[1:]
            print(phrase)
        elif v == "/":
            jumpMorse()
            phrase = phrase[1:]
            print(phrase)

#       WHEN THE MORSE STRING IS EMPTY, THE CODE PLAYS AGAIN
        if phrase == "":
            led[0] = (0, 255, 0)
            userInput()


# END ----------------------------->

# Write your code here :-)
