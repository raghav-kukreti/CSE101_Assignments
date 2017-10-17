# IndianFlag.py
# CSE 101 (vikram@iiitd.ac.in)
# August, 2016
""" Contains a function for drawing the Indian
flag and an Application Script  that can be used to check it out
"""

from SimpleGraphics import *
import math


def DrawIndianFlag(x,y,W):
	""" Draws the Indian Flag.  W is the vertical dimension
	The center of the large flag is at (x,y).

	Precondition: x,y, and W are numbers and W>0.
	"""
	DrawRect(0,3,10,3,FillColor=[0.738, 0.0860, 0.102],EdgeWidth=0,theta= 0)
	DrawChakra(0,0,15,1.4)
	DrawRect(0,-3,10,3,FillColor=[0.288, 0.395, 0.317],EdgeWidth=0,theta= 0)
	DrawRect(0,0,10,3,FillColor=[0.9, 0.9, 0.9],EdgeWidth=0,theta= 0)
	# DrawDisk(0,-3,1.4,EdgeWidth=5, EdgeColor=BLUE)
	#Complete this

def DrawChakra(x,y,theta,r):

	"""Draws the Ashok Chakra.  r is the radius of the Chakra
	The center of the Chakra is at (x,y).

	Precondition: x,y, and r are numbers and r>0.
	"""
	DrawDisk(x,y,r, EdgeColor=BLUE, EdgeWidth=5)
	DrawLineSeg(x,y,r*math.cos(0),r*math.sin(0))
	DrawLineSeg(x,y,r*math.cos(theta),r*math.sin(theta))
	DrawLineSeg(x,y,r*math.cos(2*theta),r*math.sin(2*theta))
	DrawLineSeg(x,y,r*math.cos(3*theta),r*math.sin(3*theta))
	DrawLineSeg(x,y,r*math.cos(4*theta),r*math.sin(4*theta))
	DrawLineSeg(x,y,r*math.cos(5*theta),r*math.sin(5*theta))

	DrawLineSeg(x,y,r*math.cos(6*theta),r*math.sin(6*theta))
	DrawLineSeg(x,y,r*math.cos(7*theta),r*math.sin(7*theta))
	DrawLineSeg(x,y,r*math.cos(8*theta),r*math.sin(8*theta))
	DrawLineSeg(x,y,r*math.cos(9*theta),r*math.sin(9*theta))
	DrawLineSeg(x,y,r*math.cos(10*theta),r*math.sin(10*theta))
	DrawLineSeg(x,y,r*math.cos(11*theta),r*math.sin(11*theta))
	
	DrawLineSeg(x,y,r*math.cos(12*theta),r*math.sin(12*theta))
	DrawLineSeg(x,y,r*math.cos(13*theta),r*math.sin(13*theta))
	DrawLineSeg(x,y,r*math.cos(14*theta),r*math.sin(14*theta))
	DrawLineSeg(x,y,r*math.cos(15*theta),r*math.sin(15*theta))
	DrawLineSeg(x,y,r*math.cos(16*theta),r*math.sin(16*theta))
	DrawLineSeg(x,y,r*math.cos(17*theta),r*math.sin(17*theta))
	
	DrawLineSeg(x,y,r*math.cos(18*theta),r*math.sin(18*theta))
	DrawLineSeg(x,y,r*math.cos(19*theta),r*math.sin(19*theta))
	DrawLineSeg(x,y,r*math.cos(20*theta),r*math.sin(20*theta))
	DrawLineSeg(x,y,r*math.cos(21*theta),r*math.sin(21*theta))
	DrawLineSeg(x,y,r*math.cos(22*theta),r*math.sin(22*theta))
	DrawLineSeg(x,y,r*math.cos(23*theta),r*math.sin(23*theta))
	


# Application Script
if __name__ == '__main__':
     # Display the Indian flag on a black background.
    MakeWindow(10,bgcolor=BLACK,labels=False)
    DrawIndianFlag(0,0,8)
    ShowWindow()

