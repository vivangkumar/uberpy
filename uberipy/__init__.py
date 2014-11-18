__author__ = 'Vivan'
__version__ = '1.0'

'''
Specify modules to be imported.
'''

from uber import Uber

try:
    import httplib2
except ImportError:
    raise Exception('uberipy requires the installation of httplib2')
