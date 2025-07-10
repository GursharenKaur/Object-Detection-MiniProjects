import cv2  #image
import time  #delay
import imutils  #resize

cam = cv2.VideoCapture(0)
time.sleep(1)

firstFrame = None
area = 500

while True:
  _,img = cam.read()
  text = "Normal"

  image = imutils.resize(img,width=500)  #resize
  grayImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  gaussianImg = cv2.GaussianBlur(grayImg,(21,21),0)  #smoothened

  if firstFrame is None:
    firstFrame = gaussianImg  #capturing first frame on 1st iteration
    continue

  imgDiff = cv2.absdiff(firstFrame,gaussianImg)   #absolute difference between is currentFrame-firstFrame

  threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]   #thresholding

  threshImg = cv2.dilate(threshImg, None, iterations=2)

  cnts = cv2.findContours(threshImg.copy(), 
                          cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
  cnts = imutils.grab_contours(cnts)

  for c in cnts:
    if cv2.contourArea(c) < area:
      continue
    (x,y,w,h) = cv2.boundingRect(c)
    cv2.rectangle(image, (x,y),(x+w, y+h), (0,255,0), 2)
    text = "Moving Object Detected"

  print(text)

  cv2.putText(image, text, (10,20),
              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
  cv2.imshow("cameraFeed", image)
  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break

cam.release()
cv2.destroyAllWIndows()
