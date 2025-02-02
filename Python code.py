import cv2
import numpy as np

def count_leds_bgr(image, b_min, g_min, r_min, b_max, g_max, r_max):

    lower_bgr = np.array([b_min, g_min, r_min])
    upper_bgr = np.array([b_max, g_max, r_max])

    mask = cv2.inRange(image, lower_bgr, upper_bgr)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    led_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 10: 
            led_count += 1
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return led_count, image

image = cv2.imread('C:/Users/ASUS/Pictures/Screenshots/testimng.png')
b_min, g_min, r_min = 0, 0, 200  
b_max, g_max, r_max = 255, 145, 255  

led_count, result_image = count_leds_bgr(image, b_min, g_min, r_min, b_max, g_max, r_max)
print(f"Detected LEDs: {led_count}")

cv2.imshow("Detected LEDs", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
