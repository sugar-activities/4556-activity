#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Image authors list
#Images published on flickr under the Creative Common License

#pattern:
#__(("Filename_wo_ext", _("Image name"), "Author name", "Link to photo"))
#__(("", _(""), "", ""))
from gettext import gettext as _

autores = {}

def __(a):
    autores[a[0]] = a[1:]

#****************************************
#paisajes
#****************************************
__(("Lago_Ypacarai", _("Lago Ypacarai"), "Rodrigo Perez", "http://www.flickr.com/photos/rodripf/5532922349"))


#****************************************
#escenas
#****************************************
__(("Precious_Moments",  _("Rosa y Frutillas"),"Fliker_2000", "http://www.flickr.com/photos/cyber-shot/3050275740"))

#****************************************
#animales
#****************************************
__(("Mother_and_baby_gorilla",  _("Mama y bebe gorila"), "mape_s", "http://www.flickr.com/photos/mape_s/333862026/"))
__(("Zebra_in_B_and_W", _("Zebra"), "mape_s", "http://www.flickr.com/photos/mape_s/346930948"))
__(("Jirafe_-_ Going_somwhere", _("Jirafa"), "Dwayne Macgowan", "http://www.flickr.com/photos/dwaynemac/383409225"))
__(("The_beautiful_lion_of_the_zoo_of_Basel.jpg", _("Leon"), "Tambako the Jaguar", "http://www.flickr.com/photos/tambako/4417060477/"))
__(("Three_ducks", _("Los tres patitos"), "mape_s", "http://www.flickr.com/photos/mape_s/333862325/"))
__(("Bighorn_sheep", _("Cabra"), "mape_s", "http://www.flickr.com/photos/mape_s/333862119/"))


#****************************************
#deportes
#****************************************
__(("O_rosilho", _("Jinete"), "Eduardo Amorin", "http://www.flickr.com/photos/bombeador/2373109553/"))
__(("Power", _("Fútbol"), "Zach Stern", "http://www.flickr.com/photos/zachstern/147590048"))
__(("Enzo_XX_Evolution", _("Auto"), "Philipp Lücke", "http://www.flickr.com/photos/philippluecke/4733545102"))


#****************************************
#transporte
#****************************************
__(("First_Air_727_100", _("Avion"), "Doug", "http://www.flickr.com/photos/caribb/84655830"))


if __name__ == "__main__":
    print autores
