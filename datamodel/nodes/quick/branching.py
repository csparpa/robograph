from datamodel.base import node
from datamodel.nodes import switcher, apply


class If(switcher.Switcher):
    def __init__(self, condition_function,
                 true_function, false_function,
                 name=None):
        node.Node.__init__(self, name=name)
        self._condition_function = condition_function
        self._true_function = true_function
        self._false_function = false_function

    def output(self):
        a = apply.ApplyDynamic()
        if self._condition_function(self._data):
            a.input([self._data, self._true_function])
        else:
            a.input([self._data, self._false_function])
        return a.output()

    def reset(self):
        del self._data
