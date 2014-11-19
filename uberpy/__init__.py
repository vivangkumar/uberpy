__author__ = 'Vivan'
__version__ = '1.0'

'''
Specify modules to be imported.
'''

from uber import Uber
from errors import (
    UnauthorisedException, MalformedRequestException, InvalidRequestException,
    UnacceptableContentException, NotFoundException, RateLimitException, ServerException, UberpyException
)

try:
    import httplib2
except ImportError:
    import httplib2
    raise Exception('uberpy requires the installation of httplib2')
