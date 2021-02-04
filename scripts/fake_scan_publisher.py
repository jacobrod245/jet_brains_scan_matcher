#!/usr/bin/env python
#
# import rospy
# import math
# import numpy as np
# from sensor_msgs.msg import LaserScan
#
# rospy.init_node('fake_scan_publisher', anonymous=True)
#
# pub = rospy.Publisher('fake_scan', LaserScan, queue_size=10)
#
# rate = rospy.Rate(20)
#
#
# while not rospy.is_shutdown():
#     scan = LaserScan()
#
#     scan.header.frame_id = 'laser_frame'
#     scan.angle_min = (-2/3 * math.pi)
#     scan.angle_max = 2/3 * math.pi
#     scan.angle_increment = (1/300 * math.pi)
#     scan.range_min = 1
#     scan.range_max = 10
#
#     scan.ranges = []
#     scan.intensities = []
#
#     for x in range(400):
#         number = np.random.uniform((-2/3 * math.pi, 2/3 * math.pi))
#         scan.ranges.append(number)
#
#     pub.publish(scan)
#     rate.sleep()

import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node('fake_scan_publisher')

scan_pub = rospy.Publisher('fake_scan', LaserScan, queue_size=50)

num_readings = 100
laser_frequency = 40.0

count = 0
r = rospy.Rate(1.0)

while not rospy.is_shutdown():

    current_time = rospy.Time.now()

    scan = LaserScan()

    scan.header.stamp = current_time
    scan.header.frame_id = 'laser_frame'
    scan.angle_min = -1.57
    scan.angle_max = 1.57
    scan.angle_increment = 3.14 / num_readings
    scan.time_increment = (1.0 / laser_frequency) / (num_readings)
    scan.range_min = 0.0
    scan.range_max = 100.0

    scan.ranges = []
    scan.intensities = []
    for i in range(0, num_readings):
        scan.ranges.append(1.0 * count)  # fake data
        scan.intensities.append(300)  # fake data

    scan_pub.publish(scan)
    count += 1
    r.sleep()


