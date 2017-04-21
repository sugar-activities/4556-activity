#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="rodripf"
__date__ ="$13/02/2012 09:22:53 AM$"

from sugar.datastore import datastore
import gtk
import gobject
import os

class JobjectWrapper():
    def __init__(self):
        self.__jobject = None
        self.__file_path = None
    def setJobject(self,  jobject):
        self.__jobject = jobject
    def setFilePath(self,  file_path):
        self.__file_path = file_path
    def getFilePath(self):
        if  self.__jobject != None:
            return self.__jobject.getFilePath()
        else:
            return self.__file_path

class Archivos:
    def loadJournalTable(self):
        self.ls_right =  gtk.ListStore(
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
            gobject.TYPE_PYOBJECT)
        ds_objects, num_objects = datastore.find(
            {'mime_type':['image/jpeg',
            'image/gif', 'image/tiff',  'image/png']},
            properties=['uid', 'title', 'mime_type'])
        self.ls_right.clear()
        for i in xrange (0, num_objects, 1):
            iter = self.ls_right.append()
            title = ds_objects[i].metadata['title']
            mime_type = ds_objects[i].metadata['mime_type']
            if mime_type == 'image/jpeg' \
                and not title.endswith('.jpg') \
                and not title.endswith('.jpeg') \
                and not title.endswith('.JPG') \
                and not title.endswith('.JPEG') :
                title = title + '.jpg'
            if mime_type == 'image/png' \
                and not title.endswith('.png') \
                and not title.endswith('.PNG'):
                title = title + '.png'
            if mime_type == 'image/gif' \
                and not title.endswith('.gif')\
                and not title.endswith('.GIF'):
                title = title + '.gif'
            if mime_type == 'image/tiff' \
                and not title.endswith('.tiff')\
                and not title.endswith('.TIFF'):
                title = title + '.tiff'
            self.ls_right.set(iter, COLUMN_IMAGE, title)
            jobject_wrapper = JobjectWrapper()
            jobject_wrapper.setJobject(ds_objects[i])
            self.ls_right.set(iter, COLUMN_PATH,
                jobject_wrapper)

        valid_endings = ('.jpg',  '.jpeg', '.JPEG',
            '.JPG', '.gif', '.GIF', '.tiff',
            '.TIFF', '.png', '.PNG')
        ds_mounts = datastore.mounts()
        if len(ds_mounts) == 1 and ds_mounts[0]['id'] == 1:
            # datastore.mounts() is stubbed out,
            # we're running .84 or better
            for dirname, dirnames, filenames in os.walk('/media'):
                if '.olpc.store' in dirnames:
                    dirnames.remove('.olpc.store')
                    # don't visit .olpc.store directories
                for filename in filenames:
                    if filename.endswith(valid_endings):
                        iter = self.ls_right.append()
                        jobject_wrapper = JobjectWrapper()
                        jobject_wrapper.setFilePath(
                            os.path.join(dirname, filename))
                        self.ls_right.set(iter, COLUMN_IMAGE,
                            filename)
                        self.ls_right.set(iter, COLUMN_PATH,
                            jobject_wrapper)
        self.ls_right.set_sort_column_id(COLUMN_IMAGE,
            gtk.SORT_ASCENDING)

        print ds_objects
        print num_objects

if __name__ == "__main__":
    print "Hello World";
