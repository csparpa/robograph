from robograph.datamodel.base.exceptions import NodeOutputLabelUndefinedError


class Node:

    """
    A class representing a graph node. Each node has some required parameters
    that can be provided either statically (at node instantiation) or dynamically
    (by invoking the input method). Each node partecipates in the two
    main phases of a graph execution: input and output. The outcome of the
    output method is delegated to subclasses. Each node can be reset - which
    is, you can clean its internal state just as if it was just created.
    """

    _name = None
    _reqs = None
    _params = None
    _output_label = None

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

    @property
    def output_label(self):
        """
        Returns the output label tag for this node's output value
        :return: str
        """
        return self._output_label

    def input(self, context):
        """
        Updates _params with the _reqs entries that are found into context
        :param context: dict
        :return: None
        """
        for key in self._reqs:
            if context.get(key, None):
                self._params[key] = context[key]

    def set_output_label(self, output_label):
        """
        Specifies which tagging label to apply to this node's output value
        :param output_label: str
        :return: None
        """
        self._output_label = output_label

    def output(self):
        """
        Performs the magic! This is supposed to be implemented by subclasses
        :return: a value
        """
        pass

    def execute(self):
        """
        Outputs a dict containing the labeled result of this node execution.
        If the label is not yet defined, raises an exception
        :return: dict
        """
        if self._output_label is None:
            raise NodeOutputLabelUndefinedError()
        return {self._output_label: self.output()}

    def reset(self):
        """
        Resets the node's parameters
        :return:
        """
        for key in self._params:
            self._params[key] = None
        self._output_label = None

    def __repr__(self):
        return '<node: %s instance of: %s requires: %s>' % (
            self._name or '',
            str(self.__class__),
            ','.join(self._reqs) if self._reqs else 'nothing')