fondo= 'fondo.jpg'
personaje='Mario.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.int()

screen=pygame.display.set_model((640,480),0,32) 
pygame.display.set_caption("Bienvenido")
background= pygame.image.load(fondo).convert()
mouse_cursor= pygame.image.load(personaje).convert_alpha()

"""colores de fondo
color= [(0,0,0),(255,255,255)]"""


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		screen.blit(background,(0,0))
		x,y=pygame.mouse.get_post()
		x-=mouse_cursor.get_width()/2
		y-=mouse_cursor.get_height()/2
		screen.blit(mouse_cursor,(x,y))
		pygame.display.update()

