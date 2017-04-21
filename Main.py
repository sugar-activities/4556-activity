# -*- coding: utf-8 -*-
import sys
sys.path.append('./generadores')
sys.path.append('./objetos')

from PuzzleRectangulos import PuzzleRectangulos
import pygame
from pygame.locals import *

import gtk

from Mensaje import Mensaje
from InputDialog import InputDialog

__author__ = "rodripf"
__date__ = "$25/01/2012 10:42:07 AM$"

class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.iniciado = False
        self.img = ""

    def pc (self):
        pygame.display.init()
        self.display = pygame.display.set_mode((1024, 768))
        
    def iniciar(self):
        if not self.iniciado:
            self.surf = pygame.display.get_surface()
            if self.img != "":
                self.result = [0,0]
                def elegido(d):
                    self.result = d

                d = InputDialog()

                d.setListener((elegido,))

                print d.show("Eije el tamaño del puzzle", "Ancho", "")

                self.jugar(self.img, self.result)

        self.iniciado = True


    def jugar(self, imagen, size):
        img = pygame.image.load(imagen)

        g = PuzzleRectangulos(size, img)
        g.onCompletado.append(lambda: Mensaje("<b><big>Felicitaciones!</big></b>\n\nGanaste,\n has completado el puzzle :-)"))
        g.generar()
        g.entreverar()

        self.moviendo = False       

        while True:
            self.updGTK()
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                    return
                elif event.type == 5: #clic
                    p = pygame.mouse.get_pressed()
                    print p
                    if p[0] == 1 and p[1] == 0 and p[2] == 0:
                        pos = pygame.mouse.get_pos()
                        self.sel = g.checkClic(pos)
                        
                        #para resetear el movimiento relativo
                        pygame.mouse.get_rel()

                        if self.sel != None:
                            self.moviendo = True
                elif event.type == 6:
                    if self.moviendo:
                        g.checkTablero(self.sel)
                        self.moviendo = False               

            if self.moviendo:
                g.mover(self.sel)

            rects = g.dibujar(self.surf)
            pygame.display.update(rects)

            

    def updGTK(self):
        while gtk.events_pending():
            gtk.main_iteration()



if __name__ == "__main__":
    m = Main()
    m.pc()
    m.iniciar()
    m.jugar()