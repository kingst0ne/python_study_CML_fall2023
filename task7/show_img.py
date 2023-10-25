import cv2 as cv

img = cv.imread('examples/img_1.jpg')

if img is None:
    raise Exception('No photo')

cv.imshow('show img', img)

cv.waitKey(0)