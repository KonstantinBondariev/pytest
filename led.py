import RPi.GPIO as GPIO
import time

LED_PIN = 17  # GPIO pin where the LED is connected

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Set pin as an output

print("Turning LED ON")
GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
time.sleep(2)  # Wait for 2 seconds

print("Turning LED OFF")
GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED OFF

print("Turning LED ON")
GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
time.sleep(2)  # Wait for 2 seconds

print("Turning LED OFF")
GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED OFF

print("Turning LED ON")
GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
time.sleep(2)  # Wait for 2 seconds

print("Turning LED OFF")
GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED OFF

GPIO.cleanup()  # Clean up GPIO to reset the pin state
