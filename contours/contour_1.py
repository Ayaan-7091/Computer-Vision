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

    # Canny edge detection
    edges = cv2.Canny(blur, threshold1=30, threshold2=90)  # You can tweak these for lighting

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Filter by area (avoid tiny/noisy contours)
        if area > 1000:  # Try changing this value and see
            # Draw the contour
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)

            # Draw bounding rectangle
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Show the area as text
            cv2.putText(frame, f"Area: {int(area)}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Original with Contours", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
