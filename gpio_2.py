import RPi.GPIO as GPIO
from time import sleep

def main():
	output0 = 20
	output1 = 21
	output2 = 22
	output3 = 23
	output4 = 24
	output5 = 25
	output6 = 26
	output7 = 27

	input0 = 34
	input1 = 35
	input2 = 36
	input3 = 37
	input4 = 38
	input5 = 39
	input6 = 40
	input7 = 41
	state = 1

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(output0, GPIO.OUT)
	GPIO.setup(output1, GPIO.OUT)
	GPIO.setup(output2, GPIO.OUT)
	GPIO.setup(output3, GPIO.OUT)
	GPIO.setup(output4, GPIO.OUT)
	GPIO.setup(output5, GPIO.OUT)
	GPIO.setup(output6, GPIO.OUT)
	GPIO.setup(output7, GPIO.OUT)

	GPIO.setup(input0, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(input1, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(input2, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(input3, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(input4, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(input5, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(input6, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(input7, GPIO.IN, GPIO.PUD_UP)

	try:
		while True:
			if GPIO.input(input0) == 0:
				while True:
					if GPIO.input(input0) == 1:
						state = not state
						GPIO.output(output0, state)
						sleep(0.2)
						break
			if GPIO.input(input1) == 0:
				while True:
					if GPIO.input(input1) == 1:
						state = not state
						GPIO.output(output1, state)
						sleep(0.2)
						break
			if GPIO.input(input2) == 0:
				while True:
					if GPIO.input(input2) == 1:
						state = not state
						GPIO.output(output2, state)
						sleep(0.2)
						break
			if GPIO.input(input3) == 0:
				while True:
					if GPIO.input(input3) == 1:
						state = not state
						GPIO.output(output3, state)
						sleep(0.2)
						break
			if GPIO.input(input4) == 0:
				while True:
					if GPIO.input(input4) == 1:
						state = not state
						GPIO.output(output4, state)
						sleep(0.2)
						break
			if GPIO.input(input5) == 0:
				while True:
					if GPIO.input(input5) == 1:
						state = not state
						GPIO.output(output5, state)
						sleep(0.2)
						break
			if GPIO.input(input6) == 0:
				while True:
					if GPIO.input(input6) == 1:
						state = not state
						GPIO.output(output6, state)
						sleep(0.2)
						break
			if GPIO.input(input7) == 0:
				while True:
					if GPIO.input(input7) == 1:
						state = not state
						GPIO.output(output7, state)
						sleep(0.2)
						break
	finally:
		print 'end'

if __name__ == '__main__'
	main()