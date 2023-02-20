import cv2
import numpy as np

img = cv2.imread('pic1.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([140, 60, 0])
upper_red = np.array([255, 255, 255])

mask_red = cv2.inRange(hsv, lower_red, upper_red)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask_red = cv2.dilate(mask_red, element)

contours, _ = cv2.findContours(
    mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hull_list = [cv2.convexHull(contour) for contour in contours]
drawing = np.zeros_like(img)
for hull in hull_list:
    cv2.fillConvexPoly(img, hull, (255, 0, 0))

cv2.imshow('Image', img)
cv2.imwrite('out.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
