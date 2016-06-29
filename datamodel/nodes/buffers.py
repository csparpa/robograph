from datamodel.base import node


class Buffer(node.Node):
    """
    This node return all its parameters.
    Requirements: none
    Eg:
      Buffer(test1='a', test2=567)
    """

    _reqs = []

    def __init__(self, **args):
        node.Node.__init__(self, name=args.pop('name', None))
        self._params = dict()
        self._params.update(args)

    def input(self, context):
        self._params.update(context)

    def output(self):
        return self._params

    def reset(self):
        self._params = dict()
