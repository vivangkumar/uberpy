__author__ = 'Vivan'

'''
Class representing a Uber Product.
'''


class UberProduct(object):

    def __init__(self, product_id, description, display_name, capacity, image):
        """
        Instantiate a new UberProduct object.
        :param product_id: Product ID of the Uber product.
        :param description: Description of the Uber product.
        :param display_name: Display name of the Uber product.
        :param capacity: Capacity of the Uber product.
        :param image: Image for the Uber product.
        """
        self.product_id = product_id
        self.description = description
        self.display_name = display_name
        self.capacity = capacity
        self.image = image

    @property
    def get_product_id(self):
        return self.product_id

    @property
    def get_description(self):
        return self.description

    @property
    def get_display_name(self):
        return self.display_name

    @property
    def get_capacity(self):
        return self.capacity

    @property
    def get_image(self):
        return self.image