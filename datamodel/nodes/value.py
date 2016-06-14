from datamodel.lib import node


class Value(node.Node):

    def __init__(self, value, name=None):
        node.Node.__init__(self, name=name)
        self._value = value

    # Lefthand
    def output(self):
        return self._value
