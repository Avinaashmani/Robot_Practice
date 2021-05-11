#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse


def addition_callback(data):
    sum  = data.a +data.b
    rospy.loginfo ("the sum of the two numbers are: {}".format(sum))
    return AddTwoIntsResponse(data.a + data.b)
def adding_two_numbers():
    rospy.init_node('Adding_two_Numbers_node',anonymous=False)
    s= rospy.Service ('add_two_int',AddTwoInts,addition_callback)
    rospy.loginfo("Adding Two Numbers")
    rospy.spin()
if __name__ == "__main__":
    adding_two_numbers()
    



    