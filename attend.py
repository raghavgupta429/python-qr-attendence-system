#scanning the qr code
import cv2
import sys
import pyzbar.pyzbar as pyzbar
import numpy as np
import pybase64
import time


#start the webcam
cap = cv2.VideoCapture(0)

names =[]

#function for attendence file

fob= open('attendence.txt','a+')
def enterData(z):
    if z in names:
        pass
    else: 
        names.append(z)
       # z=''.join(str(z))
        print(z)        
        fob.write(z+'\n')       
    return names

print('Reading code.........')


#function data present or not

def checkData(data):
    data = str(data)
    if data in names:
        print ('Already Present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'Present Done')
        enterData(data)
        
#Webcam read
while True:
    _,frame = cap.read()
    decodedObject= pyzbar.decode(frame)
    for obj in decodedObject:
       checkData(obj.data)
       
       time.sleep(1)
    
    cv2.imshow('Frames',frame)
    
    #closing the program when s is pressed
    if cv2.waitKey(1)&0xFF== ord('s'):
        cv2.destroyAllWindows()
        break
fob.close()
    