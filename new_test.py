import cv2
import numpy as np

img = cv2.imread(r'C:\Anhdep\butterfly.png')
pointA = (200, 100)
pointB = (450, 80)
cv2.line(img, (100,100),(300,200) , (0, 255, 255),3)
cv2.rectangle(img, (100,100), (300, 200), (0,0,255), 3)
cv2.circle(img, (100,100), 100, (0, 255, 255), 5)
cv2.imshow('NEW', img)
cv2.waitKey(0)
cv2.destroyAllWindows()