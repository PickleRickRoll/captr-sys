import busio
import digitalio
import board
import time
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7735 as st7735
from adafruit_rgb_display import color565

class Screen:
    def __init__(self, user_id):
        self.user_id = user_id
        
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

        # Create an image to draw on
        self.image = Image.new("RGB", ( self.display.height,self.display.width))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()
        #print(self.display.width,self.display.height)
        #width = 128 , height = 160
        #(height.uppins,width.right)

    def draw_menu(self):
        self.draw.rectangle((0, 0, self.display.height, self.display.width), outline=0, fill=(0, 0, 0))

        # Draw the user ID in the top-left corner
        self.draw.text((10, 10), self.user_id, font=self.font, fill=(255, 255, 255))

        # Draw the time in the top-right corner
        current_time = time.strftime("%H:%M:%S")
        bbox = self.draw.textbbox((0, 0), current_time, font=self.font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        self.draw.text((self.display.height - text_width - 5, 10), current_time, font=self.font, fill=(255, 255, 255))

        # Display the image
        self.display.image(self.image)
        
        
    def draw_msg(self, message):
        # Draw the custom message in the center
        #self.image = Image.new("RGB", ( self.display.height,self.display.width))

        message_bbox = self.draw.textbbox((0, 0), message, font=self.font)
        message_width = message_bbox[2] - message_bbox[0]
        message_height = message_bbox[3] - message_bbox[1]
        message_x = (self.display.height - message_width) / 2
        message_y = (self.display.width - message_height) / 2
        self.draw.rectangle([0,0,self.display.height,self.display.width],fill=(255,0,0))
        self.draw.text((message_x, message_y), message, font=self.font, fill=(255, 255, 255))
        
        
        
    def disp_img(self):
        
        # Display the image
        self.display.image(self.image)

        
        
        
        
if __name__ == "__main__":
    screen = Screen(user_id="User123")
    screen.draw_menu()

    while True:
        time.sleep(1)

