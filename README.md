# multi_turtlebot_navigation

## Setup

Navigate into your workspace src directory and clone this repository:

  cd ~/catkin_ws/src
  
  git clone https://github.com/u-t-autonomous/multi_turtlebot_navigation.git
  
  cd ~/catkin_ws
  
  catkin_make
  
## 3 turtlebot navigation

In 3 separate terminals, ssh into each of the turtlebots and run the onboard bringup:

ssh pi@<ip of 1st turtlebot>

ROS_NAMESPACE=tb3_0 roslaunch turtlebot3_bringup turtlebot3_robot.launch multi_robot_name:="tb3_0" set_lidar_frame_id:="tb3_0/base_scan"

ssh pi@<ip of 2nd turtlebot>

ROS_NAMESPACE=tb3_1 roslaunch turtlebot3_bringup turtlebot3_robot.launch multi_robot_name:="tb3_1" set_lidar_frame_id:="tb3_1/base_scan"

ssh pi@<ip of 3rd turtlebot>

ROS_NAMESPACE=tb3_2 roslaunch turtlebot3_bringup turtlebot3_robot.launch multi_robot_name:="tb3_2" set_lidar_frame_id:="tb3_2/base_scan"

Launch the Navigation node:

roslaunch multi_turtlebot_navigation navigation_three.launch

By default, this will launch rviz. To move the bots through rviz, first give each an initial position with the "2D Pose Estimate" buttons. Then, the bots can be given waypoints with the "2D Nav Goal" buttons.

The bots can also be interacted with through code by publishing to the <turtlebot namespace>/initialpose and <turtlebot namespace>/move_base_simple/goal topics or by using the provided Rospy Agent module.
