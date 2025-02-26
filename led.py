import RPi.GPIO as GPIO
import time

LED_PIN = 17  # GPIO pin where the LED is connected
BTN_PIN = 22  # GPIO pin where the button is connected

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Set pin as an output
GPIO.setup(BTN_PIN, GPIO.IN)  # Set pin as an input


try:
  while True:
   
    if GPIO.input(BTN_PIN) == GPIO.HIGH:
      GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on
    else:
      GPIO.output(LED_PIN, GPIO.LOW)  # Turn off
    time.sleep(0.1)  # Wait for a short time

except KeyboardInterrupt:
  pass
finally:
  print("Cleaning up")
  GPIO.cleanup()  # Clean up GPIO to reset the pin state



