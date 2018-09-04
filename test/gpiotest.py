import RPi.GPIO as GPIO
import time
import serial
import fcntl
import struct

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

inputs = [34,35,36,37,38,39,40,41]
outputs = [20,21,22,23,24,25,26]

port485 = ['/dev/ttyMAX1', '/dev/ttyMAX2', '/dev/ttyMAX3']
speed485 = 115200
timeout485 = 1

port232 = ['/dev/ttyMAX0']
speed232 = 115200
timeout232 = 1

test_state = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

rs485 = []
rs232 = []

def gpio_init():
	for i in outputs:
		GPIO.setup(i, GPIO.OUT)
	for i in inputs:
		GPIO.setup(i, GPIO.IN)

def gpio_set():
	for i in outputs:
		state = GPIO.input(i)
		if (state == 0):
			time.sleep(0.1)
			GPIO.output(i, 1)
		else:
			time.sleep(0.1)
			GPIO.output(i, 0)

def gpio_state():
	for i in outputs:
		state = GPIO.input(i)
		print("output port " + str(i) + " state : "+ str(state))

	for i in inputs:
		state = GPIO.input(i)
		print("input port " + str(i) + " state : "+ str(state))

def rs485_init():
	for i in range(len(port485)):
		rs485.append(
			serial.Serial(
				port=port485[i],
				baudrate=speed485,
				timeout=timeout485,
				parity=serial.PARITY_NONE,
				stopbits=serial.STOPBITS_ONE,
				bytesize=serial.EIGHTBITS
			)
		)
		fd = rs485[i].fileno()
		serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
		fcntl.ioctl(fd,0x542F,serial_rs485)

def rs485_test_send(port):
	for i in test_state:
		port.write(i)
	s = port.readline()
	print(port.port + ":" + s)

def rs485_test_read(port):
	count = 0
	str = ""
	while count < len(test_state):
		s = port.read(1)
		str = str + s
		count = len(str)
	print(port.port + ":" + str)

def rs485_close(port):
	port.close()

def rs232_init():
	for i in range(len(port232)):
		rs232.append(
			serial.Serial(
				port=port232[i],
				baudrate=speed232,
				timeout=timeout232,
				parity=serial.PARITY_NONE,
				stopbits=serial.STOPBITS_ONE,
				bytesize=serial.EIGHTBITS
			)
		)

def rs232_test_send(port):
	for i in test_state:
		port.write(i)
	s = port.readline()
	print(port.port + ":" + s)

def rs232_test_read(port):
	count = 0
	str = ""
	while count < len(test_state):
		s = port.read(1)
		str = str + s
		count = len(str)
	print(port.port + ":" + str)
	
def rs232_close(port):
	port.close()
