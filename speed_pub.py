#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
def twist_position_show():
    twist = Twist()
    rospy.loginfo (twist.linear.x)
    rospy.loginfo (twist.linear.y)
    rospy.loginfo (twist.angular.x)
    rospy.loginfo (twist.angular.y)
def speed_show():
    rospy.init_node('speed_pub',anonymous=False)
    speed_publisher = rospy.Publisher('speed_show',Twist,queue_size=1)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        twist =Twist()
        twist.linear.x = 1.0
        twist.angular.y = 3.0
        twist.linear.x = 4.0
        #twist_position_show()
        rospy.spin()

if __name__ == '__main__':

   # twist_position_show()
    speed_show()
    

         