import cv2
import numpy as np

url = 'http://192.168.0.180:8080/video'  # Replace with your IP
cap = cv2.VideoCapture(url)

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    frame = cv2.resize(frame, (640, 480))

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color range for detection (example: RED)
    lower_red = np.array([160, 100, 100])
    upper_red = np.array([179, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise AND to isolate red parts
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Contour detection logic 
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(5,5),0)
    canny = cv2.Canny(blur,threshold1=100,threshold2=150)

    contour,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contour, -1, (0, 255, 0), 2)

    # Display
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Detected Red", result)
    cv2.imshow("Contour",canny)

    # Break on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
