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

This method returns a list of all the products that are available in the area based on location coordinates.

** Parameters **
- latitude (float) Represents the latitude component of location.
- longitude (float) Represents the longitude component of location.

** Usage **

```python
latitude = 51.5286416
longitude = -0.1015987

uber_products = uber.get_products(latitude, longitude)
print json.dumps(products, sort_keys=True, indent=4, separators=(',', ': '))
```

** Returns **

````
{
    "products": [
        {
            "capacity": 4,
            "description": "Cheap, fast & reliable",
            "display_name": "uberX",
            "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png",
            "product_id": "3cb90303-3869-4701-a8fd-92efba468a94"
        },
        {
            "capacity": 6,
            "description": "Spacious, Convenient Comfort",
            "display_name": "uberXL",
            "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberXL_london.png",
            "product_id": "d9b19d17-f013-4b98-9b3f-cf5a9e91d2aa"
        },
        {
            "capacity": 4,
            "description": "Discreet executive quality",
            "display_name": "UberEXEC",
            "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-black.png",
            "product_id": "34a6cad0-0629-4ca0-ae68-ed0cea7695ca"
        },
        {
            "capacity": 4,
            "description": "Ultimate luxury & style",
            "display_name": "UberLUX",
            "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-lux.png",
            "product_id": "ea52c793-1ad7-4c46-96b3-b1836b8cd0f9"
        },
        {
            "capacity": 5,
            "description": "Iconic, Knowledgeable & Versatile",
            "display_name": "UberTAXI",
            "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-blacktaxi2.png",
            "product_id": "6a6629df-3400-4e4b-8742-ebd79bf4ef99"
        }
    ]
}

````

JSON list of services available

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