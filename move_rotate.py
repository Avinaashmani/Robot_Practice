#!/usr/bin/env python
import rospy
import math
import time

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

x = 0
y = 0
z = 0
yaw = 0

def pose_callback(pose):
    global x, y, yaw
    x = pose.x
    y = pose.y
    yaw = pose.theta

def rotate(angular_speed,relative_angle, clockwise):

    global yaw
    velocity_messages = Twist()
    velocity_messages.linear.x = 0
    velocity_messages.linear.y = 0
    velocity_messages.linear.z = 0
    velocity_messages.angular.x = 0
    velocity_messages.angular.y = 0
    velocity_messages.angular.z = 0

    theta0 = yaw
    angular_speed = math.radians(abs(angular_speed))

    if (clockwise == True):
        velocity_messages.angular.z = -abs(angular_speed)
    else:
        velocity_messages.angular.z = abs (angular_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10)
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)

    t0 = rospy.Time.now().to_sec()
    while True:
        rospy.loginfo("The turtle is rotating")
        velocity_publisher.publish(velocity_messages)
        t1  = rospy.Time.now().to_sec()

        current_angle = (t1 - t0) * angular_speed
        loop_rate.sleep()

        if current_angle > relative_angle:
            rospy.loginfo("Reached")
            break
    velocity_messages.angular.z = 0
    velocity_publisher.publish(velocity_messages)


def move (speed, distance, is_forward):
    global x, y, yaw
    velocity_message = Twist()
    x0 = x
    y0 = y
    if (is_forward==True):
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)
    distance_moved = 0.0
    
    loop_rate = rospy.Rate(10)
    cmd_vel_topic = 'turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)
    
    while True:
        rospy.loginfo ("Turtle moves Forwards")
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        distance_moved = distance_moved+abs(0.5 * math.sqrt (((x-x0)**2)+((y-y0)**2))) 
        rospy.loginfo(distance_moved)
        if not distance_moved<distance:
            rospy.loginfo ("Reached")
            break

def go_to_goal (position_x, position_y):
    global x, y, yaw, z
    velocity_message = Twist()

    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)
    while True:
        constant = 0.5
        distance_moved = abs (math.sqrt(((position_x - x)**2)+((position_y-y)**2)))
        linear_speed = constant * distance_moved

        constant_angular = 4.0
        goal_angle = math.atan2 (position_y-y,position_x-x)
        angular_speed = constant_angular*(goal_angle - yaw)

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish (velocity_message)
        print ('x = {} ................ y = {}'.format(x, y))
          
        if (distance_moved<0.01):
            break 

if __name__ == '__main__':
    try:
        rospy.init_node('speed_node')
        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)
        speed_subscriber = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(speed_subscriber,Pose,pose_callback)
        time.sleep(2)
        go_to_goal(6,9)
        #move(5.0,3.0,True)
        #rotate(30,90,True)
    except rospy.ROSInterruptException:
        rospy.loginfo("Node terminated")


        