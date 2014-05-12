from collection import Item
from tool import *

class Marker(object):
    def __init__(self, direction, args):
        self.direction = direction
        self.args = args

    def __eq__(self, other):
        if not isinstance(other, Marker):
            return False
        if self.args == other.args and self.direction == other.direction:
            return True
        return False



