import digitalio  # Import the digital I/O module for handling GPIO pins
import board  # Import the board module to handle pin names
import time  # Import the time module for handling timing functions

class RotaryEncoder:
    def __init__(self, clk_pin, dt_pin):
        self.clk_pin = digitalio.DigitalInOut(clk_pin)  # Initialize the clock pin
        self.dt_pin = digitalio.DigitalInOut(dt_pin)  # Initialize the data pin

        self.clk_pin.direction = digitalio.Direction.INPUT  # Set the clock pin as input
        self.clk_pin.pull = digitalio.Pull.UP  # Enable pull-up resistor on the clock pin

        self.dt_pin.direction = digitalio.Direction.INPUT  # Set the data pin as input
        self.dt_pin.pull = digitalio.Pull.UP  # Enable pull-up resistor on the data pin

        self.last_clk_state = self.clk_pin.value  # Store the initial state of the clock pin
        self.position = 0  # Initialize the position counter

    def update(self):
        clk_state = self.clk_pin.value  # Read the current state of the clock pin
        dt_state = self.dt_pin.value  # Read the current state of the data pin

        if clk_state != self.last_clk_state and clk_state == False:  # Check if clock state has changed to LOW
            if dt_state != clk_state:
                self.position += 1  # Increment position if data state is different from clock state
            else:
                self.position -= 1  # Decrement position if data state is the same as clock state

            # print(f"Position: {self.position}")  # Print the current position (commented out)
        
        self.last_clk_state = clk_state  # Update the last clock state
	time.sleep(0.0001)
        return self.position  # Return the current position

    def set_pos(self, pos):
        self.position = pos  # Set the position counter to the specified value


'''
You can run this code to verify if your encoder works properly
'''

if __name__ == "__main__":
    encoder = RotaryEncoder(clk_pin=board.D27, dt_pin=board.D22)  # Initialize the RotaryEncoder with specified pins
    a = 0
    try:
        while True:
            start = time.time()  # Record the start time
            temp = encoder.update()  # Update the encoder position
            react = start - time.time()  # Calculate the reaction time
            if a != temp:
                print('index=', temp, 'reactivity=', react)  # Print the position and reaction time if position changed
                a = temp

            # time.sleep(0.001)  # Optional sleep to reduce CPU usage (commented out)
            
    except KeyboardInterrupt:
        pass  # Do nothing on keyboard interrupt (Ctrl+C)
