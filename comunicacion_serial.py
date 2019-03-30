from time import Sleep
import serial
microcontrolador = serial.Serial('/dev/ttyACM0', 9600)

while True:
	comando = input('Introduce un comando: ')
	microcontrolador.write(comando.encode())
	if comando == 'H':
		print('LED Encendido')
	elif comando == 'L':
		print('LED Apagado')