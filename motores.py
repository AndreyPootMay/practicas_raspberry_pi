from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice
from time import sleep

pinA = OutputDevice(2)
pinB = OutputDevice(3)
pinE = OutputDevice(4)

while True:
	for i in range(1,11):
		speed=i/10
		print(speed)
		pinA.on()
		pinB.off()
		pinE.value = speed
		sleep(0.5)
	pinA.off()
	sleep(2)
while True:
	for i in range(1,11)
		speed=i/10
		print(speed)
		pinA.off()
		pinB.on()
		pinE.value = speed
		sleep(0.5)
	pinB.off()
	sleep(2)