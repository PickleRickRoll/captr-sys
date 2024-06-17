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
from rotary_encoder import RotaryEncoder
from led import LED
#from face_blur01 import FaceBlur 

class VideoRecorder:
    def __init__(self,button,molette,err,on,rec,upld):
        self.rec = False
        self.button = button
        self.molette=molette
        self.upld_led=upld
        self.rec_led=rec
        self.err_led=err
        self.on_led=on
        
    def start(self):
        video = None
        result = None
        self.on_led.turn_on()
        

        while True:
            fps=int(self.molette.update())  # Mise à jour du fps pendant l'enregistrement
            if self.button.get_State()[1]:
                if button.get_State()[0]:
                    cv.destroyAllWindows()
                    self.rec = True
                    nom_fichier = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    
                    video = cv.VideoCapture(0)
                    video.set(cv.CAP_PROP_FRAME_WIDTH, 640)
                    video.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

                    # Set the frame rate
                    video.set(cv.CAP_PROP_FPS, 30)

                    
                    if not video.isOpened():
                        print("Erreur de lecture du fichier")
                        self.err_led.turn_on()
                        return
                    

                    print("writing frames", fps)
                    # Modifier le chemin d'enregistrement des vidéos si nécessaire
                    #initialisation du fichier pour enregistrer la video 
                    result = cv.VideoWriter(
                        os.path.join('/home/abc/Desktop/projet stage/videos', f'{nom_fichier}.mp4	'), 
                        cv.VideoWriter_fourcc(*'MJPG'), fps, (640,480))

                elif not button.get_State()[0]:
                    self.rec = False
                    if video:
                        video.release()
                    if result:
                        result.release()
                    print("Vidéo enregistrée\n")
                    self.rec_led.turn_off()
                    self.upld_led.turn_off()
                    cv.destroyAllWindows()


            if self.rec:
                #reading frames
                self.rec_led.blink()
                ret, frame = video.read()
                cv.putText(frame,  datetime.now().strftime("%Y-%m-%d %H-%M-%S") , (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1 , cv.LINE_AA)
                
                #writing frames
                if ret:
                    cv.imshow('Camera Feed', frame)
                    cv.waitKey(1)
                    self.upld_led.blink()
                    result.write(frame)
                else:
                    self.err_led.turn_on()
                    break
                

        # fermer le capturing device et le VideoWriter tout à la fin
        if video:
            video.release()
        if result:
            result.release()
            
        self.rec_led.turn_off()
        self.on_led.turn_off()
        self.upld_led.turn_off()
        cv.destroyAllWindows()
        


if __name__ == "__main__":
    
    try:
        print('We are On ')
        button=Button(pin=12)
        molette=RotaryEncoder(clk_pin=16, dt_pin=20)
        
        err_led=LED(pins=[26])
        on_led=LED(pins=[4])
        rec_led=LED(pins=[27],blink_interval=10)
        upld_led=LED(pins=[22],blink_interval=10)
        
        rec_led.turn_off()
        err_led.turn_off()
        on_led.turn_off()
        upld_led.turn_off()
        
        
        recorder = VideoRecorder(button,molette,err=err_led,on=on_led,rec=rec_led,upld=upld_led)
        recorder.start()

    except KeyboardInterrupt:
        button.cleanup()
    finally:
        button.cleanup()
    
