from astropy.io import fits

import numpy

from os import listdir


def dark_gen(filepath):
    files = [fits.open(filepath + '/' + i)[0] for i in listdir(filepath) if i.endswith('.fits')]
    for i in files:
        assert files[0].header['GAIN'] == i.header['GAIN']
        assert files[0].header['EXPOSURE'] == i.header['EXPOSURE']
        assert files[0].header['INSTRUME'] == i.header['INSTRUME']
    
    master = sum([i.data for i in files])/len(files)
    return master

    


