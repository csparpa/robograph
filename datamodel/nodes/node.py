class Node:

    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    def input(self, context):
        pass

    def output(self):
        pass

    def reset(self):
        pass

    def __str__(self):
        return u'<Node: %s - %s>' % (self._name, unicode(self.__class__))
