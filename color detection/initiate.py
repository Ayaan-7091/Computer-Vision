import cv2
import numpy as np

image = cv2.imread("color detection\sample-2.jpg")
frame = cv2.resize(image,(640,480))

# Convert from BGR to HSV
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

# Defining HSV range for color to detect (here - red)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])

# Creating a mask
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create two masks and combine them
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

full_mask = cv2.bitwise_or(mask1, mask2)

# Apply combined mask
result = cv2.bitwise_and(frame, frame, mask=full_mask)

# Show
cv2.imshow("Original", image)
cv2.imshow("Mask", full_mask)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()