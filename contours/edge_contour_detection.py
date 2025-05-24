import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Unable to capture frame !")
        break

    frame = cv2.resize(frame,(640,480))

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5),0)

    #canny edge detection
    edges = cv2.Canny(blur, threshold1=150, threshold2=200)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Show all stages
    cv2.imshow("Original", frame)
    cv2.imshow("Edges", edges)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()