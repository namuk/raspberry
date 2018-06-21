import time, serial

ser = serial.Serial(
	port = '/dev/ttyMAX0',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)

while 1:
	ser.write("COM1\r\n")
	x = ser.read(1)
	print x