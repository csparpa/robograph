import node


class Mapper(node.Node):

    _context = None

    def __init__(self, name=None):
        node.Node.__init__(self, name=name)

    # Lefthand
    def obtain(self, function):
        return map(function, self._context)

    # Righthand
    def inject(self, context):
        self._context = context


class Multimapper(Mapper):

    # Lefthand
    def obtain(self, sequence_of_functions):
        return[f(self._context) for f in sequence_of_functions]

