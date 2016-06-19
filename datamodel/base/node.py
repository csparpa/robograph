class Node:

    _name = None
    _reqs = None
    _params = None

    def __init__(self, **args):
        self._name = args.get('name', None)
        self._params = dict()
        for key in self._reqs:
            self._params[key] = args.get(key, None)

    @property
    def name(self):
        """
        The name of this node
        :return: str
        """
        return self._name

    @property
    def requirements(self):
        """
        Explains the parameters required by this node
        :return: list
        """
        return self._reqs

    @property
    def parameters(self):
        """
        Gives the state of this node in terms of parameters
        :return: dict
        """
        return self._params

    def input(self, context):
        """
        Updates _params with the _reqs entries that are found into context
        :param context: dict
        :return: None
        """
        for key in self._reqs:
            if context.get(key, None):
                self._params[key] = context[key]

    def output(self):
        """
        Performs the magic!
        :return: a value
        """
        pass

    def reset(self):
        """
        Resets the node's parameters
        :return:
        """
        for key in self._params:
            self._params[key] = None

    def __str__(self):
        return u'<Node: %s - requires: %s - class: %s>' % (
            self._name,
            unicode(','.join(self._reqs)),
            unicode(self.__class__))
