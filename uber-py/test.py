__author__ = 'Vivan'

from uber import Uber
import json
from errors import UnauthorisedException, MalformedRequestException, InvalidRequestException, \
    UnacceptableContentException, NotFoundException, RateLimitException, ServerException, UberPyException
uber = Uber('CPPRD08zE_pagsI5CmSyh3URj7ITxpXx','TbP2woYtHL2_pPuBxM2r-Q8OoPr6BFBwKUt_w4sZ','UcAhCFC2SdKXKb2_jNjwmyy8LtuSg552C5ZQ9yPK')
#estimate = uber.get_fare_estimate(51.5289526,-0.1410641,51.5107835,-0.1167915)
try:
    products = uber.get_products(51.5286416,-0.1015987)
    print json.dumps(products, sort_keys=True, indent=4, separators=(',', ': '))


except UberPyException as e:
    print e.get_message
#print products
#print estimate

