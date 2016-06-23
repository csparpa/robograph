import codecs
from datamodel.base import node


class File(node.Node):
    """
    Abstract base class for file readers and writers
    Requirements:
      filepath --> path of the file to read/write
    """

    _reqs = ['filepath']


class TextFile(File):
    """
    Abstract base class for text file readers and writers
    Requirements:
      filepath --> path of the file to read/write
      encoding --> how to encode the text read/written
    """

    _reqs = File._reqs + ['encoding']


class TextFileReader(TextFile):
    """
    Reads and return the content of a text file
    """

    def output(self):
        if self._params['encoding'] is None:
            self._params['encoding'] = 'UTF-8'
        with codecs.open(self._params['filepath'], 'r',
                         encoding=self._params['encoding']) as f:
            content = f.read()
        return content


class BinaryFileReader(File):
    """
    Reads and return the content of a binary file
    """

    def output(self):
        with codecs.open(self._params['filepath'], 'rb') as f:
            content = f.read()
        return bytearray(content)


class TextFileWriter(TextFile):
    """
    Writes some text data to a a text file
    Requirements:
      data --> str
    """

    _reqs = TextFile._reqs + ['data']

    def output(self):
        if self._params['encoding'] is None:
            self._params['encoding'] = 'UTF-8'
        with codecs.open(self._params['filepath'], 'w',
                         encoding=self._params['encoding']) as f:
            f.write(self._params['data'])


class BinaryFileWriter(File):
    """
    Writes some binary data (bytearray) to a a binary file
    Requirements:
      data --> str
    """

    _reqs = File._reqs + ['data']

    def output(self):
        try:
            contents = bytearray(self._params['data'])
        except:
            contents = self._params['data']
        with open(self._params['filepath'], "wb") as bf:
            bf.write(contents)

