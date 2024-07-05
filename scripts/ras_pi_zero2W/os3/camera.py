# -*- coding: utf-8 -*-

"""
Created on Tue May 28 14:08:22 2024

@author: admin
"""


import cv2 as cv
from datetime import datetime
import os
import time

class Camera:
    def __init__(self):
        self.rec = False
        self.video=None
        self.result=None
        self.file=None
    
    
    def init_capture(self):
        self.video = cv.VideoCapture(0)
        if not self.video.isOpened():
            print("Erreur de lecture du fichier")
            return
        
        
    def rtrn_frames(self):
        ret, frame = self.video.read()
        if ret :
            return frame
        else :
            return None
    
    
    
    def save_frames(self,frame):
        cv.putText(frame,  datetime.now().strftime("%Y-%m-%d %H-%M-%S") , (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1 , cv.LINE_AA)
        self.result.write(frame)

        
                
    def create_file(self):                
         self.file = datetime.now().strftime("%Y-%m-%d %H-%M-%S")   
            
    def set_rec_settings(self,w_fps,cap_fps=24):
        self.video.set(cv.CAP_PROP_FPS, cap_fps)
        self.result = cv.VideoWriter(
                        os.path.join('/home/pi/Desktop/videos', f'{self.file}.avi'), 
                        cv.VideoWriter_fourcc(*'XVID'), w_fps, (640,480))
    

    def turn_off(self):
        if self.video :
            self.video.release()
        if self.result :
            self.result.release()
            print('file saved')


                        
                    
                    #video.set(cv.CAP_PROP_FRAME_WIDTH, 800)
                    #video.set(cv.CAP_PROP_FRAME_HEIGHT, 600)

                    # Set the frame rate
                    #video.set(cv.CAP_PROP_FPS, 30)
                    #w=video.get(3)
                    #h=video.get(4)
                    #print(w)
                    #print(h)
                    #print(video.get(5))
                    
                    
                        

                  

    



