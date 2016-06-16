from datamodel.base import node


class Value(node.Node):
    """
    This node returns an arbitrary value that is statically defined
    """

    def __init__(self, value, name=None):
        """
        :param value: any value
        :param name: name of this node
        """
        node.Node.__init__(self, name=name)
        self._value = value

    def output(self):
        return self._value
