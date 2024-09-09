#! /usr/bin/env python

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Point
from tf.transformations import euler_from_quaternion
import rospy
import rosunit
import unittest
import rostest
import time
import math

PKG = 'tortoisebot_waypoints'
NAME = 'target_g1_xy_move_integration_test'

class TargetXYMoveTest(unittest.TestCase):

    def setUp(self):

        rospy.init_node('test_coordinate_move_node')
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.current_orientation = Quaternion()
        self.init_yaw = 0
        self.final_yaw = 0
        self._target_pos = Point()
        self._target_pos.x = -0.5
        self._target_pos.y = 0.0
        self._target_yaw = math.atan2(self._target_pos.y - 0.0, self._target_pos.x - 0.0)
        self._dist_precision = 0.05
        self._yaw_precision = 0.1
        self.current_position = Point()       

    def odom_callback(self, msg):
        self.current_position    = msg.pose.pose.position 
        self.current_orientation = msg.pose.pose.orientation

    def euler_to_quaternion(self, msg):
        orientation_list = [msg.x, msg.y, msg.z, msg.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
        return yaw

    def test_correct_position(self):
        rospy.wait_for_message("/odom", Odometry, timeout=10)
        print("1T01", '-' * 20)
        print ("Current Position:")
        print (self.current_position)
        # time.sleep(2)

        err_pos = math.sqrt(pow(self._target_pos.y - self.current_position.y, 2) + 
                            pow(self._target_pos.x - self.current_position.x, 2))

        print("Error position:", err_pos)
        print("Distance Precision:", self._dist_precision)
        self.assertTrue((err_pos < self._dist_precision), "IT01-Integration error. Position was not between the expected values.")

    def test_correct_rotation(self):
        rospy.wait_for_message("/odom", Odometry, timeout=10)
        print("1T02", '-' * 20)
        print("Current Orientation:")
        print(self.current_orientation)
        # time.sleep(2)

        self.final_yaw = self.euler_to_quaternion(self.current_orientation)
        print ("Target Yaw:", self._target_yaw)
        print ("Final Yaw:", self.final_yaw)

        err_yaw = abs(self._target_yaw - self.final_yaw)
        while err_yaw > math.pi:
            err_yaw -= math.pi
        if self.final_yaw < 0:
            err_yaw = math.pi - err_yaw

        print ("Error Yaw:", err_yaw)
        print("Yaw Precision:", self._yaw_precision)
        self.assertTrue((err_yaw < self._yaw_precision), "IT02-Integration error. Rotation was not between the expected values.")


if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TargetXYMoveTest)