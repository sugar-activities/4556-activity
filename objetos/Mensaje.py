#!/usr/bin/env python

import gtk

class Mensaje:

    def __init__(self, texto):
        #base this on a message dialog
	self.window = gtk.Dialog("Abrir")


        self.window.connect("delete_event", self.deleteEvent)
        self.window.set_position(gtk.WIN_POS_CENTER)

        ok = gtk.Button("OK")
        ok.connect("clicked", self.cerrar)
        self.window.action_area.pack_start(ok)

        lbl = gtk.Label()
        lbl.set_markup(texto)
        self.window.get_content_area().pack_start(lbl, True, True, 0)

        self.window.show_all()

    def cerrar(self, b):
        self.window.destroy()

    def deleteEvent(self, widget, event, data=None):
        self.window.destroy()
        
if __name__ == '__main__':
	d = About()
        print d.show()
	gtk.main()