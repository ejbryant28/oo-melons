"""Classes for melon orders."""

from datetime import datetime
from random import randint

class AbstractMelonOrder(object):
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.set_base_price()


        
    def set_base_price(self):
        """add splurge pricing to base price"""

        #base_price is a random int between 5 and 9
        self.base_price = randint(5, 9)
        now = datetime.now()

        #christmas melons have a higher cost of 1.5 that of other melons
        if self.species == 'christmas melon':
            self.base_price = 1.5 * self.base_price


        #prices during rush hour (weekdays between 8-11) have an added $5 fee
        if now.weekday() < 5 and now.hour < 11 and now.hour >= 8:
            self.base_price += 4


    def get_total(self):
        """calculating total price of order"""

        total = (1 + self.tax) * self.qty * self.base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08  
    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Update get_total to include flat fee of $3 for orders less than 10"""

        total = super().get_total()

        if self.qty < 10:
            total = total + 3

        return total

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the U.S. Governemt, inherits from AbstractMelonOrder"""

    tax = 0
    passed_inspection = False

    def marked_inspection(self, passed):
        """Update the attribute of passed_inspection to be true"""

        self.passed_inspection = passed

