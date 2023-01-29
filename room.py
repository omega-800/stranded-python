from bag import Bag
from exceptions import InvalidCommand, InvalidDirection
from copy import deepcopy


class Room:
    """A generic room object that can be used by game code."""

    _directions = {}
    height = 3
    width = 3
    color = ""
    coordinates = {
        frozenset({"x":1,"y":1}.items()):{},
        frozenset({"x":1,"y":2}.items()):{},
        frozenset({"x":1,"y":3}.items()):{},
        frozenset({"x":2,"y":1}.items()):{},
        frozenset({"x":2,"y":2}.items()):{},
        frozenset({"x":2,"y":3}.items()):{},
        frozenset({"x":3,"y":1}.items()):{},
        frozenset({"x":3,"y":2}.items()):{},
        frozenset({"x":3,"y":3}.items()):{}
    }

    @staticmethod
    def add_direction(forward, reverse):
        """Add a direction."""
        for dir in (forward, reverse):
            if not dir.islower():
                raise InvalidCommand(
                    'Invalid direction %r: directions must be all lowercase.'
                )
            if dir in Room._directions:
                raise KeyError('%r is already a direction!' % dir)
        Room._directions[forward] = reverse
        Room._directions[reverse] = forward

        # Set class attributes to None to act as defaults
        setattr(Room, forward, None)
        setattr(Room, reverse, None)

    def __init__(self, description, color):
        self.description = description.strip()
        self.color = color

        # Copy class Bags to instance variables
        for k, v in vars(type(self)).items():
            if isinstance(v, Bag):
                setattr(self, k, deepcopy(v))

    def __str__(self):
        return self.description

    def exit(self, direction):
        """Get the exit of a room in a given direction.

        Return None if the room has no exit in a direction.

        """
        if direction not in self._directions:
            raise KeyError('%r is not a direction' % direction)
        return getattr(self, direction, None)

    def exits(self):
        """Get a list of directions to exit the room."""
        return sorted(d for d in self._directions if getattr(self, d))

    def getrow(self, row, playerCT):
        string=self.color
        w = 1
        while w <= self.width:
            if "x"+str(row)+"y"+str(w) == playerCT:
                string+="|X"
            elif self.coordinates.get(frozenset({"x":row,"y":w})) is not None:
                string+="|item.geticon"
            else:
                string+="|_"
            w+=1
        return string


    def __setattr__(self, name, value):
        if isinstance(value, Room):
            if name not in self._directions:
                raise InvalidDirection(
                    '%r is not a direction you have declared.\n\n' +
                    'Try calling Room.add_direction(%r, <opposite>) ' % name +
                    ' where <opposite> is the return direction.'
                )
            reverse = self._directions[name]
            object.__setattr__(self, name, value)
            object.__setattr__(value, reverse, self)
        else:
            object.__setattr__(self, name, value)


Room.add_direction('north', 'south')
Room.add_direction('east', 'west')

class StoneRoom(Room):
    def display():
        return ""

class SandRoom(Room):
    def display():
        return ""

class DirtRoom(Room):
    def display():
        return ""

class WaterRoom(Room):
    def display():
        return ""

class ShallowwaterRoom(Room):
    def display():
        return ""

class ForestRoom(Room):
    def display():
        return ""

class LavaRoom(Room):
    def display():
        return ""