#!/usr/bin/env python

import sys
import rospy
import random
import numpy as np
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from actionlib_msgs.msg import GoalStatusArray
import math
import numpy as np
import sys
import types
import tf

class Agent:

	goal_reached = False

	def __init__(self, namespace, initial_x=0.0, initial_y=0.0, initial_z=0.0, initial_xO=0.0, initial_yO=0.0, initial_zO=.997, initial_wO=.026):
		self.namespace = namespace
		self.initial_pose_pub = rospy.Publisher("/" + namespace + "/initialpose", PoseWithCovarianceStamped, queue_size=5)
		self.goal_topic = "/" + namespace + "/move_base_simple/goal"
		self.goal_pub = rospy.Publisher(self.goal_topic, PoseStamped, queue_size=5)
		self.goal_status_sub = rospy.Subscriber("/" + namespace + "/move_base/status", GoalStatusArray, self.feedbackCB)
		self.curr_pose_sub = rospy.Subscriber("/" + namespace + "/amcl_pose", PoseWithCovarianceStamped, self.curr_poseCB)
		initialpose = PoseWithCovarianceStamped()
		initialpose.pose.pose.position.x = initial_x
		initialpose.pose.pose.position.y = initial_y
		initialpose.pose.pose.position.z = initial_z
		initialpose.pose.pose.orientation.x = initial_xO
		initialpose.pose.pose.orientation.y = initial_yO
		initialpose.pose.pose.orientation.z = initial_zO
		initialpose.pose.pose.orientation.w = initial_wO
		
		rospy.sleep(7)
		self.initial_pose_pub.publish(initialpose)
		

	def feedbackCB(self, data):
		if len(data.status_list) > 0 and data.status_list[-1].status == 3:
			self.goal_reached = True

	def go_to_point(self, x, y, z):
		rel_x = x - self.curr_pose.pose.pose.position.x
		rel_y = y - self.curr_pose.pose.pose.position.y
		heading = np.arctan2(rel_y, rel_x)
		quat = self.__euler_to_quaternion(heading, 0, 0)
		self.go_to_point_and_orientation(x, y, 0, quat[0], quat[1], quat[2],  quat[3], 2)

	def go_to_point_and_orientation(self, x, y, z, xO, yO, zO, wO, seq):
		goal = PoseStamped()

		goal.header.seq = seq
		goal.header.stamp = rospy.Time.now()
		goal.header.frame_id = "map"

		goal.pose.position.x = x
		goal.pose.position.y = y
		goal.pose.position.z = z
		goal.pose.orientation.x = xO
		goal.pose.orientation.y = yO
		goal.pose.orientation.z = zO
		goal.pose.orientation.w = wO
		self.goal_pub.publish(goal)
		while not self.goal_reached:
			pass
		self.goal_reached = False

	def curr_poseCB(self, data):
		self.curr_pose = data

	def __euler_to_quaternion(self, yaw, pitch, roll):

		qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
		qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
		qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
		qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
		return [qx, qy, qz, qw]