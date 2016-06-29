from datamodel.base import node


# Functional operators

class Mapper(node.Node):
    """
    This node applies a mapping_function to all items in a sequence and returns
    the resulting collection.
    Requirements:
      mapping_function --> function to be applied to all items in the sequence
      sequence --> the sequence
    Eg:
      Mapper(mapping_function=lambda x: x**2, sequence=[6, 3, 0, 67])
    """

    _reqs = ['mapping_function', 'sequence']

    def output(self):
        return map(self._params['mapping_function'], self._params['sequence'])


class Reducer(node.Node):
    """
    This node applies a reducing_function to all items in a sequence and returns
    the resulting reduced value.
    Requirements:
      reducing_function --> function to be applied to couple of items in the sequence
      sequence --> the sequence
    Eg:
      Reducer(reducing_function=lambda x, y: x*y, sequence=[6, 3, 9, -2])
    """

    _reqs = ['reducing_function', 'sequence']

    def output(self):
        return reduce(self._params['reducing_function'], self._params['sequence'])


class Filter(node.Node):
    """
    This node applies a filtering_function to all items in a sequence and returns
    a sequence containing only the items that respect the input condition.
    Requirements:
      filtering_function --> function to be applied to all sequence items
      sequence --> the sequence
    Eg:
      Filter(filtering_function=lambda x: x % 2 == 0, sequence=[6, 3, 9, -2])
    """

    _reqs = ['filtering_function', 'sequence']

    def output(self):
        return filter(self._params['filtering_function'], self._params['sequence'])


# Sorting

class Sorter(node.Node):
    """
    This node sorts a sequence according to a sorting_function. This function
    defaults to natural sorting provided by the language (eg. alphabetical sorting
    for strings)
    Requirements:
      sorting_function --> function that given items A and B returns 1 if A comes
        before B, 0 if A is comes equal to B and -1 if A comes after B
      sequence --> the sequence to be sorted
    Eg:
      Sorter(sorting_function=f, sequence=[6, 3, 9, -2])
    """

    _reqs = ['sorting_function', 'sequence']

    def output(self):
        if self._params['sorting_function'] is None:
            return sorted(self._params['sequence'])
        return sorted(self._params['sequence'],
                      cmp=self._params['sorting_function'])


class ReverseSorter(Sorter):
    """
    This node sorts a sequence according to a reverse_sorting_function.
    This function defaults to reverse natural sorting provided by the language
    (eg. inverse alphabetical sorting for strings)
    Requirements:
      reverse_sorting_function --> function that given items A and B returns 1 if A comes
        before B, 0 if A is comes equal to B and -1 if A comes after B
      sequence --> the sequence to be sorted reverse
    Eg:
      ReverseSorter(reverse_sorting_function=f, sequence=[6, 3, 9, -2])
    """

    _reqs = ['reverse_sorting_function', 'sequence']

    def output(self):
        if self._params['reverse_sorting_function'] is None:
            return sorted(self._params['sequence'], reverse=True)
        return sorted(self._params['sequence'],
                      cmp=self._params['reverse_sorting_function'])


# Uniqueing

class Uniquer(node.Node):
    """
    This node removes duplicates from a sequence. Order is not preserved.
    Requirements:
      sequence --> the sequence containing duplicates
    Eg:
      Uniquer(sequence=[1, 1, 6, 'x', 0, 'x', 1, 9])
    """

    _reqs = ['sequence']

    def output(self):
        coll_type = type(self._params['sequence'])
        items = set(self._params['sequence'])
        return coll_type(items)
