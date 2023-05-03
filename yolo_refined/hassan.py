import numpy as np
import cv2

net = cv2.dnn.readNet("/home/hassan/darknet/yolov3.weights","/home/hassan/darknet/cfg/yolov3.cfg")
classes = []

with open('/home/hassan/darknet/coco.names','r') as f:
    classes = f.read().splitlines()

cap = cv2.VideoCapture(2)
while(True):
    _,img = cap.read()
    height,width,_ = img.shape
    img = img.astype(np.uint8)
    blob = cv2.dnn.blobFromImage(img,1/255,(416,416),(0,0,0),swapRB=True,crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)





    boxes = []
    confidences = []
    class_ids = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence >= 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x,y,w,h])
                class_ids.append(class_id)
                confidences.append(float(confidence))
                
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    colours = np.random.uniform(0,255,size=(len(boxes),3))

    if(len(indexes)>0):
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            colour = colours[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),colour,2)
            cv2.putText(img, label + " " + confidence, (x,y+20), font, 2, (255,255,255), 2)

    cv2.imshow("Video",img)
    key = cv2.waitKey(1)
    if(key==27):
        break

cap.release()
cv2.destroyAllWindows()