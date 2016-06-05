import node


class Apply(node.Node):

    def __init__(self, function, name=None):
        node.Node.__init__(self, name=name)
        self._function = function

    # Righthand
    def input(self, context):
        self._context = context

    # Lefthand
    def output(self):
        return self._function(self._context)

