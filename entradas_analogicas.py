from gpiozero import MCP3008
from gpiozero import PWMLED
from time import sleep

pot = MCP3008(0)
led = PWMLED(21)

led.source = pot.values

while True:
	print(pot.value)