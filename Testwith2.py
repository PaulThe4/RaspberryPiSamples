import cv2
import os

dest = '/home/gsurats1/Desktop'
os.chdir(dest)
interval = 5

cap1 = cv2.VideoCapture(0)
cap1.set(3,640)   
cap1.set(4,480)  
cap2 = cv2.VideoCapture(2)
cap2.set(3,640)   
cap2.set(4,480)  

while True:
    ret1,frame1 = cap1.read()
    cv2.imshow('Live1',frame1)
    
    ret2,frame2 = cap2.read()
    cv2.imshow('Live2',frame2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
#while True:
 #   ret2,frame2 = cap2.read()
  #  cv2.imshow('Live2',frame2)
    
   # if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break
        
cap1.release()
cap2.release()

cv2.destroyAllWindows()
