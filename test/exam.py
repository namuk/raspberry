from gpiotest import *
import threading

if __name__ == '__main__':
	print("===== GPIO port test =====")
	gpio_init()
	gpio_set()
	gpio_state()

	print("===== RS232 port test =====")
	rs232_init()
	if len(rs232) == 1:
		rs232_test_send(rs232[0])
		
	for i in range(len(rs232)):
		rs232[i].close

	print("===== RS485 port test =====")
	rs485_init()
	if len(rs485) == 3:
		rs485_test_send(rs485[0])
		rs485_test_send(rs485[2])
		rs485_test_send(rs485[0])
		
	for i in range(len(rs485)):
		rs485[i].close

	print("===== RS422 port test =====")
	#rs485_init()
	if len(rs485) == 3:
		rs485_test_send(rs485[1])

	for i in range(len(rs485)):
		rs485[i].close
