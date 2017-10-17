# DemoGraphics.py
# CS 1110 (cs-1110profs-L@cornell.edu)
# February, 2016
""" Draws a design with squares and a design
with rings."""

from SimpleGraphics import *

# First Figure
MakeWindow(10,bgcolor=WHITE,labels=False)
for i in range(0, 6):
	DrawRect(0,0,10-i,10-i,FillColor=CYAN,EdgeWidth=5,theta= -(i*5))
# # Add more squares...




# Second Figure
MakeWindow(10,bgcolor=RED,labels=False)
# # Rings
DrawDisk(0,0,2,FillColor=CYAN,EdgeWidth=5)
DrawDisk(-4,0,2,EdgeWidth=5)
DrawDisk(4,0,2,EdgeWidth=5)
DrawDisk(-2,3.5,2,EdgeWidth=5)
DrawDisk(2,3.5,2,EdgeWidth=5)
DrawDisk(0,7,2,EdgeWidth=5)

# # Add more rings...

ShowWindow()
