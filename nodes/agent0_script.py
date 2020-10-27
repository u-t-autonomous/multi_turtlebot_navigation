#!/usr/bin/env python

import sys
import agent
import rospy

if __name__ == "__main__":
	rospy.init_node("agent_test")
	a = agent.Agent("tb3_0", initial_x=0.0341992415488, initial_y=0.063386566937, initial_zO=-0.0257815181861, initial_wO=0.9996676)
	b = agent.Agent("tb3_1", initial_x=.013687, initial_y=2.176119, initial_zO=0.019995, initial_wO=.9998)
	c = agent.Agent("tb3_2", initial_x=3.46320486, initial_y=0.2825247, initial_zO=-0.999, initial_wO=.043139) 
	a.go_to_point( .6617646217,  0.7100666, 0.0)
	b.go_to_point(2.101717472, 2.35278, 0.0)
	c.go_to_point(2.605827,  0.7951288, 0.0)