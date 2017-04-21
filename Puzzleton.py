#! /usr/bin/python
# -*- coding: utf-8 -*-

#################################################################################
#    PUZZLETON - Crea puzzles con tus imagenes
#  Copyright (C) 2012 - Rodrigo Perez Fulloni
#Departamento de Ingenieria, Fundacion Teleton
#             Montevideo, Uruguay
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#################################################################################

import sugar.graphics.toolbarbox


__author__ = "rodripf"
__date__ = "$24/01/2012 10:12:42 AM$"



import sys
sys.path.append('./generadores')
sys.path.append('./objetos')

from gettext import gettext as _

import gtk

from sugar.activity import activity
import sugargame.canvas

import logging
import time

from Main import Main
from ElegirImg import ElegirImg
import ControlFactory
from threading import Thread




class Puzzleton(activity.Activity):
    _NEW_TOOLBAR_SUPPORT = True
    try:
        from sugar.graphics.toolbarbox import ToolbarBox
        print sugar.graphics.toolbarbox.ToolbarBox
        from sugar.graphics.toolbarbox import ToolbarButton
        from sugar.activity.widgets import StopButton
        print "importado"
    except:
        print "no importado"
        _NEW_TOOLBAR_SUPPORT = False


    DEFAULT_SIZE = [3, 3]
    def __init__(self, handle):
        self.size = self.DEFAULT_SIZE
	activity.Activity.__init__(self, handle, False)

        def puzzleToolbar(toolbar):
            ControlFactory.labelFactory(_("Cantidad de piezas") + ": ", toolbar)
            ControlFactory.labelFactory(_("Ancho") + " ",toolbar)
            ControlFactory.spinFactory(self.DEFAULT_SIZE[0], 1, 30, self.cambiarAncho, toolbar)
            ControlFactory.labelFactory(" x " + _("Alto") + " ", toolbar)
            ControlFactory.spinFactory(self.DEFAULT_SIZE[1], 1, 30, self.cambiarAlto, toolbar)
            self.cntFichasLBL = \
            ControlFactory.labelFactory(" = " + "9 " + _("piezas"), toolbar)
            ControlFactory.separatorFactory(toolbar)
            ControlFactory.labelFactory(_("Abrir galeria") + ": ", toolbar)
            ControlFactory.buttonFactory('open', toolbar, self.abrir, tooltip=_('Abrir'))
            ControlFactory.separatorFactory(toolbar)


        if self._NEW_TOOLBAR_SUPPORT: #toolbar nuevo
            print sugar.graphics.toolbarbox.ToolbarBox()
            self.toolbar_box = sugar.graphics.toolbarbox.ToolbarBox()
           
            puzzleToolbar(self.toolbar_box.toolbar)

            stop_button = sugar.activity.widgets.StopButton(self)
            stop_button.props.accelerator = '<Ctrl><Shift>Q'
            self.toolbar_box.toolbar.insert(stop_button, -1)
            stop_button.show()
            
            self.set_toolbar_box(self.toolbar_box)
            self.toolbar_box.show()

        else: #old toolbar
            toolbox = activity.ActivityToolbox(self)



            #activity toolbar
            self.activity_tb = toolbox.get_activity_toolbar()
            self.activity_tb.share.props.visible = False


            ##############toolbar nuevo Puzzle################
            self.puzzleNuevoTB = gtk.Toolbar()
            puzzleToolbar(self.puzzleNuevoTB)

            #boton abrir

           

            #toolbox
            toolbox.add_toolbar(_("Puzzle Nuevo"), self.puzzleNuevoTB)
            toolbox.show_all()

            self.set_toolbox(toolbox)
            toolbox.show()

        #canvas
        self.canv = sugargame.canvas.PygameCanvas(self)
        self.set_canvas(self.canv)

        self.main = Main()
        self.canv.grab_focus()
        self.canv.run_pygame(self.main.iniciar)  
        print "init!"


#       self.main.jugar()

    def abrir(self, boton):
        e = ElegirImg()
        e.onAbrir.append(self.cargada)
        e.show()

    def cambiarAncho(self, b):
        self.size[0] = b.get_value_as_int()
        self.cntFichasLBL.set_label(" = " + str(self.size[0] * self.size[1]) + " " + _("piezas"))

    def cambiarAlto(self, b):
        self.size[1] = b.get_value_as_int()
        self.cntFichasLBL.set_label(" = " + str(self.size[0] * self.size[1]) + " " + _("piezas"))

    def cargada(self, img):
        self.main.jugar(img, self.size)

    def close(self, skip_save=False):
        activity.Activity.close(self, True)

    def read_file(self, file_path):
        if file_path.endswith(("bmp", "gif", "jpeg", "png", "tiff", "tif", "jpg", "jpe")):
            self.img = file_path
            self.main.img = file_path
            print "readfile!"
