import json
import os

from robograph.datamodel.base import node


class ToJSON(node.Node):
    """
    This node converts serializable data to JSON
    Requirements:
      data --> data to be dumped to JSON
    Eg:
      ToJSON(data=[1,2,3])
      ToJSON(dict(a="1",b="2"))
    """

    _reqs = ['data']

    def output(self):
        return json.dumps(self._params['data'])


class ToCSV(node.Node):
    """
    This node converts a data matrix to CSV
    Requirements:
      data_matrix --> iterable of lists (csv rows)
      header_list --> header data list (csv header)
      delimiter -->  separator token for row values
      linesep --> newline char
    Eg:
      ToCSV(data_matrix=[[1,2,3],[4,5,6],[7,8,9]],
            header_list=['one','two','three'],
            delimiter=',',
            linesep='\n')
    """

    _reqs = ['data_matrix', 'header_list', 'delimiter', 'linesep']

    def output(self):
        if self._params['delimiter'] is None:
            delim = ','
        else:
            delim = self._params['delimiter']

        if self._params['linesep'] is None:
            eol = os.linesep
        else:
            eol = self._params['linesep']

        lines = eol.join([delim.join(map(str, row)) for row in self._params['data_matrix']])
        if self._params['header_list']:
            header = delim.join(self._params['header_list'])
        else:
            header = ''
        return header + eol + lines
