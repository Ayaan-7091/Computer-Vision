import cv2
print(cv2.__version__)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #ret = status, frame = image

    if not ret:
        print("unable to capture frame")
        break

    cv2.imshow("Webcam View", frame)

     # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()