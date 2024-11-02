import cv2
import numpy

photo = cv2.imread('images/7513062eb6bf0f06d20230aef126b5dc.jpg')

img = numpy.zeros(photo.shape[:2], dtype='uint8')

circle =  cv2.circle(img.copy(), (200 ,300), 150, 255, -1)
squre = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)
img = cv2.bitwise_not(photo, photo, mask=circle)
cv2.imshow('reee', img)


cv2.waitKey(0)