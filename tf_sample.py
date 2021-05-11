#!/usr/bin/env python

import rospy
import cv2 as cv
import numpy as np
import geometry_msgs.msg
import tf_conversions
import tf2_ros



def sample_broadcaster(msg):
    broadcaster = tf2_ros.TransformBroadcaster()

    linear_x = msg


    transform = geometry_msgs.msg.TransformStamped()

    transform.header.frame_id = "/word"
    transform.header.stamp = rospy.Time.now()
    transform.child_frame_id = '/odom'
    transform.transform.translation.x = 1
    transform.transform.translation.y = 0
    transform.transform.translation.z = 0

    transform.transform.rotation.x = 1
    transform.transform.rotation.y = 1
    transform.transform.rotation.z = 1
    transform.transform.rotation.w = 1

if __name__ == '__main__':
    rospy.init_node("tf2_broadcaster")
   
    rospy.spin()
    



