__author__ = 'Vivan'

import json
from httplib2 import Http

from errors import UnauthorisedException, MalformedRequestException, InvalidRequestException, \
    UnacceptableContentException, NotFoundException, RateLimitException, ServerException
from urllib import urlencode


class Uber:

    """
    Base class to set up credentials
    """

    def __init__(self, client_id, server_token, secret):
        self.client_id = client_id

        if self.server_token == '':
            raise Exception('Server token is required.')
        else:
            self.server_token = server_token
        self.secret = secret

        self.client = Http()

    def add_credentials(self, query_parameters):

        """
        Adds the Uber credentials to the uri.
        Params:
            query_parameters: Takes the existing set of query parameters and adds the 'server_token' to it.
        Returns:
            query_parameters: Modified parameters with the credentials.
        """

        query_parameters['server_token'] = self.server_token

        return query_parameters

    def sanitise_path(self, path):

        """
        Ensure a preceding / in the path
        Params:
            path: The uri path to be checked for.
        Returns:
            path: Modified version of the path.
        """
        if path[0] != '/':
            path = '/' + path

        return path

    def check_status(self, uri, response):

        """
        Check the HTTP status codes for known errors that the Uber API may return.
        Params:
            uri: The uri of request.
            response: Response returned by Uber API.
        Returns:
            None
        """

        if response.status == 400:
            raise MalformedRequestException(uri, response)

        if response.status == 401:
            raise UnauthorisedException(uri, response)

        if response.status == 404:
            raise NotFoundException(uri, response)

        if response.status == 406:
            raise UnacceptableContentException(uri, response)

        if response.status == 422:
            raise InvalidRequestException(uri, response)

        if response.status == 429:
            raise RateLimitException(uri, response)

        if response.status >= 500:
            raise ServerException(uri, response)

    def build_request(self, path, query_parameters):

        """
        Construct URI for the API call.
        Params:
            path: The API end point to be used.
            query_parameters: Parameters to be added to the query.
        Returns:
            url: The fully constructed URL
        """
        url = 'https://api.uber.com/v1' + self.sanitise_path(path)
        url += '?' + urlencode(query_parameters)

        return url

    def get_json(self, uri_path, http_method='GET', query_parameters=None, body=None, headers=None):

        """
        Make an API call and get the response returned in JSON.
        Params:
            uri_path: The endpoint to be used to make the request.
            http_method: HTTP method to be used.
            query_parameters: Parameters to be included in the request.
            body: Optional body of the request.
            headers: Optional headers to be added, if any.
        """
        query_parameters = query_parameters or {}
        headers = headers or {}

        # Add credentials to the request
        query_parameters = self.add_credentials(query_parameters)
        # Build the request uri with parameters
        uri = self.build_request(uri_path, query_parameters)

        if http_method in ('POST', 'PUT', 'DELETE') and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        headers['Accept'] = 'application/json'
        # Make the request
        response, content = self.client.request(
            uri=uri,
            method=http_method,
            body=body,
            headers=headers
        )

        # Check for known errors that could be returned
        self.check_status(uri, response)

        return json.loads(content.decode('utf-8'))

    def products(self, latitude, longitude):
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