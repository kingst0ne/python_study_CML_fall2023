import cv2 as cv
from detect import detect_and_display



img = cv.imread('examples/img_2.jpg')

detect_and_display(img)

cv.waitKey(0)