#!/usr/bin/env python
import rospy
import sensor_msgs.msg._Imu
import gazebo_msgs.msg._LinkState
from std_msgs.msg import String

def call_back_feature(msg):
    rospy.loginfo("Hello, the node has begun: ")
    rospy.loginfo(msg)

if __name__ == "__main__":
    rospy.init_node('smart_node')
    sub = rospy.Subscriber("robot_news_topic",String,call_back_feature)
    rospy.loginfo("Hello: this node has begun")
    rospy.spin()