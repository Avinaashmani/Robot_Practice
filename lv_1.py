#!/usr/bin/env python
import rospy
import sys
import cv2 as cv
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

class image_publisher:
    
    def __init__(self):
        self.video_sub = rospy.Subscriber('/usb_cam/image_raw', Image,self.video_callback)
        self.video_pub = rospy.Publisher('robot_video', Image, queue_size=10)

        self.bridge = CvBridge()


    def video_callback(self,ros_video):
        font = cv.FONT_HERSHEY_SIMPLEX
        color = (191, 69, 69)
        video_converted = self.bridge.imgmsg_to_cv2(ros_video,'bgr8')

        try:
            video_converted
        except CvBridgeError as error:
            print(error)

        cv.putText(video_converted, "Hello Seenu Ma'am", (10, 200), font, 3, color, 4)
        cv.imshow('ROBOT_VIDEO', video_converted)
        cv.waitKey(2)

        try:
            self.video_pub.publish(self.bridge.cv2_to_imgmsg(video_converted, 'bgr8'))
        except CvBridgeError as error:
            print (error)

def video_process(args):
    image_convertor = image_publisher()
    rospy.init_node('image_publisher', anonymous=True)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('ROBOT VIDEO SHUTDOWN')
    cv.destroyAllWindows()


if __name__ == '__main__':
    video_process(sys.argv)




    

    
    