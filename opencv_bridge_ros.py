#!/usr/bin/env python 

from time import time

from numpy.lib.financial import rate
import rospy as rp
import numpy as np
import cv2 as cv
import sys 

from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

rp.init_node('robot_feed', anonymous=False)

rp.loginfo ('Welcome Pilot')

rasp_cam = rp.Publisher ('raspberry_pi_cam', Image, queue_size=10)
webcam = rp.Publisher ('webcam_video', Image, queue_size=10)

bridge = CvBridge()

#cam_1 = cv.VideoCapture(1)
cam_2 = cv.VideoCapture(0)
video = cv.VideoCapture(0)
rate = rp.Rate(10)
body_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')
def camera():
    while cam_2.isOpened():
#        ret, frame1 = cam_1.read()
        ret, frame2 = cam_2.read()

#        frame1 = cv.flip (frame1, 1)
        frame2 = cv.flip (frame2, 1)

#        cv.imshow('RaspbperryPi Camera', frame1)
        cv.imshow('Webcam', frame2)

        wait = cv.waitKey(3)

        #rpi_cam_converted = bridge.cv2_to_imgmsg(frame1, "passthrough")
        webcam_converted = bridge.cv2_to_imgmsg(frame2, encoding="passthrough")
        #rasp_cam.publish(rpi_cam_converted)
        webcam.publish(webcam_converted)


        if wait == ord('x'):
            break
def human_detection():
    
    while video.isOpened():
        ret, frame = video.read()
        frame = cv.flip(frame, 1)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        bodies = body_cascade.detectMultiScale(frame, 1.1, 1)

        for (x, y, w, h) in bodies:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.imshow('Video', frame)

        cv_to_raw = bridge.cv2_to_imgmsg(frame, encoding="passthrough")
        webcam.publish(cv_to_raw)
        k = cv.waitKey(30) & 0xff
        if k == ord('x'):
            break

#    cam_1.release()
    video.release()
    cv.destroyAllWindows()
    rp.spin()
   

if __name__ == '__main__':
    try:
        camera()
        #human_detection()
        rate.sleep()
    except rp.ROSInternalException:
        pass

    

    

