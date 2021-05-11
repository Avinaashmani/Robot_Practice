#!/usr/bin/env python
import cv2 as cv
import rospy
import numpy as np
import sys
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

print(cv.__version__)

bridge = CvBridge()
error = CvBridgeError()

# video = cv.VideoCapture(0)
image = cv.imread('robot_car.jpg')

# cv.imshow('Image', image)

def image_callback(ros_frame):
    print ("Node is running")

    global bridge
    global error
    cv_image = bridge.imgmsg_to_cv2(ros_frame, "bgr8")
    try:
        cv_image
    except CvBridgeError as error:
        print(error)
    color = (142, 15, 196)
    cv_image = cv.flip(cv_image, 1)
    cv.putText(cv_image, "Hello Professors", (10, 200), cv.FONT_HERSHEY_COMPLEX, 2, color, 3)
    cv.imshow('Ros_View', cv_image)
    to_pub = bridge.cv2_to_imgmsg(cv_image,"bgr8")

    video_pub = rospy.Publisher("/car_video", Image, queue_size=10)
    video = Image()
    video.data = to_pub
    video_pub.publish(video)
    return to_pub
    cv.waitKey(2)
    

def main(args):
    global image

    rospy.init_node('image_covertor', anonymous=False)
    ros_sub = rospy.Subscriber('/usb_cam/image_raw',Image,image_callback)
    # video_pub = rospy.Publisher("/usb_cam/image_raw", Image, queue_size=10)
    
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down Node")
    cv.destroyAllWindows()
"""
while True:
    ret, frame = video.read()
    # cv.imshow('Video', frame)

    exc = cv.waitKey(1) & 0xFF
    if exc == ord('x'):
        break

cv.destroyAllWindows()
"""
if __name__ == "__main__":

    main(sys.argv)


def video_callback(ros_video):
    global bridge
    video_converted = bridge.imgmsg_to_cv2(ros_video, 'bgr8')
    video_converted = cv.flip(video_converted, 1)
    try:
        video_converted
    except CvBridgeError as error:
        print (error)
    cv.imshow('Ros_video', video_converted)
    pub_video = Image
    pub_video.data = bridge.cv2_to_imgmsg(video_converted, 'bgr8')
    
    cv.waitKey(2)
    return ros_video
    return video_converted

def video_process(args):

    rospy.init_node('video_publisher', anonymous=True)
    video_sub = rospy.Subscriber("/usb_cam/image_raw", Image, video_callback)
    video_pub = rospy.Publisher('/video_camera', Image, queue_size=10)
    
    try:
       rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo('Node is shutdown')
    cv.destroyAllWindows()