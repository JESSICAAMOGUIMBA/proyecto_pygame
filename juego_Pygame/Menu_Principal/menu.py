import pygame
from pygame.locals import *
import os
from sys import exit


class Menu:
        
    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font('dejavu.ttf', 20)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                
                titulo, funcion = self.opciones[self.seleccionado]
                
                funcion()

        # para que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = 30
        x = 105
        y = 105
        
        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (200, 0, 0)
            else:
                color = (0, 0, 0)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)


def jugador_1 ():
    
    print (" Nuevo jugador 1")

    

def jugador_2 ():
    print (" Nuevo jugador 2")

def scores():
    print (" Scores")

def salir_del_programa():
    import sys
    print (" Gracias")
    sys.exit(0)


if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("Jugador 1", jugador_1 ),
        ("Jugador 2", jugador_2 ),
        ("Scores", scores),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((320, 240))
    

    fondo = pygame.image.load("menu.jpg").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)
