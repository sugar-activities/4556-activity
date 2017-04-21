# -*- coding: utf-8 -*-

import pygame

class Ficha(pygame.sprite.Sprite):
    def __init__(self, id, rect, image= None, color=None, mask = None):
        pygame.sprite.Sprite.__init__(self)

        self.id = id
        if image!=None:
            self.image = image
        elif color!=None:
            self.color = color
        else:
            assert "Se precisa o una imagen o un color"
            
        if rect != None:
            self.rect = pygame.Rect(rect)
        else:
             assert "Se precisa un rectangulo rect con la posicion y el tamanio"

        if mask!=None:
            self.mask = mask

        #si no tiene imagen lo genero
        if image == None:
            if mask==None:
                self.image = pygame.Surface((self.rect[2], self.rect[3]))
                self.image.fill(color)


        self.__position = (0,0)

    def setClicked(self, clicked):
        #TODO: cambiar la imagen, resaltar
        self.__clicked=clicked
        
    def getClicked(self, clicked):
        return self.__clicked


    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def __generarFichaColor(self):
        pass



