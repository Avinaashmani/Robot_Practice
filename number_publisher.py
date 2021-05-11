#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String

if __name__ == "__main__":

    rospy.init_node ("number_publisher")
    rospy.set_param('/welcome_message',"Hello Hi")
    pub = rospy.Publisher("/number",Int64,queue_size=6000)
    freq = rospy.get_param('/number_pub_frequency')
    rate = rospy.Rate(freq)
    number = rospy.get_param("/number_to_publish")
    wc_msg = rospy.get_param('/welcome_message')
    rospy.loginfo(wc_msg)
# def num_counter (num):
#     while not rospy.is_shutdown():
#         num = num +1
#         rospy.loginfo(num)

    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = number
        pub.publish (msg)
        rate.sleep()
    rospy.loginfo("The node has been shut Down")
    