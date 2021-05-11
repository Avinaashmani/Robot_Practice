#!/usr/bin/env python

import rospy
import time
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

x = 0
y = 0
yaw = 0

def pose_callback(pose_msg):
    global x, y, yaw
    x = pose_msg.x
    y = pose_msg.y
    yaw=pose_msg.theta

def movement(speed, distance, direction):
    velocity_data = Twist()
    #get current location commands
    global x, y, yaw
    x_o = x
    y_o = y
    if (direction):
        velocity_data.linear.x = abs(speed)
    else:
        velocity_data.linear.x = -abs(speed)
    
    rate = rospy.Rate(10)
    speed_pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    while True:
        rospy.loginfo("The bot is moving in: ")
        speed_pub.publish(velocity_data)
        rate.sleep()
        distance_moved = distance_moved+abs(0.5*math.sqrt((x - x_o)**2 + ((y - y_o)**2)))
        rospy.loginfo (distance_moved)
        if not (distance_moved<distance):
            print("Reached {}".format(distance_moved))
            break
        
    velocity_data.linear.x = 0
    speed_pub.publish(velocity_data)

if __name__ == '__main__':
    
    try:
        
        rospy.init_node('sweaper_node',anonymous=False)
        sub = rospy.Subscriber('/turtle1/pose',Pose,pose_callback)
        time.sleep(2)
        
        movement (1.0, 4.0, True)
    except rospy.ROSInterruptException:
        rospy.loginfo("The node has been terminated: ")
    
