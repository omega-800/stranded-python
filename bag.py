import random
class Bag(set):
    """A collection of Items, such as in an inventory.

    Behaves very much like a set, but the 'in' operation is overloaded to
    accept a str item name, and there is a ``take()`` method to remove an item
    by name.

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._alias_dict = {}
        for item in self:
            self._add_aliases(item)

    #######
    # Convenience functions to update internal alias dict.
    ####### 
    def _add_aliases(self, item):
        """Updates"""
        for alias in item.aliases:
            self._alias_dict.setdefault(alias.lower(), set()).add(item)

    def _discard_aliases(self, item):
        for alias in item.aliases:
            item_set = self._alias_dict.get(alias.lower(), set())
            item_set.discard(item)

            # Avoids memory leaks when many items are added/removed.
            if not item_set and alias in self._alias_dict:
                del self._alias_dict[alias]

    ####### 
    # Implementations of base set interface.
    ####### 
    def add(self, item):
        super().add(item)
        self._add_aliases(item)

    def clear(self):
        super().clear()
        self._alias_dict.clear()

    def copy(self):
        result = super().copy()
        result._alias_dict = self._alias_dict.copy()
        return result

    def difference(self, other_bag):
        return Bag(super().difference(other_bag))

    def difference_update(self, other_bag):
        for element in other_bag:
            self.discard(element)

    def discard(self, item):
        super().discard(item)
        self._discard_aliases(item)

    def intersection(self, other_bag):
        return Bag(super().intersection(other_bag))

    def intersection_update(self, other_bag):
        for element in other_bag:
            self.add(element)

    def pop(self):
        result = super().pop()
        self._discard_aliases(result)
        return result

    def remove(self, item):
        super().remove(item)
        self._discard_aliases(item)

    def symmetric_difference(self, other_bag):
        return Bag(super().symmetric_difference(other_bag))

    def symmetric_difference_update(self, other_bag):
        diff = super().symmetric_difference(other_bag)
        for element in self:
            if element not in diff:
                self.remove(element)
        for element in diff:
            if element not in self:
                self.add(element)

    def union(self, other_bag):
        return Bag(super().union(other_bag))

    def update(self, elements):
        for element in elements:
            self.add(element)

    ####### 
    # Bag interface.
    ####### 
    def find(self, name):
        """Find an object in the bag by name, but do not remove it.

        Return None if the name does not match.
        
        If more than one object with the same name exists, returns one of them.

        """
        name = name.lower()
        for element in self._alias_dict.get(name, []):
            return element

    def __contains__(self, v):
        """Return True if an Item is present in the bag.

        If v is a str, then find the item by name, otherwise find the item by
        identity.

        """
        if isinstance(v, str):
            return bool(self.find(v))
        else:
            return super().__contains__(v)

    def take(self, name):
        """Remove an Item from the bag if it is present.

        If multiple names match, then return one of them.

        Return None if no item matches the name.

        """
        obj = self.find(name)
        if obj is not None:
            self.remove(obj)
        return obj

    def get_random(self):
        """Choose an Item from the bag at random, but don't remove it.

        Return None if the bag is empty.

        """
        if not self:
            return None
        which = random.randrange(len(self))
        for index, obj in enumerate(self):
            if index == which:
                return obj

    def take_random(self):
        """Remove an Item from the bag at random, and return it.

        Return None if the bag is empty.

        """
        obj = self.get_random()
        if obj is not None:
            self.remove(obj)
        return obj

