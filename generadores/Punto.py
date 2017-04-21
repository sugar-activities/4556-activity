# -*- coding: utf-8 -*-

__author__="rodripf"
__date__ ="$25/01/2012 10:59:46 AM$"

import pygame

class Punto(pygame.sprite.Sprite):
     def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pos + (1,1))
