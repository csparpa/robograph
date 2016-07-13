import os
import sys

from robograph.datamodel.base import node


class ConsolePrinter(node.Node):
    """
    This node prints on stdout its context and then returns it as output.
    Requirements:
      message --> anything that can be printed on stodut
    Eg:
      ConsolePrinter(message=[1,2,3])
      ConsolePrinter(message="hello world")
    """

    _reqs = ['message']

    def output(self):
        try:
            sys.stdout.write(str(self._params['message']))
            sys.stdout.write(os.linesep)
        except:
            pass
        return self._params['message']


class LogPrinter(node.Node):
    """
    This node writes its required message on a logger and then returns the message.
    The message will be lgoged at the specified loglevel
    Requirements:
      message --> anything that can be logged
      logger --> a logging.logger
      loglevel --> int (eg. logging.ERROR, logging.DEBUG, etc)
      stringify --> bool
    Eg:
      ConsolePrinter(message=[1,2,3])
      ConsolePrinter(message="hello world")
    """

    _reqs = ['message', 'logger', 'loglevel']

    def output(self):
        self._params['logger'].log(self._params['loglevel'],
                                   self._params['message'])
        return self._params['message']
