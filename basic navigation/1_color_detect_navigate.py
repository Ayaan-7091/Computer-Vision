import cv2
import numpy as np


url = 'http://192.168.0.180:8080/video'  # Replace with your IP
cap = cv2.VideoCapture(url)

last_direction = {
    "Red": None,
    "Green": None,
    "Blue": None
}
while (True):
    retr, frame = cap.read()

    if not retr:
        print('Unable to process frame !')
        break

    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Red (2 parts)
    lower_red1 = np.array([0, 100, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 70])
    upper_red2 = np.array([180, 255, 255])

    # Green
    lower_green = np.array([36, 100, 70])
    upper_green = np.array([86, 255, 255])

    # Blue
    lower_blue = np.array([94, 100, 70])
    upper_blue = np.array([126, 255, 255])

    red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #function to detect and process masks

    def detect_and_display(mask, color_name, color_bgr):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            contours = sorted(contours, key=cv2.contourArea,reverse=True)
            contour = contours[0] #selecting the largest contour
            area = cv2.contourArea(contour)
            if area > 500:
                x,y,w,h = cv2.boundingRect(contour)
                cx = x + w // 2
                cy = y + h // 2

                #draw a rectangle and a center point
                cv2.rectangle(frame, (x,y),(x+w,y+h),color_bgr,2)
                cv2.circle(frame,(cx,cy),5,(255,255,255),-1)
                cv2.putText(frame,f"{color_name} {(cx,cy)}",(cx+10,cy),cv2.FONT_HERSHEY_PLAIN,0.5,(255,255,255),1)

                
                #Navigation logic
                if cx <= 200:
                    direction = 'TURN LEFT'
                elif cx > 440:
                    direction = 'TURN RIGHT'
                else:
                    direction = 'MOVE FORWARD'
                
                if direction != last_direction[color_name]:
                    print(f"[{color_name}] : Direction - {direction}")
                    last_direction[color_name] = direction
                
                cv2.putText(frame, f"Direction: {direction}", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color_bgr, 2)
                
                #setting up directional arrows

            else:
                print(f"[{color_name}] : Direction - Stop")


        else:
                print(f"[{color_name}] : Direction - Stop")

   
    #apply to each color
    detect_and_display(red_mask, "Red", (0, 0, 255))
    detect_and_display(green_mask, "Green", (0, 255, 0))
    detect_and_display(blue_mask, "Blue", (255, 0, 0))

    cv2.imshow("Masked",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()