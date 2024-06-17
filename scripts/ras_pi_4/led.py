import RPi.GPIO as GPIO
import time

class LED:
    def __init__(self, pins, blink_interval=100):
        # Use the BCM GPIO numbering
        GPIO.setmode(GPIO.BCM)
        
        # List of GPIO pins for LEDs
        self.led_pins = pins
        
        # Set all LED pins as output
        for pin in self.led_pins:
            GPIO.setup(pin, GPIO.OUT)
        
        self.state = False
        self.counter = 0
        self.blink_interval = blink_interval  # Interval in terms of loop iterations

    def blink(self):
        self.counter += 1
        if self.counter >= self.blink_interval:
            self.counter = 0
            self.state = not self.state
            if self.state:
                self.turn_on()
            else:
                self.turn_off()
    
    def turn_on(self):
        for pin in self.led_pins:
            GPIO.output(pin, GPIO.HIGH)
    
    def turn_off(self):
        for pin in self.led_pins:
            GPIO.output(pin, GPIO.LOW)
    
    def cleanup(self):
        # Clean up GPIO settings
        GPIO.cleanup()

# Example usage
if __name__ == "__main__":
    led_pins = [26]  # GPIO pins to which LEDs are connected
    led = LED(led_pins, blink_interval=100)
    
    try:
        while True:
            led.turn_off()
            # Simulate doing other tasks
            # Replace this with your actual main loop code
            # A small sleep to prevent high CPU usage (optional)
            time.sleep(0.01)
    except KeyboardInterrupt:
        led.cleanup()
    finally:
        GPIO.cleanup()   
