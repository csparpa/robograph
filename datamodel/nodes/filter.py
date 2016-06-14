from datamodel.base import node


class InputCombiner(node.Node):

    _inputs = list()

    def input(self, input):
        self._inputs.append(input)

    def output(self):
        return self._inputs

    def reset(self):
        self._inputs = list()


class InputFilter(node.Node):

    def input(self, discard, **inputs):
        self._discard = discard
        self._inputs = inputs

    def output(self):
        if self._discard is None:
            return self._inputs
        for name in self._discard:
            self._inputs.pop(name, None)
        return self._inputs

    def reset(self):
        del self._discard
        del self._inputs