# -*- coding: utf-8 -*-

"""
Created on Tue May 28 14:08:22 2024

@author: admin
"""
# Enregistrement de vidéo avec boutons start/stop et molette pour changer le frame rate

import cv2 as cv
from datetime import datetime
import keyboard
import os
import time
from face_blur02 import FaceBlur

class VideoRecorder:
    def __init__(self):
        self.rec = False
        self.button = False
        self.fps  = 30   

    def molette(self):
        if keyboard.is_pressed('right'):
            self.fps += 1
            self.fps = min(max(self.fps, 1), 30)
            print('fps = ', self.fps)
            time.sleep(0.1) 
            
        if keyboard.is_pressed('left'):
            self.fps -= 1
            self.fps = min(max(self.fps, 1), 30)
            print('fps = ', self.fps)
            time.sleep(0.1) 
        
        return self.fps

    def start(self,faceblur):
        video = None
        result = None

        while True:
            if  keyboard.is_pressed('q'):
                break
            
            fps=self.molette()  # Mise à jour du fps pendant l'enregistrement
            if keyboard.is_pressed('space'):
                cv.destroyAllWindows()
                self.button = not self.button
                print('button = ', self.button)
                # Petit délai pour éviter plusieurs détections de la barre d'espace
                while keyboard.is_pressed('space'):
                    pass

                if self.button:
                    self.rec = True
                    nom_fichier = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    video = cv.VideoCapture(0) 
                    video.set(5,fps)
                    if not video.isOpened():
                        print("Erreur de lecture du fichier")
                        return
                    # 3 corresponds to the property CV_CAP_PROP_FRAME_WIDTH
                    frame_width = int(video.get(3))
                    frame_height = int(video.get(4))
                    size = (frame_width, frame_height)
                    print("actual_________frame", int(video.get(5)))
                    print('molette -----fps=',fps)
                    # Modifier le chemin d'enregistrement des vidéos si nécessaire
                    #initialisation du fichier pour enregistrer la video 
                    result = cv.VideoWriter(
                        os.path.join('C:\\Users\\admin\\Desktop\\projet stage\\videos', f'{nom_fichier}.avi'), 
                        cv.VideoWriter_fourcc(*'XVID'), fps, size)

                else:
                    self.rec = False
                    if video:
                        video.release()
                    if result:
                        result.release()
                    print("Vidéo enregistrée\n")

            if self.rec:
                #reading frames 
                ret, frame = video.read()
                cv.putText(frame,  datetime.now().strftime("%Y-%m-%d %H-%M-%S") , (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1 , cv.LINE_AA)
                frame=faceblur.blur(frame)
                cv.imshow('Camera Feed', frame)
                cv.waitKey(1)
                #writing frames
                if ret: 
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
    faceblur=FaceBlur()
    print('We are On ')
    recorder = VideoRecorder()
    recorder.start(faceblur)
    print('shutting downq')
    