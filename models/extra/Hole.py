from operator import itemgetter

from ..validation.NumberValidator import NumberValidator
from ..Door import Door

class Hole:
    """
    a class to represent a Hole in a Wall object.

    holes[dn] = [[[dp,dp+dw],[0,dh]]]

    Attributes
    ----------
    wall_index: int
        wall index
    hpos: float 
        horizontal position of hole 
    hsize: float 
        horizontal size of hole 
    vpos: float 
        vertical height of hole 
    vsize: float 
        vertical size of hole 
    Door: object
        door object
    """

    wall_index = NumberValidator(minvalue=0, maxvalue=3, additional_msg="Wall index", int_only=True)
    hpos  = NumberValidator()
    hsize = NumberValidator()
    vpos  = NumberValidator()
    vsize = NumberValidator()

    def __init__(self, desc = {}):
        """
        constructs all the necessary attributes for the Hole object.
        
        parameters
        -----------
            desc: dict
                dictionary representing Hole information
        """
        (
        self.hpos,
        self.hsize,
        self.vpos,
        self.vsize,
        self.wall_index,
        ) = itemgetter('hpos',
                       'hsize',
                       'vpos',
                       'vsize',
                       'wall_index',
                       )(desc)
        self.door = None
        if 'door' in desc:
            self.door = Door(desc['door'])
            #perform validdation door size should be smaller
            self.door.wall_index = self.wall_index

    def __str__(self):
        """
        returns string with color object info.
        """
        door_string = ''
        if self.door is not None:
            door_string += '\tHas door:\n'
            door_string += self.door.__str__()

        return(
               '\tWall index: {}\n'
               '\tHorizontal:\n'
               '\t- Position: {:6.2f}\n'
               '\t- Size:     {:6.2f}\n'
               '\tVertical:\n'
               '\t- Position: {:6.2f}\n'
               '\t- Size:     {:6.2f}\n'
               f'{ door_string }'

               .format(
                      self.wall_index,
                      self.hpos,
                      self.hsize,
                      self.vpos,
                      self.vsize,
                      )
               )
