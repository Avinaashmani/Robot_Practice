#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import String
from iot_messages.msg import IoTsensors


counter = 0
def temrature_humidity():
    pub = rospy.Publisher('iot_sensors',IoTsensors,queue_size=10)
    rospy.init_node('iot_sensor_node',anonymous=False)
    rate =  rospy.Rate(1)
    global counter
    while not rospy.is_shutdown():
        sensor = IoTsensors()
        sensor.id = 6050
        sensor.temprature = 34 + (random.random()*2)
        sensor.humidity   = 25 + (random.random()*5)
        sensor.name = "MPU 6050"
        pub.publish(sensor)
        rospy.loginfo (sensor)
        counter =  counter +1 
        rospy.loginfo ("No.of messages {}".format(counter))
        rate.sleep()

if __name__ == '__main__':
    temrature_humidity()
    
    