#!/usr/bin/python

import time
import threading
import pygame
import sys
from sys import exit
import os

####vars
running = True
yposition = 0
oldxpos = 1200
oldypos = 0
#newxpos = 1200
bgcolor = (75,75,255)
circlecolour = (255,255,255)
size = 2
#count = 0
colcount = 0
#newpos = 1200
threadcount = 0
i =0
fname =""
startpos = 0
####screen init

screen = pygame.display.set_mode((1366,700))
pygame.init()

###classes

class myThread (threading.Thread):
	def __init__(self, filename, startpos, rowcount):
		threading.Thread.__init__(self)
		self.fname = filename
		self.startpos = startpos
		self.rowcount = rowcount
	def run(self):
		processfile(self.fname, self.startpos, self.rowcount)

class drawthread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		pygame.display.update()
###functions

def processfile(filename, startpos, rowcount):
		
	count = 0
	ypos = rowcount * 100
	#print ypos
	xpos = startpos
	
	datafile = open(filename)
	while datafile.readline():
		temp=[]
		blarg = datafile.readline()
		count = count + 1
		if count >= 3:
			temp = blarg.split()
			for num in range (0, len(temp)):
				xpos = xpos + 1
				col = abs((float(temp[num])*100)/255)
				if col >= 256:
					circlecolour = (120,255,50)
				if col >= 30 and col <= 255:
					circlecolour = (0,col,0)
				if col <= 30:
					circlecolour = (0,0,col * 2)
				#pygame.draw.rect(screen, circlecolour, (200,200,size,size), 0)
				screen.set_at((xpos, ypos), circlecolour)		
			ypos = ypos + 1
			xpos = startpos
	#count = 0	

	datafile.close()
###main

for dirname, dirnames, filenames in os.walk('./southampton'):
	filenames.sort()
	filenames.reverse()
	threadarray = []
	
	for filename in filenames:
		threadarray.append("")
		pathtodata = (os.path.join(dirname, filename))
		
		if colcount >= 10:
			oldxpos=oldxpos-200
			#yposition = 0
			colcount = 0
		
		#print pathtodata
	#	print pathtodata,oldxpos
		threadarray[threadcount] = myThread(pathtodata,oldxpos,colcount)
		threadarray[threadcount].start()
		threadcount += 1
		colcount = colcount+1
	
while running:
#		screen.fill(bgcolor)
	
	
	updatescreen = drawthread()
	updatescreen.start()
	
	for event in pygame.event.get():	
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		
		
