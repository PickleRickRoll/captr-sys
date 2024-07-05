import busio
import digitalio
import board
import time
import adafruit_rgb_display.st7735 as st7735
from adafruit_rgb_display import color565

class Screen:
    def __init__(self):
        
        
        # Config for display baudrate (default max is 24mhz):
        BAUDRATE = 24000000
        
        
        # Initialize SPI bus
        self.spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        # Configure the display
        self.display = st7735.ST7735R(
            self.spi,
            cs=digitalio.DigitalInOut(board.CE0), #gpio pin 8 , CE0
            dc=digitalio.DigitalInOut(board.D23),  # GPIO 23, Pin 16
            rst=digitalio.DigitalInOut(board.D24),   # GPIO 24, Pin 18
            baudrate=BAUDRATE
        )
        self.display.rotation = 90  # Landscape mode
        self.height=self.display.height
        self.width=self.display.width
        
        #print(self.display.width,self.display.height)
        #width = 128 , height = 160
        #(height.uppins,width.right)

    
        
    def disp_img(self,image):
        
        # Display the image
        self.display.image(image)

        
        
        
        
if __name__ == "__main__":
    screen = Screen()
    #screen.fill(0x7521)
    screen.pixel(64,64,0)
    


