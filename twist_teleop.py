#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

linear_x = 0.0
linear_y = 0.0
linear_z = 0.0

angular_x = 0.0
angular_y = 0.0
angular_z = 0.0

def motor_move(data):
    global linear_x
    global linear_y
    global linear_z

    global angular_x
    global angular_y
    global angular_z

    linear_x = data.linear.x
    rospy.loginfo(linear_x)

if __name__ == '__main__':

    rospy.init_node ('motor_driver', anonymous=True)
    sub = rospy.Subscriber('/turtle1/cmd_vel',Twist, motor_move)

    rospy.spin()

    