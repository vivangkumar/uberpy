__author__ = 'Vivan'

import json
from httplib2 import Http
from urllib import urlencode

from errors import (
    UnauthorisedException, MalformedRequestException, InvalidRequestException,
    UnacceptableContentException, NotFoundException, RateLimitException, ServerException, UberpyException
)


class Api(object):
    """
    Base class to handle url building, parameter encoding, adding authorisation and receiving responses.
    """

    def __init__(self, client_id, server_token, secret):
        """
        Instantiate a new Api object.
        :param client_id: Client ID for an application provided by Uber.
        :param server_token: Server token for an application provided by Uber.
        :param secret: Secret for an application provided by Uber.
        """
        self.client_id = client_id

        if self.server_token == '' or self.server_token is None:
            raise UberpyException('Server token is required.')
        else:
            self.server_token = server_token
        self.secret = secret

        self.client = Http()

    def add_credentials(self, query_parameters):
        """
        Adds the Uber server token to the query parameters to make an authorised request.
        :param query_parameters: Query parameters to be sent.
        :return: string
        """
        query_parameters['server_token'] = self.server_token

        return query_parameters

    @staticmethod
    def sanitise_path(path):
        """
        Adds a '/' to the path if it does not exist.
        :param path: Path that is to be sanitised.
        :return: string
        """
        if path[0] != '/':
            path = '/' + path

        return path

    @staticmethod
    def check_status(content, response):
        """
        Check the response that is returned for known exceptions and errors.
        :param response: Response that is returned from the call.
        :raise:
         MalformedRequestException if `response.status` is 400
         UnauthorisedException if `response.status` is 401
         NotFoundException if `response.status` is 404
         UnacceptableContentException if `response.status` is 406
         InvalidRequestException if `response.status` is 422
         RateLimitException if `response.status` is 429
         ServerException if `response.status` > 500
        """

        if response.status == 400:
            raise MalformedRequestException(content, response)

        if response.status == 401:
            raise UnauthorisedException(content, response)

        if response.status == 404:
            raise NotFoundException(content, response)

        if response.status == 406:
            raise UnacceptableContentException(content, response)

        if response.status == 422:
            raise InvalidRequestException(content, response)

        if response.status == 429:
            raise RateLimitException(content, response)

        if response.status >= 500:
            raise ServerException(content, response)

    def build_request(self, path, query_parameters):
        """
        Build the HTTP request by adding query parameters to the path.
        :param path: API endpoint/path to be used.
        :param query_parameters: Query parameters to be added to the request.
        :return: string
        """
        url = 'https://api.uber.com/v1' + self.sanitise_path(path)
        url += '?' + urlencode(query_parameters)

        return url

    def get_json(self, uri_path, http_method='GET', query_parameters=None, body=None, headers=None):
        """
        Fetches the JSON returned, after making the call and checking for errors.
        :param uri_path: Endpoint to be used to make a request.
        :param http_method: HTTP method to be used.
        :param query_parameters: Parameters to be added to the request.
        :param body: Optional body, if required.
        :param headers: Optional headers, if required.
        :return: JSON
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
        response, content = self.client.request(
            uri=uri,
            method=http_method,
            body=body,
            headers=headers
        )

        # Check for known errors that could be returned
        self.check_status(content, response)

        return json.loads(content.decode('utf-8'))
