from astropy.io import fits

import numpy

from os import listdir
from os.path import isfile,


def dark_gen(filepath):
    files = [fits.open(i) for i in listdir(filepath) if i.endswith.lower(('.fits'))]
    for i in files 

