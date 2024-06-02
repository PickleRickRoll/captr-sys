# -*- coding: utf-8 -*-
"""
Created on Wed May 29 02:41:49 2024

@author: admin
"""

import cv2 as cv
import numpy as np

class FaceBlur:
    def __init__(self, model_path='C:\\Users\\admin\\Desktop\\projet stage\\face_blur_models\\'):
        # Load the pre-trained DNN model for face detection
        prototxt_path = model_path + 'deploy.prototxt'
        model_file_path = model_path + 'res10_300x300_ssd_iter_140000.caffemodel'
        self.net = cv.dnn.readNetFromCaffe(prototxt_path, model_file_path)

    def blur(self, frame):
        # Get the frame dimensions
        (h, w) = frame.shape[:2]
        
        # Prepare the frame for DNN face detection
        blob = cv.dnn.blobFromImage(cv.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        self.net.setInput(blob)
        detections = self.net.forward()
        
        # Loop over the detections
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            
            # Filter out weak detections
            if confidence > 0.5:
                # Compute the (x, y)-coordinates of the bounding box
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                
                # Ensure the bounding box coordinates are within the frame dimensions
                startX = max(0, startX)
                startY = max(0, startY)
                endX = min(w, endX)
                endY = min(h, endY)
                
                # Extract the face region
                face_region = frame[startY:endY, startX:endX]
                
                # Apply Gaussian blur to the face region
                face_region = cv.GaussianBlur(face_region, (99, 99), 30)
                
                # Put the blurred face region back into the frame
                frame[startY:endY, startX:endX] = face_region
        
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
