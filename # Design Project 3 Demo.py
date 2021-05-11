# Design Project 3 Demo

import cv2 as cv

import numpy as np

# from matplotlib import pyplot as plt
video = cv.VideoCapture(0)

ret_A, frame_A = video.read()
ret_B, frame_B = video.read()

frame_A = cv.flip(frame_A, 1)
frame_B = cv.flip(frame_B, 1)

kernel = np.ones((5, 5), np.uint8)

color = (181, 181, 33)
font = cv.FONT_HERSHEY_SIMPLEX
thickness = 5


def trackbar(x):
    print (x)


cv.namedWindow('Adjust')
cv.createTrackbar('Thresh Adjust', 'Adjust', 0, 255, trackbar)

while True:
    abs_diff = cv.absdiff(frame_A, frame_B)
    gray_frame_diff = cv.cvtColor(abs_diff, cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(gray_frame_diff, (7, 7), 0)
    ret_th, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)

    dilate = cv.dilate(thresh, kernel=None, iterations=2)

    contour, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # drawn_contour = cv.drawContours(frame_A, contour, -1, color, thickness=thickness)

    for i in contour:
        (x_point, y_point, width, height) = cv.boundingRect(i)
        if cv.contourArea(i) < 200:
            continue
        cv.rectangle(frame_A, (x_point, y_point), (x_point + width, y_point +height), color, thickness)
        cv.putText(frame_A, ' :-Movement-:', (x_point, y_point), font, 1.5, color, 2)

    cv.imshow('Video Feed', frame_A)
    frame_A = frame_B
    ret_B, frame_B = video.read()

    exc = cv.waitKey(1) & 0xFF

    if exc == ord('x'):
        break
video.release()
cv.destroyAllWindows()