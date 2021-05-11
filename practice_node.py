#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node ("Lv_one_node")
    pub = rospy.Publisher("/Lv_One_Robot", String, queue_size=10)
    
    rate = rospy.Rate(3)

    
    while not rospy.is_shutdown():
        message = String
        message.data = "Hello Friend"
        pub.publish(message)

        rate.sleep()
    rospy.loginfo("The the Node has been ShutDown")
