from RPi import GPIO
from time import sleep

class RotaryEncoder:
    def __init__(self, clk_pin, dt_pin):
        self.clk_pin = clk_pin
        self.dt_pin = dt_pin
        self.counter = 0
        

        GPIO.setwarnings(False)  # Ignore warnings
        GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
        GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set clk pin as input
        GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set dt pin as input
        self.clk_last_state = GPIO.input(clk_pin)

    def update(self):
        clk_state = GPIO.input(self.clk_pin)
        dt_state = GPIO.input(self.dt_pin)
        if clk_state != self.clk_last_state:
            if dt_state != clk_state:
                self.counter += 0.5
            else:
                self.counter -= 0.5
            self.counter=max((self.counter),1)
            print(int(self.counter))
        self.clk_last_state = clk_state
        return int(self.counter)


if __name__ == "__main__":
    encoder = RotaryEncoder(clk_pin=16, dt_pin=20)
    try:
        while True:
            encoder.update()
            
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO when the script is interrupted
