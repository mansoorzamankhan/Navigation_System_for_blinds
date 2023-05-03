import serial
import time
import pyttsx3
import threading
##text to speach 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
speak=True
item='welcome to sensor module  '
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


arduino=serial.Serial(
port= '/dev/ttyUSB0'  ,
baudrate= 115200,
bytesize=serial.EIGHTBITS,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
timeout=5,
xonxoff=False,
rtscts=False,
dsrdtr=False,
writeTimeout=2
)
while True:
    try:
        arduino.write("|".encode())
        data=arduino.readline()
        if data=='stares detected':
            if speak==False:
                if item!=itemOld:
                    speak=True
                if item==itemOld:
                    speak=False 
                itemOld=item
                print(data)
        time.sleep(1)
        if data=='small object  detected':
            if speak==False:
                if item!=itemOld:
                    speak=True
                if item==itemOld:
                    speak=False 
                itemOld=item
                print(data)
        time.sleep(1)
        if data=='small object  detected':
            if speak==False:
                if item!=itemOld:
                    speak=True
                if item==itemOld:
                    speak=False 
                itemOld=item
                print(data)
        time.sleep(1)
        if data=='wet surface detected':
            if speak==False:
                if item!=itemOld:
                    speak=True
                if item==itemOld:
                    speak=False 
                itemOld=item
                print(data)
        time.sleep(1)
        if data=='its very dark here':
            if speak==False:
                if item!=itemOld:
                    speak=True
                if item==itemOld:
                    speak=False 
                itemOld=item
                print(data)
        time.sleep(1)
      
        
    except Exception as e:
        print(e) 
        arduino.close()