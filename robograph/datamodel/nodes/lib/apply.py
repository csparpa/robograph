from robograph.datamodel.base import node


class Apply(node.Node):

    """
    This node executes an arbitrary function on a given argument
    Requirements:
      function --> function to be executed
      argument --> argument for the function
    Eg:
      Apply(function=lambda x: x+1, argument=8)
      Apply(function=sum, argument=[8, 13, 6])
    """

    _reqs = ['function', 'argument']

    def output(self):
        return self._params['function'](self._params['argument'])
