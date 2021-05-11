#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback_odom(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    
    rospy.loginfo('X = {}, Y ={}, Z = {}'.format(x, y, z))

if __name__ == "__main__":
    rospy.init_node('location_monitor_node')
    sub = rospy.Subscriber("/odom",Odometry,callback_odom)
    pub = rospy.Publisher("/topic_location_of_the_robot",Odometry,queue_size=10)

    rospy.spin()
while not rospy.is_shutdown:
    pass