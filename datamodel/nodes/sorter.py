import node


class Sorter(node.Node):

    def __init__(self, sorting_function=None, name=None):
        node.Node.__init__(self, name=name)
        self._sorting_function = sorting_function

    # Righthand
    def input(self, unsorted):
        self._context = unsorted

    # Lefthand
    def output(self):
        if self._sorting_function is None:
            return sorted(self._context)
        return self._sorting_function(self._context)

    def reset(self):
        del self._context


class ReverseSorter(Sorter):

    # Lefthand
    def output(self):
        if self._sorting_function is None:
            return sorted(self._context, reverse=True)
        return self._sorting_function(self._context)

