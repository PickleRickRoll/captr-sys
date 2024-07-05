# -*- coding: utf-8 -*-

"""
Created on Tue May 28 14:08:22 2024

@author: admin
"""

import cv2 as cv  # Import OpenCV library for computer vision tasks
from datetime import datetime  # Import datetime module for handling date and time
import os  # Import os module for interacting with the operating system

class Camera:
    def __init__(self):
        self.video = None  # Variable to hold the video capture object
        self.result = None  # Variable to hold the video writer object
        self.file = None  # Variable to hold the filename

    def init_capture(self):
        self.video = cv.VideoCapture(0)  # Initialize video capture from the default camera
        if not self.video.isOpened():  # Check if the camera opened successfully
            print("Error opening the camera")  # Print error message if the camera did not open
            return

    def rtrn_frames(self):
        ret, frame = self.video.read()  # Read a frame from the video capture
        if ret:
            return frame  # Return the frame if read successfully
        else:
            return None  # Return None if frame not read

    def save_frames(self, frame):
        cv.putText(frame, datetime.now().strftime("%Y-%m-%d %H-%M-%S"), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv.LINE_AA)
        # Overlay the current date and time on the frame
        self.result.write(frame)  # Write the frame to the video file

    def create_file(self):
        self.file = datetime.now().strftime('%m-%d__%H:%M')  # Generate a filename based on the current date and time

    # Change your video directory here
    def set_rec_settings(self, wfps, dimensions):
        self.video.set(cv.CAP_PROP_FRAME_WIDTH, dimensions[0])  # Set the width of the video capture
        self.video.set(cv.CAP_PROP_FRAME_HEIGHT, dimensions[1])  # Set the height of the video capture
        self.result = cv.VideoWriter(
            os.path.join('/home/pi/Desktop/videos', f'{self.file}__{dimensions[0]}x{dimensions[1]}.avi'),
            cv.VideoWriter_fourcc(*'XVID'), wfps, dimensions)
        # Initialize video writer to save the video to a file with the specified resolution and frame rate

        '''
        # You can do more testing of the camera here if you want
        
        w = self.video.get(3)  # Get the width of your capture
        h = self.video.get(4)  # Get the height of your capture
        print(w)  # Print the width
        print(h)  # Print the height
        print(self.video.get(5))  # Get the FPS of your capture and print it
        print(wfps)  # Print the desired frame rate
        '''

    def turn_off(self):
        if self.video:
            self.video.release()  # Release the video capture object
        if self.result:
            self.result.release()  # Release the video writer object
            print('file saved')  # Print message indicating the file was saved

