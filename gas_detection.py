#!/usr/bin/env python
import rospy
import sys
import tensorflow as tf
import numpy as np
import pandas as pd
import cv2 as cv
import seaborn as sb
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split as tst

from sensor_msgs.msg import Image
from sensor_msgs.msg import Imu
from std_msgs.msg import String
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
from time import time

rospy.init_node('human_detection', anonymous=False)
rospy.loginfo('Welcome Pilot')

webcam_pub = rospy.Publisher('WebCam_Publisher',Image, queue_size=10)
turtlebot_pub = rospy.Publisher('TurtleCam_Publisher', Image, queue_size=10)

bridge = CvBridge()

video = cv.VideoCapture(0)
rate = rospy.Rate(10)
body_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')
text= 'ROBOT CHARGE: '
text2 ='GAS LEVEL: '
def camera(image):

    raw_to_cv = bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")
    #bodies = body_cascade.detectMultiScale(raw_to_cv, 1.1, 1)
    #for (x, y, w, h) in bodies:
    cv.rectangle (raw_to_cv, (25, 30), (12, 45), (255, 0, 0), 2)
    offset = 35
    x,y = 0,0
   
    cv.putText(raw_to_cv, text, (0,15), cv.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0),2)
    cv.putText(raw_to_cv, text2,(200,15), cv.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0),2)
    cv.imshow('TurtleCam', raw_to_cv)

    wait = cv.waitKey(20)
#    cv.imshow ("Video", raw_to_cv)
    cv_to_raw = bridge.cv2_to_imgmsg(raw_to_cv, encoding="bgr8")
    turtlebot_pub.publish(cv_to_raw)

    wait = cv.waitKey(2)
    if wait == ord('x'):
        cv.destroyAllWindows()
def human_detection():

    while video.isOpened():
        ret, frame = video.read()
        frame = cv.flip(frame, 1)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        bodies = body_cascade.detectMultiScale(frame, 1.1, 1)

        for (x, y, w, h) in bodies:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.imshow('Video', frame)

        cv_to_raw = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        webcam_pub.publish(cv_to_raw)
        k = cv.waitKey(30) & 0xff
        if k == ord('x'):
            break



if __name__ == '__main__':
    try:
        rospy.Subscriber('/camera/image', Image, camera)
        #human_detection()
        rospy.spin()
        rate.sleep()
    except rospy.ROSInternalException:
        pass