import node


class Summer(node.Node):

    # Lefthand
    def obtain(self, value=None):
        return lambda seq: reduce(lambda x, y: x+y, seq)
