import RPi.GPIO as GPIO
import time

class Button:
    def __init__(self, pin):
        self.pin = pin
        self.button_state = False
        self.pushed = False
        self.last_state = True  # To track the previous state of the button
        GPIO.setwarnings(False)  # Ignore warnings for now
        GPIO.setmode(GPIO.BCM)  # Use Raspberry Pi pin numbering
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin as input

    def update(self):
        self.button_state = GPIO.input(self.pin)
        if self.button_state != self.last_state:  # Check for state change
            if self.button_state == GPIO.HIGH:  # Button pressed
                self.pushed = True
        else:  # Button released
            pass
        self.last_state = self.button_state

    def get_State(self):
        self.update()
        if self.pushed==True :
                print('Button was pushed',self.pushed)
        state = [self.pushed]
        self.pushed=False
        return state

    def cleanup(self):
        GPIO.cleanup()  # Clean up GPIO on exit

if __name__ == "__main__":
    button = Button(pin=4)
    try:
        while True:
            # Example usage of get_state()
            state = button.get_State()
            if state[0]:
                print("Button state:", state)
            time.sleep(0.1)  # Delay to reduce CPU usage
    except KeyboardInterrupt:
        print("\nExiting program")
    finally:
        button.cleanup()  # Clean up when Ctrl+C is pressed
