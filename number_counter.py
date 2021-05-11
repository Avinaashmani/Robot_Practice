#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String
from std_srvs.srv import SetBool

counter = 0

def callback_reset_counter(req):
    if req.data:
       global counter
       counter = 0
       rospy.loginfo("The Counter Has been reset")
       
    rospy.loginfo("The counter has Not been Reset")

def callback_number(msg):
    global counter
    counter += msg.data
    new_msg = Int64()
    new_msg.data = counter
    pub.publish(new_msg)



if __name__ == "__main__":
    rospy.init_node('num_counter')
    sub = rospy.Subscriber("/number", Int64, callback_number)
    pub = rospy.Publisher('/number_count',Int64,queue_size=10)
    
    reset_sevices = rospy.Service("/reset_sevice",SetBool,callback_reset_counter)
    
    rospy.spin()
