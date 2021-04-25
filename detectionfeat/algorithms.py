import cv2 
import numpy 


def detect_face(img_file, img_name):

    face_cascade = cv2.CascadeClassifier('detectionfeat/cascades/haarcascade_frontalface.xml')
    
    img = cv2.imread(img_file,1)
    
  
    face_img = img.copy()
  
    face_rects = face_cascade.detectMultiScale(face_img) 
    
    for (x,y,w,h) in face_rects: 
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,0,0), 10) 
        
    
    return face_img