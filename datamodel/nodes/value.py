from datamodel.base import node


class Value(node.Node):
    """
    This node returns an arbitrary value.
    Requirements:
      value --> any Python datatype
    Eg:
      Value(value=dict(number=3))
      Value(value=dict(int_list=[1, 6, 9]))
      Value(value=dict(word1='blabla', word2='bleble'))
    """

    _reqs = ['value', ]

    def output(self):
        return self._params['value']
