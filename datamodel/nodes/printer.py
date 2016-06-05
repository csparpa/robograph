import node


class ConsolePrinter(node.Node):

    # Righthand
    def input(self, context):
        self._context = context

    # Lefthand
    def output(self):
        return self._context
