import wiringpi as pi, time
import line_notifier as ln

led_pin = 4
cds_pin = 18

pi.wiringPiSetupGpio()
pi.pinMode(led_pin, 1)
pi.pinMode(cds_pin, 0)

while True:
    if (pi.digitalRead(cds_pin) == 1):
        pi.digitalWrite(led_pin, 0)
    else:
        # 暗くなったらLINEを送る 実際にはポストの中なので明るくなったら送るようにすべき
        pi.digitalWrite(led_pin, 1)
        ln.notify()
