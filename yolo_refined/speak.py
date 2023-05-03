import cv2
import jetson.inference 
import jetson.utils
import numpy as np 
import time
import os
from gtts import gTTS
import threading

print(cv2.__version__)
width=640
height=480
flip=2
speak=True
item='welcome mansoor'
confidence=0
itemOld=""
def sayItem():
    global speak
    global item
    while True:
        if speak==True:
            output=gTTS(text=item,lang='en',slow=False)
            output.save('output.mp3')
            os.system('mpg123 output.mp3')
            speak=False
x=threading.Thread(target=sayItem,daemon=True)
x.start()          



cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
net=jetson.inference.imgageNet('googlenet')
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark= time.time()
fpsFilter=0
while True:
    ret, frame = cam.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(img)
    if speak==False:
        classID,confidence=net.Classify(img,width,height)
        if confidence>= 0.5:
            item=net.GetClassDesc(classID)
            if item!=itemOld:
                speak=True
        if confidence< .5:
            item=''  
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