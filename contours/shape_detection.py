import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        print("Unable to capture frame!")
        break

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 150, 200)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:
            # Approximate the shape
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            # Bounding box
            x, y, w, h = cv2.boundingRect(approx)

            # Draw contours and box
            cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Determine shape based on vertices
            vertices = len(approx)
            shape = "Unidentified"

            if vertices == 3:
                shape = "Triangle"
            elif vertices == 4:
                aspectRatio = w / float(h)
                shape = "Square" if 0.95 <= aspectRatio <= 1.05 else "Rectangle"
            elif vertices > 4 and vertices < 10:
                shape = "Polygon"
            else:
                shape = "Circle"  # Approximation is very smooth

            # Label the shape
            cv2.putText(frame, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255, 255, 255), 2)

    cv2.imshow("Detected Shapes", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
