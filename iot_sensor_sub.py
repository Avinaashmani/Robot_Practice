#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from iot_messages.msg import IoTsensors

def iot_callback(sensor):
    
    rospy.loginfo (sensor.id)
    rospy.loginfo (sensor.temprature)
    rospy.loginfo (sensor.name)
    rospy.loginfo (sensor.humidity)
if __name__ == '__main__':
    rospy.init_node('iot_subs_node',anonymous=False)
    rospy.Subscriber('iot_sensors', IoTsensors, iot_callback)
    counter = 0
    counter = counter +1
    rospy.loginfo(counter)
    rate  =rospy.Rate(1)
    rospy.spin()



    