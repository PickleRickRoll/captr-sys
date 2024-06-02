# -*- coding: utf-8 -*-
"""
Created on Wed May 29 02:34:47 2024

@author: admin
"""

import cv2 as cv

class FaceBlur:
    def __init__(self):
        # Load the pre-trained Haar cascade classifier for face detection
        self.face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def blur(self, frame):
        # Convert the frame to grayscale because face detection works on grayscale images
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv.CASCADE_SCALE_IMAGE)
        
        # Loop over the detected faces and apply a blur to each face region
        for (x, y, w, h) in faces:
            # Extract the face region
            face_region = frame[y:y+h, x:x+w]
            
            # Apply Gaussian blur to the face region
            face_region = cv.GaussianBlur(face_region, (99, 99), 30)
            
            # Put the blurred face region back into the frame
            frame[y:y+h, x:x+w] = face_region
        
        return frame

# Example usage:
if __name__ == "__main__":
    face_blur = FaceBlur()
    
    # Open a video capture device
    video = cv.VideoCapture(0)
    
    if not video.isOpened():
        print("Erreur de lecture du fichier")
        exit()
    
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Apply face blur
        frame = face_blur.blur(frame)
        
        # Display the frame with blurred faces
        cv.imshow('Camera Feed', frame)
        
        # Exit loop on 'q' key press
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    video.release()
    cv.destroyAllWindows()
