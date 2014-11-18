__author__ = 'Vivan'

from uber import Uber

uber = Uber('CPPRD08zE_pagsI5CmSyh3URj7ITxpXx','TbP2woYtHL2_pPuBxM2r-Q8OoPr6BFBwKUt_w4sZ','UcAhCFC2SdKXKb2_jNjwmyy8LtuSg552C5ZQ9yPK')
products = uber.get_products(51.5286416,-0.1015987)

print products

