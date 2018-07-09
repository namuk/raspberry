from gpio import *
import threading

if __name__ == '__main__':
	print("===== GPIO port test =====")
	gpio_init()
	gpio_set()
	gpio_state()
	
	print("===== RS232 port test =====")
	rs232_init()
	if len(rs232) == 2:
		th = threading.Thread(target=rs232_test_read, args=(rs232[1],))
		th.start()
		rs232_test_send(rs232[0])
		th.join()

		th = threading.Thread(target=rs232_test_read, args=(rs232[0],))
		th.start()
		rs232_test_send(rs232[1])
		th.join()

	for i in range(len(rs232)):
		rs232[i].close

	print("===== RS485 port test =====")
	rs485_init()
	if len(rs485) == 2:
		th = threading.Thread(target=rs485_test_read, args=(rs485[1],))
		th.start()
		rs485_test_send(rs485[0])
		th.join()

		th = threading.Thread(target=rs485_test_read, args=(rs485[0],))
		th.start()
		rs485_test_send(rs485[1])
		th.join()

	for i in range(len(rs485)):
		rs485[i].close

	raw_input("RS422 Test. change connect line. Press Enter to continue...")

	print("===== RS422 port test =====")
	#rs485_init()
	if len(rs485) == 2:
		th = threading.Thread(target=rs485_test_read, args=(rs485[1],))
		th.start()
		rs485_test_send(rs485[0])
		th.join()
		
		th = threading.Thread(target=rs485_test_read, args=(rs485[0],))
		th.start()
		rs485_test_send(rs485[1])
		th.join()
	
	for i in range(len(rs485)):
		rs485[i].close