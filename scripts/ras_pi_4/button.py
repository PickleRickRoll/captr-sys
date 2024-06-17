import RPi.GPIO as GPIO

class Button:
    
    def __init__(self,pin):
        self.button_state = False
        self.pushed=False
        GPIO.setwarnings(False)  # Ignore warnings for now
        GPIO.setmode(GPIO.BCM)  # Use Raspberry Pi pin numbering
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin as input
        GPIO.add_event_detect(pin, GPIO.RISING, callback=self.button_callback, bouncetime=200)  # Setup event on pin rising edge

    def button_callback(self, channel):
        self.button_state = not (self.button_state)  # Toggle button state
        self.pushed=True
        print("Button was pushed!")
        

        
    def get_State(self):
        state= [self.button_state,self.pushed]
        self.pushed=False
        return state

    def cleanup(self):
        GPIO.cleanup()  # Clean up

if __name__ == "__main__":
    button = Button(pin=12)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        button.cleanup()  # Clean up when Ctrl+C is pressed
