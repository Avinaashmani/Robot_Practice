#!/usr/bin/env python
from logging import error
import ros
import rospy
import cv2 as cv
import sys
from matplotlib import pyplot as plt

from sensor_msgs.msg import Image
from cv_bridge import CvBridge 
from cv_bridge import CvBridgeError
from std_msgs.msg import String

rospy.init_node('Video_Trial', anonymous=False)
rospy.loginfo("Hello Camera Node, Started !")

bridge = CvBridge()

def display_image(img):
    cv.imshow("Live Feed", img)
    cv.waitKey(3)

def subs_callbak(img_message):
    rospy.loginfo(img_message.header)

    try:
        converted_image = bridge.imgmsg_to_cv2(img_message, "bgr8")
    except CvBridgeError as error:
        print (error)
    
    display_image(converted_image)

subs_image = rospy.Subscriber('/usb_cam/image_raw', Image, subs_callbak)
pubs_image = rospy.Publisher('/robot_video', Image, queue_size=10)


while not rospy.is_shutdown():
    rospy.spin()

