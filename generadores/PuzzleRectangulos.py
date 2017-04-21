from PuzzleBase import PuzzleBase
from Ficha import Ficha
import pygame
# -*- coding: utf-8 -*-

__author__ = "rodripf"
__date__ = "$24/01/2012 01:28:19 PM$"

class PuzzleRectangulos(PuzzleBase):
    def generar(self):
        PuzzleBase.generar(self)
        #divido en rectangulos
        self.width = int(self.pixelesImg[0] / self.size[0])
        self.height = int(self.pixelesImg[1] / self.size[1])

        rects = [] #rectangulos
        self.imgFichas = [] #rectangulos recortados

        posAnt = 0
        for x in xrange(self.size[0]):
            for y in xrange(self.size[1]):
                r = (x * self.width, y * self.height, self.width, self.height)
                rects.append(r)
                 #recorto la imagen en esos rectangulos
                img = self.imagen.subsurface(r)
                self.imgFichas.append(img)
                #genero la ficha
                self.fichas.add(Ficha((x,y), (0,0,self.width,self.height), image = img))

                #genero el tablero y lo pongo en posicion con sus id
                self.tablero.add(Ficha((x,y), \
                (r[0] + PuzzleBase.POSICION_IMG[0], r[1] + PuzzleBase.POSICION_IMG[1]) + r[2:], color=(100,100,100)))

    def checkTablero(self, sel):
        tabl = pygame.sprite.spritecollide(sel, self.tablero, False)
        sirve = None
        #chequeo cual esta mas aprox
        if tabl != []:
            mejor = 0
            for t in tabl:
                intersect = t.rect.clip(sel)
                area = intersect[2] * intersect[3]
                if area > mejor:
                    mejor = area
                    sirve = t
            if mejor > self.width * self.height * (1 - PuzzleBase.TOLERANCIA_ENCAJE):
                sel.rect = sirve.rect
                if self.corresponde(sel, sirve):
                    self.fichaBienCB(sel)



