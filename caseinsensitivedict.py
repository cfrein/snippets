from collections import OrderedDict

class CaseInsensitiveDict(OrderedDict):
    """Convert all keys to lower
    """
    def __setitem__ (self, key, value):
        # pylint: disable=W0221
        OrderedDict.__setitem__(self, key.lower(), value)

    def __getitem__ (self, key):
        return OrderedDict.__getitem__(self, key.lower())

    def get (self, key, default=None):
        # pylint: disable=W0613
        return OrderedDict.get(self, key.lower())

    def has_key (self, key):
        return OrderedDict.has_key(self, key.lower())

