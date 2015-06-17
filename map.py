#!/usr/bin/python

import pygame
import sys
from sys import exit
import os


running = True
xpos = 0
ypos = 0
####screen init

screen = pygame.display.set_mode((1366,700))
pygame.init()
bgcolor = (75,75,255)
circlecolour = (255,255,255)
#size = 2
count = 0
colcount = 0
newpos = 1200

for dirname, dirnames, filenames in os.walk('./southampton'):
	filenames.sort()
	filenames.reverse()
	for filename in filenames:
		
		pathtodata = (os.path.join(dirname, filename))
		print pathtodata
		datafile = open(pathtodata)
		
		if colcount >= 10:
			newpos=xpos-200
			ypos = 0
			colcount = 0
		colcount = colcount+1
		
		while datafile.readline():
			count = count + 1
			if count >= 6:
				temp=[]
				blarg = datafile.readline()
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
					#pygame.draw.rect(screen, circlecolour, (xpos,ypos,size,size), 0)
					screen.set_at((xpos, ypos), circlecolour)		
				ypos = ypos + 1
				xpos = newpos
		count = 0
		pygame.display.update()

	datafile.close()

while running:
#		screen.fill(bgcolor)
		
		for event in pygame.event.get():	
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
		
		
