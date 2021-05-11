#!/usr/bin/env python
import rospy
import cv2 as cv
import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
from random import random, seed
from random import random

from std_msgs.msg import String
import time

pub_gas = rospy.Publisher('/gas_data', String, queue_size=10)
rospy.init_node('gas_stuff_node', anonymous=False)
np.random.seed(23)
val = 1
rate = rospy.Rate(10)
gas_ppa =0
def gas_output():
    global val
    global gas_ppa
    while (val<10):
        
        gas_ppa = np.random.randint(0, 90)
        #rospy.loginfo(gas_ppa)
        pub_gas.publish (gas_ppa)
        time.sleep(1.0)


    rospy.spin()


try:
    gas_output()
except rospy.ROSInternalException():
    pass
    
