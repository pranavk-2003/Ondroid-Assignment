import cv2
import numpy as np
image = cv2.imread('C:/Users/ASUS/Pictures/Screenshots/testimng.png')

def nothing(x):
    pass

cv2.namedWindow('Adjust Mask')
cv2.createTrackbar('B_min', 'Adjust Mask', 0, 255, nothing)
cv2.createTrackbar('G_min', 'Adjust Mask', 0, 255, nothing)
cv2.createTrackbar('R_min', 'Adjust Mask', 180, 255, nothing)
cv2.createTrackbar('B_max', 'Adjust Mask', 100, 255, nothing)
cv2.createTrackbar('G_max', 'Adjust Mask', 100, 255, nothing)
cv2.createTrackbar('R_max', 'Adjust Mask', 255, 255, nothing)

while True:
    B_min = cv2.getTrackbarPos('B_min', 'Adjust Mask')
    G_min = cv2.getTrackbarPos('G_min', 'Adjust Mask')
    R_min = cv2.getTrackbarPos('R_min', 'Adjust Mask')
    B_max = cv2.getTrackbarPos('B_max', 'Adjust Mask')
    G_max = cv2.getTrackbarPos('G_max', 'Adjust Mask')
    R_max = cv2.getTrackbarPos('R_max', 'Adjust Mask')

    lower_red = np.array([B_min, G_min, R_min])
    upper_red = np.array([B_max, G_max, R_max])

    mask = cv2.inRange(image, lower_red, upper_red)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('Adjust Mask', result)

    if cv2.waitKey(1) & 0xFF == 27: 
        break

cv2.destroyAllWindows()
