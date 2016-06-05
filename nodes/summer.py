import node


class Summer(node.Node):

    # Righthand
    def input(self, context):
        self._context = context

    # Lefthand
    def output(self):
        return sum(self._context)
