# uber-py

A python based wrapper for [Uber's public API] (https://developer.uber.com/)
It provides flexibility to retrieve JSON responses from the API as well as translating them to objects.

# Version History
## 1.0.0

## Getting Started

### Dependencies

This package requires Python 2.5+

Essential requirements-

- [httplib2] (http://code.google.com/p/httplib2/)
- Uber Server Token, Client ID, Secret

### Installation
To install by downloading the source:

    sudo python setup.py install

Alternatively, using pip:

    sudo pip install uber-py

### Authorisation

#### User credentials

Credentials can be obtained from [Uber's API website] (https://developer.uber.com/)
This includes a client_id, secret, and server_token.

For the initial version, only the server_token is required as OAuth 2.0 is currently not implemented.
Future versions will, however support OAuth 2.0.

## Documentation

Check out the latest official API documentation at https://developer.uber.com/v1/endpoints/

Create a new Uber instance as follows:
```python
from uber import Uber

uber = Uber(client_id, server_token, secret)
```

This will give access to the underlying API methods.

### JSON Methods

#### GET /v1/products - get_products(latitude, longitude)

#### GET /v1/estimates/price - get_fare_estimate(start_latitude, start_longitude, end_latitude, end_longitude)

#### GET /v1/estimates/time - get_time_estimate(start_latitude, start_longitude, customer_uuid, product_id)

#### GET /v1/promotions - get_promotions(start_latitude, start_longitude, end_latitude, end_longitude)

### Todo

Currently, the library does not include any of the OAuth requiring API calls.

These include
- /v1.1/history : This returns data about a user's history
- GET /v1/me : Returns information about the user who has authorized with the application.

### Contributors

[Vivan] (https://github.com/vivangkumar)

## Licence

This code is licenced under the [MIT Licence](http://opensource.org/licenses/mit-license.php)