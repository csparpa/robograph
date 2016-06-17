import sys
import os
from datamodel.base import node


class ConsolePrinter(node.Node):
    """
    This node prints on stdout its context and then returns it as output.
    """

    def input(self, context):
        self._context = context

    def output(self):
        try:
            sys.stdout.write(str(self._context))
            sys.stdout.write(os.linesep)
        except:
            pass
        return self._context

    def reset(self):
        del self._context


class LogPrinter(node.Node):
    """
    This node prints its context on a statically defined logger and then
    returns it as output
    """

    def __init__(self, logger, loglevel, stringify=False, name=None):
        """
        :param logger: any logging.Logger subtype
        :param loglevel: the log level
        :param stringify: try to cast to str the context before passing it to
        the logger
        :param name: name of this node
        """
        node.Node.__init__(self, name=name)
        self._logger = logger
        self._loglevel = loglevel
        self._stringify = stringify

    def input(self, context):
        self._context = context

    def output(self):
        str_context = self._context
        if self._stringify:
            try:
                str_context = str(self._context)
            except:
                pass  # oops...
        self._logger.log(self._loglevel, str_context)
        return self._context

    def reset(self):
        del self._context