from operator import itemgetter

from ..validation.NumberValidator import NumberValidator

class Color:
    """
    a class to represent a color.

    attributes
    ----------
    r: float 
        number representig red value
    g: float 
        number representig red value
    b: float 
        number representig red value
    alpha: float 
        number representig red value
    """

    r =     NumberValidator()
    g =     NumberValidator()
    b =     NumberValidator()
    alpha = NumberValidator()

    def __init__(self, desc = {}):
        """
        Constructs all the necessary attributes for the color object.
        
        Parameters
        -----------
            desc: dict
                dictionary representing light source information
        """
        (
        self.r,
        self.g,
        self.b,
        ) = itemgetter('r',
                       'g',
                       'b',
                       )(desc)
        if 'alpha' in desc:
            self.alpha = itemgetter('alpha')(desc)
        else: 
            self.alpha = 0

    def __str__(self):
        """
        returns string with color object info.
        """
        return(
               '\tColor:\n'
               '\tR:        {:6.2f}\n'
               '\tG:        {:6.2f}\n'
               '\tB:        {:6.2f}\n'
               '\tAlpha:     {:6.2f}\n'
               .format(
                      self.r,
                      self.g,
                      self.b,
                      self.alpha,
                      )
               )
