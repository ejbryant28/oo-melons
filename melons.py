"""Classes for melon orders."""

class AbstractMelonOrder(object):
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 5

        if self.species == 'christmas melon':
            self.base_price = 1.5 * self.base_price


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

