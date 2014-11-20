__author__ = 'Vivan'


import unittest
import os

from uberpy.uber import Uber
from uberpy.errors import InvalidRequestException

mock_server_token = os.environ['UBER_SERVER_TOKEN']
mock_client_id = ''
mock_secret = ''


class UberpyApiTests(unittest.TestCase):

    def setUp(self):
        self.uber = Uber(mock_client_id, mock_server_token, mock_secret)

        self.start_latitude = 51.5252162
        self.start_longitude = -0.1036919
        self.end_latitude = 51.5049949
        self.end_longitude = -0.0103968

        self.product_id = '3cb90303-3869-4701-a8fd-92efba468a94'

    def test_get_products(self):
        products = self.uber.get_products(self.start_latitude, self.start_longitude)
        self.assertTrue(products is not None)

    def test_get_products_invalid(self):
        self.assertRaises(InvalidRequestException, self.uber.get_products, None, self.start_longitude)

    def test_get_price_estimate(self):
        price_estimate = self.uber.get_price_estimate(self.start_latitude, self.start_longitude, self.end_latitude,
                                                      self.end_longitude)
        self.assertTrue(price_estimate is not None)

    def test_get_price_estimate_invalid(self):
        self.assertRaises(InvalidRequestException, self.uber.get_price_estimate, self.start_latitude,
                          self.start_longitude, None, None)

    def test_get_time_estimate_1(self):
        time_estimate = self.uber.get_time_estimate(self.start_latitude, self.start_longitude, None, None)
        self.assertTrue(time_estimate is not None)

    def test_get_time_estimate_2(self):
        time_estimate = self.uber.get_time_estimate(self.start_latitude, self.start_longitude, self.product_id, None)
        self.assertTrue(time_estimate is not None)

    def test_get_time_estimate_invalid(self):
        self.assertRaises(InvalidRequestException, self.uber.get_time_estimate, self.start_latitude,
                          None, None, None)

    def test_get_promotions(self):
        promotions = self.uber.get_promotions(self.start_latitude, self.start_longitude,
                                              self.end_latitude, self.end_longitude)
        self.assertTrue(promotions is not None)

    def test_get_promotions_invalid(self):
        self.assertRaises(InvalidRequestException, self.uber.get_promotions, None,
                          self.start_longitude, self.end_latitude, self.end_longitude)

if __name__ == '__main__':
    unittest.main()
