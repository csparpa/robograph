from datamodel.nodes import apply
from datamodel.base import node


# Functional operators

class Mapper(node.Node):

    def __init__(self, mapping_function, name=None):
        node.Node.__init__(self, name=name)
        self._mapping_function = mapping_function

    def input(self, iterable):
        self._iterable = iterable

    def output(self):
        return map(self._mapping_function, self._iterable)

    def reset(self):
        del self._iterable


class Reducer(node.Node):

    def __init__(self, reducing_function, name=None):
        node.Node.__init__(self, name=name)
        self._reducing_function = reducing_function

    def input(self, iterable):
        self._iterable = iterable

    def output(self):
        return reduce(self._reducing_function, self._iterable)

    def reset(self):
        del self._iterable


class Filter(node.Node):

    def __init__(self, filtering_function, name=None):
        node.Node.__init__(self, name=name)
        self._filtering_function = filtering_function

    def input(self, iterable):
        self._iterable = iterable

    def output(self):
        return filter(self._filtering_function, self._iterable)

    def reset(self):
        del self._iterable


# Sorting

class Sorter(node.Node):

    def __init__(self, sorting_function=None, name=None):
        node.Node.__init__(self, name=name)
        self._sorting_function = sorting_function

    def input(self, unsorted):
        self._context = unsorted

    def output(self):
        if self._sorting_function is None:
            return sorted(self._context)
        return self._sorting_function(self._context)

    def reset(self):
        del self._context


class ReverseSorter(Sorter):

    def output(self):
        if self._sorting_function is None:
            return sorted(self._context, reverse=True)
        return self._sorting_function(self._context)


# Uniqueing

class Uniquer(node.Node):

    def input(self, dataset):
        self._dataset = dataset

    def output(self):
        coll_type = type(self._dataset)
        items = set(self._dataset)
        return coll_type(items)

    def reset(self):
        del self._dataset
