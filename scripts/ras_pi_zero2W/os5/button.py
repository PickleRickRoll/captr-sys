import RPi.GPIO as GPIO  # Import the RPi.GPIO library for controlling GPIO pins
import time  # Import the time library for handling time-related functions

class Button:
    def __init__(self, pin):
        self.pin = pin  # GPIO pin number
        self.button_state = False  # Current state of the button
        self.pushed = False  # Flag for simple push detection
        self.long_press = False  # Flag for long press detection
        self.start = 0  # Time when the button was first pressed

        self.last_state = True  # To track the previous state of the button
        GPIO.setwarnings(False)  # Ignore warnings for now
        GPIO.setmode(GPIO.BCM)  # Use Raspberry Pi pin numbering
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin as input with pull-up resistor

    def update(self):
        # Update the button state
        self.button_state = GPIO.input(self.pin)  # Read the button state
        if self.button_state != self.last_state:  # Check for state change
            if self.button_state == GPIO.HIGH:  # Button is pressed
                self.pushed = True  # Set pushed flag
        else:  # Button released
            pass
        self.last_state = self.button_state  # Update last state

        # Check for long press
        if self.button_state == GPIO.LOW:  # If button is pressed
            temp = time.time()  # Get current time
            timer = temp - self.start  # Calculate time elapsed since button was pressed
            if timer > 6.0:  # Long press detected (change this number to adjust long press duration)
                self.long_press = True  # Set long press flag
                self.start = time.time()  # Reset start time

        if self.button_state == GPIO.HIGH:  # If button is released
            self.start = time.time()  # Reset start time

    def get_State(self):
        self.update()  # Update the button state
        if self.pushed == True:
            print('Button was pushed', self.pushed)  # Print message if button was pushed
        if self.long_press == True:
            print('Button was pushed', self.long_press)  # Print message if button was long pressed

        state = [self.pushed, self.long_press]  # Return the state as a list
        self.pushed = False  # Reset pushed flag
        self.long_press = False  # Reset long press flag
        return state  # Return the button state

    def cleanup(self):
        GPIO.cleanup()  # Clean up GPIO on exit


'''
You can run this code to verify if your button works properly
'''

if __name__ == "__main__":
    button = Button(pin=3)  # Initialize the Button object with pin 3
    try:
        while True:
            # Example usage of get_state()
            state = button.get_State()  # Get the button state
            if state[0]:
                print("Button state:", state)  # Print the button state if pushed
            time.sleep(0.1)  # Delay to reduce CPU usage
            if state[1]:
                print("Button state:", state)  # Print the button state if long pressed
    except KeyboardInterrupt:
        print("\nExiting program")  # Print message on keyboard interrupt
    finally:
        button.cleanup()  # Clean up when Ctrl+C is pressed
