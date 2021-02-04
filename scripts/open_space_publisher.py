#!/usr/bin/env python

import rospy
import math
import numpy as np
import sensor_msgs.msg import LaserScan

def callback(data):

    rospy.loginfo("", data.something)

def listener():

    rospy.init_node("")