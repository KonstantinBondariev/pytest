import RPi.GPIO as GPIO
import time

LED_PIN = 17  # GPIO pin where the LED is connected

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Set pin as an output

def log_pin_states():
  for pin in range(2, 28):  # GPIO pins range from 2 to 27
    try:
      state = GPIO.input(pin)
      print(f"Pin {pin}: {'HIGH' if state else 'LOW'}")
    except RuntimeError:
      print(f"Pin {pin}: Not available")

log_pin_states()

try:
  while True:
    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
    time.sleep(10)  # Wait for 1 second
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
    time.sleep(10)  # Wait for 1 second
except KeyboardInterrupt:
  pass
finally:
  print("Cleaning up")
  GPIO.cleanup()  # Clean up GPIO to reset the pin state


