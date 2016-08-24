import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
vertices=(
	(1,-1,-1),
	(1,1,-1),
	(-1,1,-1),
	(-1,-1,-1),
	(1,-1,1),
	(1,1,1),
	(-1,-1,1),
	(-1,1,1),
	)
colors=(
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(1,1,0),
	(0,1,1),
	(1,1,1),
	)
edges=(
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7),
	)

surfaces =(
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6),
	)
def Cube():
	glBegin(GL_QUADS)
	x=0
	
	for surface in surfaces:
		
		for vertex in surface:
			x+=1
			if x>len(colors)-1:
				x=0
			
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
	glEnd()
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
			
			
	glEnd()
def main():
	pygame.init()
	display=(800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	
	gluPerspective(45, (display[0]/display[1]), 0.1,100.0)
	
	glTranslatef(0.0,0.0,-100)
	
	glRotatef(0,0,0,0)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-1,0,0)
				if event.key == pygame.K_RIGHT:
					glTranslatef(1,0,0)
				if event.key == pygame.K_UP:
					glTranslatef(0,1,0)
				if event.key == pygame.K_DOWN:
					glTranslatef(0,-1,0)
				
		glTranslate(0,0,0.4)
		x=glGetDouble(GL_MODELVIEW_MATRIX)
		array=[]
		for i in x:
			for g in i:
				array.append(g)
		
		print(array)
		camera_z =x[3][2]
		print(camera_z)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		pygame.display.flip()
		pygame.time.wait(10)
main()