import node


class ApplyStatic(node.Node):

    def __init__(self, function, name=None):
        node.Node.__init__(self, name=name)
        self._function = function

    def input(self, context):
        self._context = context

    def output(self):
        return self._function(self._context)

    def reset(self):
        del self._context


class ApplyDynamic(node.Node):
    def __init__(self, name=None):
        node.Node.__init__(self, name=name)

    def input(self, context):
        if len(context) != 2:
            raise RuntimeError()
        self._data = context[0]
        self._function = context[1]

    def output(self):
        return self._function(self._data)

    def reset(self):
        del self._data
        del self._function