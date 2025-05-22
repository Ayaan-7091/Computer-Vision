import cv2
import numpy as np

image = cv2.imread("color detection\sample-leaf.jpg")

frame = cv2.resize(image,(640,480))
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])


mask = cv2.inRange(hsv,lower_green,upper_green)

result = cv2.bitwise_and(frame,frame,mask=mask)

cv2.imshow('Original',image)
cv2.imshow('Mask',mask)
cv2.imshow('Result',result)

cv2.waitKey(0)
cv2.destroyAllWindows()
