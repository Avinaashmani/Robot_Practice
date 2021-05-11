#!/usr/bin/env python 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def callback_cmd(msg):
    cmd = Twist()
    rospy.loginfo(cmd)
def callback_pose(msg):
    pose = Pose()
    rospy.loginfo (pose)
def pose_show():
    rospy.init_node('pose_show',anonymous=False)
    sub = rospy.Subscriber ('/turtle1/pose',Pose,callback_pose)
    rate = rospy.Rate(1)
    rate.sleep()
def cmd_show():
    rospy.init_node('cmd_vals',anonymous=False)
    sub = rospy.Subscriber ('/turtle1/cmd_vel',Twist,callback_cmd)
    rospy.spin()
if __name__ == "__main__":
    pose_show()
    #cmd_show()
