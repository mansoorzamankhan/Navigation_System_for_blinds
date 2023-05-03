import cv2
from cv2 import threshold
import jetson.inference 
import jetson.utils
import numpy as np 
import time
import os
from gtts import gTTS
import threading
import pyttsx3

print(cv2.__version__)
width=640
height=480
flip=2
##text to speach 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
speak=True
item='welcome  to the object recognition module , i will recognize what is arround you '
confidence=0
itemOld=""
def voice(str):
    engine.say(str)
    engine.runAndWait()

cam=cv2.VideoCapture(0)
def sayItem():
    global speak
    global item
    while True:
        if speak==True:
            voice(item)
            speak=False
x=threading.Thread(target=sayItem,daemon=True)
x.start()          




cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
net=jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark= time.time()
fpsFilter=0
while True:
    ret, frame = cam.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(img)
    
    detection=net.Detect(img,width,height)
    for detect in detection :
        ID=detect.ClassID
        top=int(detect.Top)
        left=int(detect.Left)
        bottom=int(detect.Bottom)
        right= int(detect.Right)
        item=net.GetClassDesc(ID)
        cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),1)
        cv2.putText(frame,item,(left,top+20),font,.75, (0,255,0),2)
        if speak==False:
        
            if item!=itemOld:
                speak=True
            if item==itemOld:
                speak=False  
        itemOld=item      
    dt=time.time()-timeMark
    timeMark=time.time()
    fps=1/dt
    fpsFilter=0.95*fpsFilter + 0.05*fps
    cv2.putText(frame,str(round(fpsFilter,1))+'  FPS  '+item+"    "+str(round(confidence,2)),(0,30),font,1,(0,0,255),2)


    cv2.imshow('nanoCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()