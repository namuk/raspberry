from gpiotest import *
import threading

if __name__ == '__main__':
	gpio_init()	
	rs232_init()
	rs485_init()
	
	while 1:
		print("===== GPIO port test =====")
		gpio_set()
		gpio_state()

		print("===== RS232 port test =====")
		rs232_test_send(rs232[0])
		
		for i in range(len(rs232)):
			rs232[i].close

		print("===== RS485 port test =====")
		rs485_test_send(rs485[0])
		rs485_test_send(rs485[2])
		
		for i in range(len(rs485)):
			rs485[i].close
	
		print("===== RS422 port test =====")
		#rs485_init()
		rs485_test_send(rs485[1])
	
		for i in range(len(rs485)):
			rs485[i].close
