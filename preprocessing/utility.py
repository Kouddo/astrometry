from astropy.io import fits
import numpy as np
from os import listdir


def import_files(filepath):
    files = [fits.open(filepath + '/' + i)[0] for i in listdir(filepath) if i.endswith('.fits')]
    return files

def assert_similar(files):
        for i in files:
            assert files[0].header['GAIN'] == i.header['GAIN']
            assert files[0].header['EXPOSURE'] == i.header['EXPOSURE']
            assert files[0].header['INSTRUME'] == i.header['INSTRUME']

def average_fits(files):
    master = sum([i.data for i in files])/len(files)
    return master

def median_fits(files):
    return None