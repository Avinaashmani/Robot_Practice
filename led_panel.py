#!/usr/bin/env python

import rospy

if __name__ == "__main__":
    rospy.init_node ('led_panel')

    rate = rospy.Rate(10)
    led_status = [0,0,0]

    while not rospy.is_shutdown():
        rospy.loginfo("This node has begun")
        rospy.loginfo(led_status)
        rospy.sleep(10)
    