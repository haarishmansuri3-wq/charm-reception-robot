import RPi.GPIO as GPIO

GREEN_LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.output(GREEN_LED_PIN, GPIO.LOW)

def led_on():
GPIO.output(GREEN_LED_PIN, GPIO.HIGH)

def led_off():
GPIO.output(GREEN_LED_PIN, GPIO.LOW)

