import codecs

from datamodel.base import node


class FileReader(node.Node):

    def __init__(self, filepath, name=None):
        node.Node.__init__(self, name=name)
        self._filepath = filepath

    def input(self, context):
        pass

    def output(self):
        pass


class TextFileReader(FileReader):

    def __init__(self, filepath, encoding='UTF-8', name=None):
        FileReader.__init__(self, filepath, name=name)
        self._encoding = encoding

    def output(self):
        with codecs.open(self._filepath, 'r', encoding=self._encoding) as f:
            content = f.read()
        return content


class BinaryFileReader(FileReader):

    def output(self):
        with codecs.open(self._filepath, 'rb') as f:
            content = f.read()
        return bytearray(content)


class FileWriter(node.Node):

    def __init__(self, filepath, name=None):
        node.Node.__init__(self, name=name)
        self._filepath = filepath

    def input(self, file_content):
        self._file_content = file_content

    def output(self):
        pass

    def reset(self):
        del self._file_content


class TextFileWriter(FileWriter):

    def __init__(self, filepath, encoding='UTF-8', name=None):
        FileWriter.__init__(self, filepath, name=name)
        self._encoding = encoding

    def output(self):
        with codecs.open(self._filepath, 'w', encoding=self._encoding) as f:
            f.write(self._file_content)


class BinaryFileWriter(FileWriter):

    def output(self):
        with open(self._filepath, "wb") as bf:
            bf.write(bytearray(self._file_content))
