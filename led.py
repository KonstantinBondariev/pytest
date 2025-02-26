import RPi.GPIO as GPIO
import time

LED_PIN = 17  # GPIO pin where the LED is connected

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Set pin as an output

try:
  while True:
    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
    time.sleep(1)  # Wait for 1 second
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
    time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()  # Clean up GPIO to reset the pin state


