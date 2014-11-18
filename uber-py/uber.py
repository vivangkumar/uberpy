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
        Lists all the Uber products available in an area.
        Params:
            latitude: Latitude coordinate for which the products are to be retrieved.
            longitude: Longitude coordinate for which the products are to be retrieved.
        Returns:
            JSON returned by Uber
        """
        endpoint = 'products'
        query_parameters = {
            'latitude': latitude,
            'longitude': longitude
        }

        return self.get_json(endpoint,'GET', query_parameters, None, None)