from PIL import Image, ImageDraw, ImageFont  # Import PIL modules for image creation and drawing
import cv2 as cv  # Import OpenCV library for computer vision tasks
import math  # Import math module for mathematical functions

class Draw:
    def __init__(self, height, width):
        self.height = height  # Height of the drawing area
        self.width = width  # Width of the drawing area
        # Create an image to draw on
        self.image = Image.new("RGB", (self.height, self.width))  # Create a new RGB image
        self.draw = ImageDraw.Draw(self.image)  # Create a drawing object
        self.font = ImageFont.load_default()  # Load the default font
        self.align = 'center'  # Default alignment
        self.background = (255, 0, 0)  # Background color (B, G, R)
        self.font_color = (255, 255, 255)  # Font color (white)

    # Draws a message at the specified position (x, y)
    def draw_msg(self, message, position):
        # Calculate bounding box for the text
        message_bbox = self.draw.textbbox(position, message, font=self.font)
        message_width = message_bbox[2] - message_bbox[0]
        message_height = message_bbox[3] - message_bbox[1]
        message_x = position[0] - message_width / 2
        message_y = position[1] - message_height / 2
        # Draw the text on the image
        self.draw.text((message_x, message_y), message, font=self.font, fill=self.font_color)

    # Clears the image by drawing a rectangle with the background color
    def clear_img(self):
        self.draw.rectangle([0, 0, self.height, self.width], fill=self.background)

    # Returns the current image
    def rtrn_img(self):
        return self.image

    # Converts an OpenCV image to a PIL image
    def convert(self, image):
        pil_image = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        pil_image = pil_image.resize((self.height, self.width), Image.LANCZOS)
        return pil_image

    # Draws a message with a bounding box at the specified position (x, y) with the specified color
    def bound_mssg(self, message, position, color):
        # Calculate bounding box for the text
        message_bbox = self.draw.textbbox(position, message, font=self.font)
        message_width = message_bbox[2] - message_bbox[0]
        message_height = message_bbox[3] - message_bbox[1]
        message_x = position[0] - message_width / 2
        message_y = position[1] - message_height / 2
        padding = 3  # Padding around the text
        pos = (message_x, message_y)
        bbox = self.draw.textbbox(pos, message, font=self.font)
        expanded_bbox = (bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding)
        # Draw the bounding box around the text
        self.draw.rectangle(expanded_bbox, outline=color, width=1)

    # Draws an arc with text placed along it
    def draw_arc_with_text(self, xy, start, end, fill='white', width=2, text_list=[], font=None):
        self.draw.arc(xy, start, end, fill=fill, width=width)  # Draw the arc
        position = []
        # Compute the bounding box center
        x0, y0, x1, y1 = xy
        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2
        rx = (x1 - x0) / 2
        ry = (y1 - y0) / 2

        # Number of text items
        n = len(text_list)

        if n > 0:
            # Generate angles for text placement
            angles = [start + (end - start) * (i) / (n - 1) for i in range(n)]

            for i, text in enumerate(text_list):
                angle = angles[i]
                angle_rad = math.radians(angle)

                # Position of the text
                tx = cx + (rx) * math.cos(angle_rad) + 1
                ty = cy - (ry + 42) * math.sin(angle_rad) + 10
                position.append((tx, ty))

                tick_length = 5
                tick_width = 1

                tick_start_x = cx + (rx - tick_length) * math.cos(angle_rad)
                tick_start_y = cy - (ry - tick_length) * math.sin(angle_rad)
                tick_end_x = cx + (rx + tick_length) * math.cos(angle_rad)
                tick_end_y = cy - (ry + tick_length) * math.sin(angle_rad)

                # Draw the tick
                self.draw.line([(tick_start_x, tick_start_y), (tick_end_x, tick_end_y)], fill=fill, width=tick_width)

                # Draw the text
                self.draw_msg(text, (tx, ty))
        return position
