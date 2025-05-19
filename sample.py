import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Unable to capture frame !")
        break

    frame = cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    edges = cv2.Canny(frame,threshold1=30,threshold2=90)

    cv2.imshow("Base Frame", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Edges", edges)


    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()