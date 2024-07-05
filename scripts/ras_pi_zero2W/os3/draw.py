from PIL import Image, ImageDraw, ImageFont,ImageChops
import time
import cv2 as cv

class Draw :
    
    
    def __init__(self,user_id,height,width):
        
        self.height=height
        self.width=width
        # Create an image to draw on
        self.image = Image.new("RGB", ( self.height,self.width))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()
        self.id=user_id
        
    
    
    
    
    def draw_icons(self):
        #self.draw.rectangle((0, 0, self.height, self.width), outline=0, fill=(0, 0, 0))

        # Draw the user ID in the top-left corner
        self.draw.text((10, 10), self.id, font=self.font, fill=(255, 255, 255))

        # Draw the time in the top-right corner
        current_time = time.strftime("%H:%M:%S")
        bbox = self.draw.textbbox((0, 0), current_time, font=self.font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        self.draw.text((self.height - text_width - 5, 10), current_time, font=self.font, fill=(255, 255, 255))

   #position=(x,y) 
    def draw_msg(self, message,position):
        
        # Draw the custom message in the center

        message_bbox = self.draw.textbbox(position, message, font=self.font)
        message_width = message_bbox[2] - message_bbox[0]
        message_height = message_bbox[3] - message_bbox[1]
        message_x = position[0] -message_width/2
        message_y = position[1] -message_height/2
        
        self.draw.text((message_x, message_y), message, font=self.font, fill=(255, 255, 255))
        
    
    def clear_img(self):
        self.draw.rectangle([0,0,self.height,self.width],fill=(255,0,0))
    
    
    def rtrn_img(self):
        return self.image

    
    
    def convert(self,image):
        pil_image = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        pil_image = pil_image.resize((self.height, self.width), Image.LANCZOS)
        return pil_image
    
    
    
    def bound_mssg(self,message,position,color):
        
        message_bbox = self.draw.textbbox(position, message, font=self.font)
        message_width = message_bbox[2] - message_bbox[0] 
        message_height = message_bbox[3] - message_bbox[1] 
        message_x = position[0] -message_width/2
        message_y = position[1] -message_height/2
        padding=5
        pos=(message_x,message_y)
        bbox = self.draw.textbbox(pos, message, font=self.font)
        expanded_bbox = (bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding)
        self.draw.rectangle(expanded_bbox, outline=color, width=1)
