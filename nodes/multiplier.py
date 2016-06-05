import node


class Multiplier(node.Node):

    # Righthand
    def input(self, context):
        self._context = context

    # Lefthand
    def output(self):
        return reduce(lambda x, y: x*y, self._context)

