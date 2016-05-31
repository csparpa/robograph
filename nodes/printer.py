import node


class Printer(node.Node):

    # Lefthand
    def obtain(self, value=None):
        def _print(arg):
            print arg
        return _print
