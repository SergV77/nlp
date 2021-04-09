#!flask/bin/python

from locLib import *

def loadModele ():
    return load_model('models/model_best290321.hdf5')