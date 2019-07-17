

import pygame
from pygame.locals import*
from sys import exit
#randmicos
from random import randint

pygame.init()

negro = (0, 0, 0)
blanco = (255, 255, 255)
screen = pygame.display.set_mode((890, 550), 0, 32)

# titulo a la ventana
pygame.display.set_caption("Duck Hunt")

#Variables para la posicion del mouse.
x_pos = 0
y_pos = 0

# variables para la posicion cuando hagamos clic con el mouse
x_clic = 0
y_clic = 0

# variable para la posicion del pato (randomico)
x_duck = 0
y_duck = randint(0, 450)

# inicializamos contadores para puntos y la velocidad
puntos = 0
velocidad = 2

# booleano para cuando no mate el pato
pierde = False

# init (frecuencia = 22050, tamaño = -16, canales = 2, búfer = 1024)
#https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.init
pygame.mixer.init(44100, -16, 2, 1024)

# configuracion del volume de la musica entre 0.0/1.0
#https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.set_volume
pygame.mixer.music.set_volume(0.5)

while True:
    for event in pygame.event.get():
        # 
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONDOWN:
            x_clic, y_clic = pygame.mouse.get_pos()

    posicion = (x_pos - 50, y_pos - 50)

    x_duck += 1

    if x_duck * velocidad > 890 and not pierde:
        x_duck = 0
        y_duck = randint(0, 450)

        # errou, toca a musica do game over
        pygame.mixer.music.load("duckHurtGameOver.ogg")
        pygame.mixer.music.play()

        pierde = True

    # no se vera la flecha del cursor
    pygame.mouse.set_visible(False)

    
    screen.blit(pygame.image.load("fondo.png"), (0, 0))
    #muestra en  screen el puntaje de patos muertos 
    # .from.... muestra al frente del fondo principal
    screen.blit(pygame.font.SysFont("comicsansms", 60).render("Score: " + str(puntos), True, blanco), (500, 450))

    
    # COLISION PATO-MIRA

    if x_clic in range(x_duck * velocidad - 30, x_duck * velocidad + 30) and y_clic in range(y_duck - 30, y_duck + 30):
        # agregsmos musica cuando mata al pato
        pygame.mixer.music.load("punto.ogg")
        pygame.mixer.music.play()

        #va sumando los puntos
        puntos += 1
        #y aumenta la velocidad 
        velocidad += 1
        x_duck = 0
        y_duck = randint(50, 500)

    screen.blit(pygame.image.load("pato.gif"), (x_duck * velocidad, y_duck))

    if pierde:
        x_duck = -50
        y_duck = -50
        #imagen en la mitad del fondo
        screen.blit(pygame.image.load("perro.gif"), (400, 340))

    screen.blit(pygame.image.load("mira.gif").convert(), posicion)

    pygame.display.update()
