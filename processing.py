import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    #resize for better performance 
    frame = cv2.resize(frame,(640,480))

    #1. Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Blur (removes noise)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3. Canny Edge Detection
    edges = cv2.Canny(blur, 50, 150)

    cv2.imshow("Original Frame",frame)
    cv2.imshow("Grayscale Frame",gray)
    cv2.imshow("Gaussian Blur",blur)
    cv2.imshow("Canny Edge Detection",edges)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
