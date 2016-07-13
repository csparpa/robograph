import time
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


class DelayedBuffer(Buffer):
    """
    This node freezes for the specified amount of seconds and then returns
    the rest of its parameters
    Requirements:
      seconds --> how many seconds to stay frozen
    Eg:
      Delayer(seconds=10, test1=1, test2=2)
    """
    _reqs = Buffer._reqs + ['seconds']

    def output(self):
        delay = self._params.pop('seconds', 0)
        time.sleep(delay)
        return self._params
