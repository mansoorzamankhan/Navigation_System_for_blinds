import cv2
import os
import numpy as np
from gtts import gTTS
import threading
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import pyttsx3
##text to speach 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
speak=True
item='welcome to Face recognition module, i will recognize Persons arround you '
itemOld=""
def voice(str):
    engine.say(str)
    engine.runAndWait()

def sayItem():
  global speak
  global item
  while True:
    if speak==True:
      voice(item)
      
      speak=False
x=threading.Thread(target=sayItem,daemon=True)
x.start()  


#from PIL import Image
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = load_model(filepath='recognizer.h5')

#X = np.zeros((6,224,224,3),dtype=np.uint8)
#for i,file in enumerate(os.listdir('/home/hassan/FYP_data/test/')):
#  X[i] = cv2.cvtColor(cv2.resize(cv2.imread('/home/hassan/FYP_data/test/'+file),(224,224)),cv2.COLOR_BGR2RGB)

cap = cv2.VideoCapture(1)
#total = 6
rows,cols = 224,224

#for i in range(total):
while True:
  # Read the frame
  _,img = cap.read()
  #img = X[i]
  rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  # Detect the faces
  faces = face_cascade.detectMultiScale(img, 1.1, 8)
  for (x,y,w,h) in faces:
      image = rgb[y:y+h,x:x+w]
      image = cv2.resize(image,(224,224),interpolation=cv2.INTER_AREA)
      new = img_to_array(image).flatten().astype(np.uint8)
      frame_normed = (new - new.min()) / (new.max() - new.min())
      frame_normed = np.array(frame_normed)
      test = np.reshape(frame_normed,(1,224,224,3))
      classes = model.predict(test)
      print(classes[0])
      if round(classes[0][0]) > classes[0][1]:
        item='hassan is here'
        cv2.putText(img, 'Hassan Ali', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        if speak==False:
          if item!=itemOld:
            speak=True
          if item==itemOld:
            speak=False 
        itemOld=item
      else:
        item='Mansoor is here'
        cv2.putText(img, 'Mansoor Zaman Khan', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        if speak==False:
          if item!=itemOld:
            speak=True
          if item==itemOld:
            speak=False 
          itemOld=item
      
      cv2.imshow('img', img)
      
      #cv2.imwrite('/home/hassan/FYP_data/res/'+str(int(classes[0][0]))+'.jpg',img)

    # Stop if 'd' key is pressed
  if cv2.waitKey(20) & 0xFF==ord('q'):
    break
  # Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
