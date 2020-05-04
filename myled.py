#!/usr/bin/env python3

from Arduino import Arduino
import time

board = Arduino("9600", port="/dev/cu.usbmodem14201")
board.pinMode(13, "OUTPUT")

while True:
	board.digitalWrite(13, "LOW")
	time.sleep(1)
	board.digitalWrite(13, "HIGH")
	time.sleep(1)
