# -*- coding: utf-8 -*-

__author__="rodripf"
__date__ ="$24/01/2012 01:11:33 PM$"

import pygame
from Punto import Punto
import random

class PuzzleBase:
    POSICION_IMG = (50, 50)
    TOLERANCIA_ENCAJE = 0.2
    VOLVER_A_MOVER = True
    
    def __init__(self, size, imagen):
        self.size = size
        self.imagen = imagen
        self.pixelesImg = imagen.get_rect()[2:]
        self.fichas = pygame.sprite.OrderedUpdates()
        self.tablero = pygame.sprite.RenderUpdates()
        self.fondo = pygame.sprite.RenderUpdates()
        self.fondo.add(Fondo())
        

        self.bien = []
        
        #funciones para callbacks
        self.onPiezaBien = []
        self.onCompletado = []

        self.posAnt = (0,0)

    def generar(self):
        self.fichas.empty()
        self.tablero.empty()
        pass

    def checkClic(self, pos):
        #chequea si se hizo clic en una ficha y la retorna
        p=Punto(pos)
        sprs = pygame.sprite.spritecollide(p, self.fichas, False)

        if not self.VOLVER_A_MOVER: #las que ya estan bien no se pueden mover
            sprs = [s for s in sprs if s not in self.bien]

        if sprs != []:
            clic = sprs[-1]
            self.fichas.remove(clic)
            self.fichas.add(clic)
            if self.VOLVER_A_MOVER and clic in self.bien:
                self.bien.remove(clic)
            self.posAnt = pos
            return clic
        else:
            return None


    def mover(self, sel):
        pos = pygame.mouse.get_pos()
        mouseMov = (pos[0] - self.posAnt[0], pos[1] - self.posAnt[1])
        self.posAnt = pos        
    
        nuevaPos = (sel.rect[0] + mouseMov[0], sel.rect[1] + mouseMov[1])
        sel.rect = pygame.Rect(nuevaPos + (sel.rect[2], sel.rect[3]))

    def checkTablero(self, sel):
        #chequea si la ficha cayo cerca en alguna ficha del tablero
        #si si la acomoda
        pass

    def entreverar(self):
        fwidth = int(self.pixelesImg[0] / self.size[0])
        fheight = int(self.pixelesImg[1] / self.size[1])
        sw, sh = pygame.display.get_surface().get_rect()[2:]
        for s in self.fichas.sprites():
            rx = random.randint(0, sw - fwidth)
            ry = random.randint(0, sh - fheight)
            s.rect[0] = rx
            s.rect[1] = ry


    def dibujar(self, surf):
        rect = self.fondo.draw(surf)
        rect += self.tablero.draw(surf)
        rect += self.fichas.draw(surf)
        return rect

    def corresponde(self, ficha, fichaTablero):
        return ficha.id == fichaTablero.id


############################################################################
####                    CALLBACKS                                       ####
############################################################################

    def fichaBienCB(self, ficha):
        for f in self.onPiezaBien:
            f()

        self.bien.append(ficha)

        print "bien"

        if len(self.bien) == self.size[0] * self.size[1]:
            self.completadoCB()

    def completadoCB(self):
        for f in self.onCompletado:
            f()

        print "Ganaste!"


class Fondo(pygame.sprite.Sprite):
    COLOR_DE_FONDO = (255, 255, 255)
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        res = pygame.display.get_surface().get_rect()
        self.image = pygame.Surface((res[2], res[3]))
        self.image.fill(self.COLOR_DE_FONDO)
        self.rect = pygame.Rect((0,0,res[2], res[3]))