import numpy as np
import cv2 



def detect_face(img_file, img_name):

    img = cv2.imread(img_file, 1)


    face_cascade = cv2.CascadeClassifier('cascades/face.xml')
    
  
    face_img = img.copy()
  
    face_rects = face_cascade.detectMultiScale(face_img) 
    
    for (x,y,w,h) in face_rects: 
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10) 
        
    
    result_file = cv2.imwrite(img_name, face_img)

    return result_file

    