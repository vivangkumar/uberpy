__author__ = 'Vivan'
__version__ = '1.0'

'''
Specify modules to be imported.
'''

from uber import Uber
from errors import (
    UnauthorisedException, MalformedRequestException, InvalidRequestException,
    UnacceptableContentException, NotFoundException, RateLimitException, ServerException, UberPyException
)

try:
    import httplib2
except ImportError:
    raise Exception('uberipy requires the installation of httplib2')
