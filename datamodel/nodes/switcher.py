import node


class If(node.Node):
    def __init__(self, condition_function,
                 true_function, false_function,
                 name=None):
        node.Node.__init__(self, name=name)
        self._condition_function = condition_function
        self._true_function = true_function
        self._false_function = false_function

    def input(self, data):
        self._data = data

    def output(self):
        if self._condition_function(self._data):
            return self._data, self._true_function
        return self._data, self._false_function
