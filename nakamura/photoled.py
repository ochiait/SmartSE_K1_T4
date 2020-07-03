import wiringpi as pi, time
import line_notifier as ln

from enum import Enum
class State(Enum):
        dark = 0
        bright = 1

led_pin = 4
cds_pin = 18
state = State.dark

pi.wiringPiSetupGpio()
pi.pinMode(led_pin, 1)
pi.pinMode(cds_pin, 0)

while True:
    if (pi.digitalRead(cds_pin) == 1):
        pi.digitalWrite(led_pin, 0)
	# print("**state before = ", state, ", after = bright")
	if (state == State.dark):
		ln.notify()
		time.sleep(10)
	state = State.bright
    else:
        pi.digitalWrite(led_pin, 1)
	# print("**state before = ", state, ", after = dark")
	state = State.dark