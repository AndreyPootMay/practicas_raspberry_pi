from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	print("Se ha detectado movimiento")
	pir.wait_for_no_motion()
	print("Se ha dejado de detectar movimiento")