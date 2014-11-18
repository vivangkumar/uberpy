__author__ = 'Vivan'
__version__ = '1.0.0'

'''
Specify modules to be imported.
'''

import json

try:
    import httplib2
except ImportError:
    raise Exception('uber-py requires the installation of httplib2')
