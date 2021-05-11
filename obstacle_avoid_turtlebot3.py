#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry


def callback_position(msg):
     x = msg.pose.pose.position.x
     y = msg.pose.pose.position.y

     x_l = msg.twist.twist.linear.x
     y_l = msg.twist.twist.linear.y
     rospy.loginfo ("Position X {}, Position Y {}, Twist Linear X {},Twist Linear Y {} ".format(x, y, x_l, y_l))
    
def current_self_position():
    rospy.init_node('location_monitor')
    sub_position = rospy.Subscriber('/odom',Odometry,callback_position)
    rate = rospy.Rate(10)
    rospy.spin()
    

if __name__ == '__main__':
    current_self_position()
 