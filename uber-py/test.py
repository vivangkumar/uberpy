__author__ = 'Vivan'

from uber import Uber
from errors import UnauthorisedException, MalformedRequestException, InvalidRequestException, \
    UnacceptableContentException, NotFoundException, RateLimitException, ServerException
uber = Uber('CPPRD08zE_pagsI5CmSyh3URj7ITxpXx','TbP2woYtHL2_pPuBxM2r-Q8OoPr6BFBwKUt_w4sZ','UcAhCFC2SdKXKb2_jNjwmyy8LtuSg552C5ZQ9yPK')
#products = uber.get_products(51.5286416,-0.1015987)
#estimate = uber.get_fare_estimate(51.5289526,-0.1410641,51.5107835,-0.1167915)
try:
    eta = uber.get_time_estimate(None,-0.1410641)
    print eta
except InvalidRequestException as e:
    print e.get_message()
#print products
#print estimate


