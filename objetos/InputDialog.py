#!/usr/bin/env python

import gtk
from string import atoi

class InputDialog:
    def responseToDialog(self, other, other2, entry, entry2, dialog, response, ):
        if not self.una:
            self.una = True
            dialog.response(response)
            for f in self.__listeners:
                f([atoi(entry.get_text()), atoi(entry2.get_text())])

    def __init__(self):
        self.una = False

    def show(self, texto, texto2, etiqueta):
	#base this on a message dialog
	dialog = gtk.MessageDialog(
		None,
		gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
		gtk.MESSAGE_QUESTION,
		gtk.BUTTONS_OK,
		None)
	dialog.set_markup(texto)
	#create the text input field
	entry = gtk.Entry()
        entry2 = gtk.Entry()
	#allow the user to press enter to do ok
	dialog.connect("response", self.responseToDialog, entry, entry2, dialog, gtk.RESPONSE_OK)
	#create a horizontal box to pack the entry and a label
	hbox = gtk.HBox()
	hbox.pack_start(gtk.Label(etiqueta), False, 5, 5)
	hbox.pack_end(entry)
        hbox.pack_end(entry2)
	#some secondary text
	dialog.format_secondary_markup(texto2)
	#add it and show it
	dialog.vbox.pack_end(hbox, True, True, 0)
	dialog.show_all()
	#go go go
        
	dialog.run()
        res = [atoi(entry.get_text()), atoi(entry2.get_text())]
	dialog.destroy()
        return res


    def setListener(self, functions):
        self.__listeners = functions


def m (text):
    print text


if __name__ == '__main__':
	d = InputDialog()
        d.setListener((m,))
        print d.show("Esta es una prueba", "prueba2", "nombre")
	gtk.main()