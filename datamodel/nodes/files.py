import codecs

from datamodel.base import node


class FileReader(node.Node):

    def __init__(self, filepath, encoding='UTF-8', name=None):
        node.Node.__init__(self, name=name)
        self._filepath = filepath
        self._encoding = encoding

    def input(self, context):
        pass

    def output(self):
        with codecs.open(self._filepath, 'r', encoding=self._encoding) as f:
            content = f.read()
        return content


class FileWriter(node.Node):

    def __init__(self, filepath, encoding='UTF-8', name=None):
        node.Node.__init__(self, name=name)
        self._filepath = filepath
        self._encoding = encoding

    def input(self, context):
        self._context = context

    def output(self):
        with codecs.open(self._filepath, 'w', encoding=self._encoding) as f:
            f.write(self._context)

    def reset(self):
        del self._context
