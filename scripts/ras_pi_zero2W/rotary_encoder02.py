import digitalio
import board
import time

class RotaryEncoder:
    def __init__(self, clk_pin, dt_pin):
        self.clk_pin = digitalio.DigitalInOut(clk_pin)
        self.dt_pin = digitalio.DigitalInOut(dt_pin)

        self.clk_pin.direction = digitalio.Direction.INPUT
        self.clk_pin.pull = digitalio.Pull.UP

        self.dt_pin.direction = digitalio.Direction.INPUT
        self.dt_pin.pull = digitalio.Pull.UP

        self.last_clk_state = self.clk_pin.value
        self.position = 0

    def update(self):
        clk_state = self.clk_pin.value
        dt_state = self.dt_pin.value

        if clk_state != self.last_clk_state:
            if dt_state != clk_state:
                self.position += 1
            else:
                self.position -= 1

            print(f"Position: {self.position}")
        
        self.last_clk_state = clk_state
        return self.position


if __name__ == "__main__":
    encoder = RotaryEncoder(clk_pin=board.D5, dt_pin=board.D6)
    try:
        while True:
            encoder.update()
            time.sleep(0.001)
            
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO when the script is interrupted

