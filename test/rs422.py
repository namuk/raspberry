import serial, fcntl, struct

ser = serial.Serial(
	port = '/dev/ttyMAX3',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)

fd = ser.fileno()
serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
fcntl.ioctl(fd, 0x542F, serial_rs485)

while 1:
	ser.write("RS422")
	x = ser.readline()
	print x