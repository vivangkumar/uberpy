__author__ = 'Vivan'

from api import Api


class Uber(Api):

    """
    Class holding all Uber API calls. Inherits from the base API class.
    """
    def __init__(self, client_id, server_token, secret):

        super(Api, self).__init__(client_id, )
