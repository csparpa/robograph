from datamodel.base import node


class ConsolePrinter(node.Node):

    def input(self, context):
        self._context = context

    def output(self):
        print self._context
        return self._context

    def reset(self):
        del self._context