class Convert:
    """A family of conversions
    """
    def cups2Gallons(self, cups):
        """Convert cups to gallons
        """
        gallons = cups / 16
        return gallons

import numpy as np
class Add:
    """Tests numpy import requirements
    """
    def add(self, array):
        """Sums an array
        """
        return np.sum(array)