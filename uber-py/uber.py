__author__ = 'Vivan'

from api import Api


class Uber(Api):

    """
    Class holding all Uber API calls. Inherits from the base API class.
    """
    def __init__(self, client_id, server_token, secret):
        self.client_id = client_id
        self.server_token = server_token
        self.secret = secret

        super(Uber, self).__init__(self.client_id, self.server_token, self.secret)

    def get_products(self, latitude, longitude):
        """
        Get a list of all Uber products based on latitude and longitude coordinates.
        :param latitude: Latitude for which product list is required.
        :param longitude: Longitude for which product list is required.
        :return: JSON
        """
        endpoint = 'products'
        query_parameters = {
            'latitude': latitude,
            'longitude': longitude
        }

        return self.get_json(endpoint,'GET', query_parameters, None, None)

    def get_fare_estimate(self, start_latitude, start_longitude, end_latitude, end_longitude):
        """
        Returns the fare estimate based on two sets of coordinates.
        :param start_latitude: Starting latitude or latitude of pickup address.
        :param start_longitude: Starting longitude or longitude of pickup address.
        :param end_latitude: Ending latitude or latitude of destination address.
        :param end_longitude: Ending longitude or longitude of destination address.
        :return: JSON
        """
        endpoint = 'estimates/price'
        query_parameters = {
            'start_latitude': start_latitude,
            'start_longitude': start_longitude,
            'end_latitude': end_latitude,
            'end_longitude': end_longitude
        }

        return self.get_json(endpoint, 'GET', query_parameters, None, None)

    def get_time_estimate(self, start_latitude, start_longitude, customer_uuid=None, product_id=None):
        """
        Get the ETA for Uber products.
        :param start_latitude: Starting latitude.
        :param start_longitude: Starting longitude.
        :param customer_uuid: (Optional) Customer unique ID.
        :param product_id: (Optional) If ETA is needed only for a specific product type.
        :return: JSON
        """

        endpoint = 'estimates/time'
        query_parameters = {
                'start_latitude': start_latitude,
                'start_longitude': start_longitude
            }

        if customer_uuid is not None:
            query_parameters['customer_uuid'] = customer_uuid
        elif product_id is not None:
            query_parameters['product_id'] = product_id
        elif customer_uuid is not None and product_id is not None:
            query_parameters['customer_uuid'] = customer_uuid
            query_parameters['product_id'] = product_id

        return self.get_json(endpoint, 'GET', query_parameters, None, None)
