__author__ = 'Vivan'

'''
Classes representing a Uber price estimate and Uber time estimate.
Both inherit from the UberEstimate class.
'''


class UberEstimate(object):

    def __init__(self, product_id, display_name):
        """
        Instantiate a new UberEstimate Object.
        @param product_id: Product ID of the Uber product.
        @param display_name: Display name of the Uber product.
        """

        self.product_id = product_id
        self.display_name = display_name

    @property
    def get_product_id(self):
        return self.product_id

    @property
    def get_display_name(self):
        return self.display_name


class UberPriceEstimate(UberEstimate):

    def __init__(self, product_id, currency_code, display_name, estimate, low_estimate,
                 high_estimate, surge_multiplier, duration, distance):

        """
        Instantiate a new UberPriceEstimate Object.
        @param product_id: Product ID of the Uber product.
        @param currency_code: Currency that is used in the region.
        @param display_name: Display name of the Uber product.
        @param estimate: Estimate combining upper and lower estimate.
        @param low_estimate: Lower bound of estimate.
        @param high_estimate: Upper bound of estimate.
        @param surge_multiplier: Surge multiplier for the estimate.
        @param duration: Time taken for the journey.
        @param distance: Distance of the journey.
        """
        super(UberPriceEstimate, self).__init__(product_id, display_name)

        self.currency_code = currency_code
        self.estimate = estimate
        self.low_estimate = low_estimate
        self.high_estimate = high_estimate
        self.surge_multiplier = surge_multiplier
        self.duration = duration
        self.distance = distance

    @property
    def get_currency_code(self):
        return self.currency_code

    @property
    def get_low_estimate(self):
        return self.low_estimate

    @property
    def get_high_estimate(self):
        return self.high_estimate

    @property
    def get_surge_multiplier(self):
        return self.surge_multiplier

    @property
    def get_duration(self):
        return self.duration

    @property
    def get_distance(self):
        return self.distance


class UberTimeEstimate(UberEstimate):

    def __init__(self, product_id, display_name, estimate):
        """
        Instantiate a new UberTimeEstimate Object.
        @param product_id: Product ID of the Uber product.
        @param display_name: Display name of the Uber product.
        @param estimate: Time estimate (ETA) of the Uber product.
        """
        super(UberTimeEstimate, self).__init__(product_id, display_name)

        self.estimate = estimate

    @property
    def get_estimate(self):
        return self.estimate