#!/usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan

def callback(data):

    scan_data = [data.ranges, data.intensities]

    rospy.loginfo(scan_data)



def listener():

    rospy.init_node("open_space_publisher")

    rospy.Subscriber("master_scan", LaserScan, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()




