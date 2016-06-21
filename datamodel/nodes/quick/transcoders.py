import json
import os
from datamodel.base import node


class ToJSON(node.Node):

    def input(self, context):
        self._context = context

    def output(self):
        return json.dumps(self._context)

    def reset(self):
        del self._context


class ToCSV(node.Node):

    def __init__(self, header_list=None, delimiter=',', linesep=os.linesep,
                 name=None):
        node.Node.__init__(self, name=name)
        self._header_list = header_list
        self._delimiter = delimiter
        self._linesep = linesep

    def input(self, data_matrix):
        self._data_matrix = data_matrix

    def output(self):
        lines = self._linesep.join([self._delimiter.join(row) for row in self._data_matrix])
        if self._header_list:
            header = self._delimiter.join(self._header_list)
        else:
            header = ''
        return header + self._linesep + lines

    def reset(self):
        del self._data_matrix