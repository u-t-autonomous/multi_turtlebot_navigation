#!/usr/bin/env python

import sys
import agent
import rospy

if __name__ == "__main__":
	rospy.init_node("agent_test")
	a = agent.Agent("tb3_0", initial_x=-0.0563954, initial_y=0.1402886, initial_zO=0.00749953884123, initial_wO=0.999971878)
	b = agent.Agent("tb3_1", initial_x=3.43185210228, initial_y=0.136713042855, initial_zO= -0.99997, initial_wO=0.00749958)
	c = agent.Agent("tb3_2", initial_x=0.160504952073, initial_y=2.07770085335, initial_zO=0.020482106140, initial_wO=.9998) 
	a.go_to_point(1.56703829765, -0.0142412204295, 0.0)
	b.go_to_point(3.40452218056, 1.9586602449, 0.0)
	c.go_to_point(1.92002558708,  2.54011845589, 0.0)
