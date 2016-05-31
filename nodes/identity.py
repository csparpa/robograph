import node


class Identity(node.Node):

    # Lefthand
    def obtain(self, value=None):
        return lambda x: value

    # Righthand
    def inject(self, context):
        pass
