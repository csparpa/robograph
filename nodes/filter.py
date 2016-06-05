import node


class InputCombiner(node.Node):

    _inputs = list()

    # Righthand
    def input(self, input):
        self._inputs.append(input)

    # Lefthand
    def output(self):
        return self._inputs


class InputFilter(node.Node):

    # Righthand
    def input(self, discard, **inputs):
        self._discard = discard
        self._inputs = inputs

    # Lefthand
    def output(self):
        if self._discard is None:
            return self._inputs
        for name in self._discard:
            self._inputs.pop(name, None)
        return self._inputs
