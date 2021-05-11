#!/usr/bin/env python

import rospy
import time
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String

x = 0
y = 0
z = 0
yaw = 0

def move (speed, distance, direction):
    global x,y
    velocity_messages = Twist()
    if speed > 0.4:
        print ("Speed must be lower than 0.4")
    if (direction == True):
        velocity_messages.linear.x = abs(speed)
    else:
        velocity_messages.linear.x = -abs(speed)
    distance_moved = 0.0

    loop_rate = rospy.Rate(10)
    cmd_vel_topic = '/cmd_vel_mux/input/teleop'
    velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True:
        rospy.loginfo ("Robot is moving forward ---------> ")
        velocity_publisher.publish(velocity_messages)

        loop_rate.sleep()

        t1 = rospy.Time.now().to_sec()
        distance_moved = (t1-t0)*speed
        if not (distance_moved<distance):
            rospy.loginfo("Reached  =) ")
            break    

    velocity_messages.linear.x = 0.0
    velocity_publisher.publish(velocity_messages)


def rotate (angle,relative_angle,direction):
    velocity_messages = Twist()
    global x,y,z,yaw
    velocity_messages.linear.x = 0
    velocity_messages.linear.y = 0
    velocity_messages.linear.z = 0
    velocity_messages.angular.x = 0
    velocity_messages.angular.y = 0
    velocity_messages.angular.z = 0

    theta0 = yaw
    angular_speed = math.radians(abs(angle))
    loop_rate = rospy.Rate(10)
    if (direction == True):
        velocity_messages.angular.z = abs(angle)
    else:
        velocity_messages.angular.z = -abs(angle)

    t0 = rospy.Time.now().to_sec()
    angle_moved = 0.0
    cmd_vel_topic = '/cmd_vel_mux/input/teleop'
    velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)
    
    while True:
        
        rospy.loginfo ('The Robot is Rotating =)) ')
        velocity_publisher.publish(velocity_messages)

        t1 =rospy.Time.now().to_sec()

        current_angle= (t1- t0)*angular_speed
        rospy.loginfo (relative_angle)
        rospy.loginfo (current_angle)
        loop_rate.sleep()
        if (current_angle > relative_angle):
            rospy.loginfo ("Reached =) ")
            break
    
    velocity_messages.angular.z = 0.0
    velocity_publisher.publish(velocity_messages)
        

   

if __name__ == '__main__':
    try:
        rospy.init_node('rviz_node',anonymous=False)
        
        time.sleep(2)
        move(0.3,0.5,False)
        time.sleep(2)
        rotate(90,90,True)
        
    except rospy.ROSInterruptException:
        rospy.loginfo ("Node has been terminated =(")

    
    
