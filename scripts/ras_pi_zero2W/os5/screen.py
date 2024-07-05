import busio  # Import the busio module for handling SPI communication
import digitalio  # Import the digitalio module for handling GPIO pins
import board  # Import the board module to handle pin names
import adafruit_rgb_display.st7735 as st7735  # Import the display driver for ST7735

class Screen:
    def __init__(self):
        # Config for display baudrate (default max is 24mhz):
        BAUDRATE = 24000000  # Set the SPI communication speed
        
        # Initialize SPI bus
        self.spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)  # Create SPI bus object
        # Configure the display
        self.display = st7735.ST7735R(
            self.spi,
            cs=digitalio.DigitalInOut(board.CE0),  # Chip select pin, do not change (GPIO pin 8, CE0)
            dc=digitalio.DigitalInOut(board.D23),  # Data/command pin, can be changed (GPIO pin 23)
            rst=digitalio.DigitalInOut(board.D24),  # Reset pin, can be changed (GPIO pin 24)
            baudrate=BAUDRATE  # Set the SPI baudrate
        )
        self.display.rotation = 90  # Set display orientation to landscape mode
        self.height = self.display.height  # Get display height
        self.width = self.display.width  # Get display width
        
        # Print display dimensions (commented out)
        # print(self.display.width, self.display.height)
        # width = 128, height = 160

    def disp_img(self, image):
        # Display the image on the screen
        self.display.image(image)



if __name__ == "__main__":
    screen = Screen()  # Initialize the Screen object