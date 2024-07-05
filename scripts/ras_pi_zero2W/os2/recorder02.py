# -*- coding: utf-8 -*-

"""
Created on Tue May 28 14:08:22 2024

@author: admin
"""
# Enregistrement de vidéo avec boutons start/stop et molette pour changer le frame rate

import cv2 as cv
from datetime import datetime
import os
import time
from button import Button
from rotary_encoder02 import RotaryEncoder
from screen02 import Screen
import board
#from face_blur01 import FaceBlur 

class VideoRecorder:
    def __init__(self,button,molette,screen):
        self.rec = False
        self.button = button
        self.molette=molette
        self.screen=screen
        self.fps=0
        
    def start(self):
        video = None
        result = None
        self.screen.draw_menu()
        

        while True:
            
            
            temp=self.fps
            self.fps=int(self.molette.update())  # Mise à jour du fps pendant l'enregistrement
            self.screen.draw_msg(f'{self.fps}')

            if temp!=self.fps :
                self.screen.disp_img()
            
            if button.get_State()[0]:
                if not self.rec :
                    cv.destroyAllWindows()
                    self.rec = not self.rec
                    print(self.rec)
                    nom_fichier = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    
                    video = cv.VideoCapture(0)
                    video.set(cv.CAP_PROP_FRAME_WIDTH, 640)
                    video.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

                    # Set the frame rate
                    video.set(cv.CAP_PROP_FPS, 30)

                    
                    if not video.isOpened():
                        print("Erreur de lecture du fichier")
                        return
                        

                    print("writing frames", self.fps)
                    # Modifier le chemin d'enregistrement des vidéos si nécessaire
                    #initialisation du fichier pour enregistrer la video 
                    result = cv.VideoWriter(
                        os.path.join('/home/pi/Desktop/videos', f'{nom_fichier}.avi'), 
                        cv.VideoWriter_fourcc(*'XVID'), self.fps, (640,480))

                elif self.rec:
                    self.rec = not self.rec
                    print('hi')
                    if video:
                        video.release()
                    if result:
                        result.release()
                    print("Vidéo enregistrée\n")
                    cv.destroyAllWindows()
                    
            if self.rec:
                #reading frames
                ret, frame = video.read()
                cv.putText(frame,  datetime.now().strftime("%Y-%m-%d %H-%M-%S") , (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1 , cv.LINE_AA)
                
                #writing frames
                if ret:
                    #cv.imshow('Camera Feed', frame)
                    cv.waitKey(1)
                    result.write(frame)
                else:
                    break
        

        # fermer le capturing device et le VideoWriter tout à la fin
        if video:
            video.release()
        if result:
            result.release()
            
        cv.destroyAllWindows()
        


if __name__ == "__main__":
    
    try:
        print('We are On ')
        button=Button(pin=4)
        molette=RotaryEncoder(clk_pin=board.D27, dt_pin=board.D22)
        screen=Screen(user_id='User123')
        
        
        
        recorder = VideoRecorder(button,molette,screen)
        recorder.start()

    except KeyboardInterrupt:
        button.cleanup()
    finally:
        button.cleanup()
    

