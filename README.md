# uberpy

[![Build Status](https://travis-ci.org/vivangkumar/uberpy.svg?branch=master)](https://travis-ci.org/vivangkumar/uberpy)

A python based wrapper for [Uber's public API] (https://developer.uber.com/).

It provides flexibility to retrieve JSON responses from the API as well as translating them to objects.

## Version History

### 1.0

- Initial release with most API calls except a few mentioned in the To-do section.

## Getting Started

### Dependencies

This package requires Python 2.5+

Essential requirements-

- [httplib2] (https://github.com/jcgregorio/httplib2)
- Uber Server Token, Client ID, Secret

### Installation
To install by downloading the source:

    sudo python setup.py install

Alternatively, using pip:

    sudo pip install uberpy

### Authorisation

#### User credentials

Credentials can be obtained from [Uber's API website] (https://developer.uber.com/)
This includes a client_id, secret, and server_token.

For the initial version, only the server_token is required as OAuth 2.0 is currently not implemented.
Future versions will, however support OAuth 2.0.

## Documentation

Check out the latest official [API documentation] (https://developer.uber.com/v1/endpoints/) for a detailed reference.

First, import uberipy:
```python
from uberpy import Uber
```

Create a new Uber instance as follows:
```python
uber = Uber(client_id, server_token, secret)
```

This will give access to the underlying API methods.

### JSON Methods

#### GET /v1/products - get_products(latitude, longitude)

This method returns a list of all the products that are available in the area based on location coordinates.

**Parameters**

- latitude (float) Represents the latitude component of location.
- longitude (float) Represents the longitude component of location.

**Usage**

```python
latitude = 51.5286416
longitude = -0.1015987

uber_products = uber.get_products(latitude, longitude)
# Do something with it
```

#### GET /v1/estimates/price - get_price_estimate(start_latitude, start_longitude, end_latitude, end_longitude)

This method returns an estimate of the fare for a trip between two locations.

**Parameters**

- start_latitude (float) Latitude component of start location.
- start_longitude (float) Longitude component of start location.
- end_latitude (float) Latitude component of end location.
- end_longitude (float) Longitude component of end location.

**Usage**

```python
start_latitude = 51.5252162
start_longitude = -0.1036919
end_latitude = 51.5049949
end_longitude = -0.0103968

fare_estimate = uber.get_fare_estimate(start_latitude, start_longitude, end_latitude, end_longitude)
# Do something with it
```

#### GET /v1/estimates/time - get_time_estimate(start_latitude, start_longitude, customer_uuid, product_id)

Get the estimated time of arrival of a Uber product.

**Parameters**

- start_latitude (float) Latitude component.
- start_longitude (float) Longitude component.
- customer_uuid (string) *Optional* Unique customer identifier to be used for experience customization.
- product_id (string) *Optional* Unique identifier representing a specific product for a given latitude & longitude.

**Usage**

```python
start_latitude = 51.5252162
start_longitude = -0.1036919

time_estimate = uber.get_time_estimate(start_latitude, start_longitude, customer_uuid=None, product_id=None)
# Do something with it
```

#### GET /v1/promotions - get_promotions(start_latitude, start_longitude, end_latitude, end_longitude)

Returns the promotions that will be available to a new user based on their location.

**Parameters**

- start_latitude (float) Latitude component of start location.
- start_longitude (float) Longitude component of start location.
- end_latitude (float) Latitude component of end location.
- end_longitude (float) Longitude component of end location.

**Usage**

```python
start_latitude = 51.5252162
start_longitude = -0.1036919
end_latitude = 51.5049949
end_longitude = -0.0103968

promotions = uber.get_promotions(start_latitude, start_longitude, end_latitude, end_longitude)
# Do something with it
```

### Tests

To run the tests, you will have to obtain
- server_token
- client_id
- secret
 
Add them to the tests before you run them.
You can always comment out the tests you dont want.

### Errors and Exceptions

There are a few possible exceptions that can be thrown based on the error codes sent back by the API.
You can look out for these errors when implementing.

- *UnauthorisedException*: If the API was accessed using improper credentials (401)
- *MalformedRequestException*: Malformed request was sent to server (400)
- *NotFoundException*: Resource was not found (404)
- *UnacceptableContentException*: Client sent an accepts header for a content type which does not exist on the server (406)
- *InvalidRequestException*: If an invalid request is sent (422)
- *RateLimitException*: If the allocated request quota expires (429)
- *ServerException*: If the server returns a status code >= 500.
- *UberpyException*: General exceptions that may be thrown.

### Todo

Functions to create Uber objects to extend classes and provide flexibility.

Currently, the library does not include any of the OAuth requiring API calls.

These include
- /v1.1/history : This returns data about a user's history
- GET /v1/me : Returns information about the user who has authorized with the application.

### Contributors

[Vivan] (https://github.com/vivangkumar)

## Licence

This code is licenced under the [MIT Licence](http://opensource.org/licenses/mit-license.php)