import random

from datamodel.lib import node


class IntegerRandomizer(node.Node):

    def __init__(self, range_lower=0, range_upper=10,
                 name=None):
        node.Node.__init__(self, name=name)
        self._range_lower = range_lower
        self._range_upper = range_upper

    def input(self, context):
        pass

    def output(self):
        return random.randint(self._range_lower, self._range_upper)


class FloatRandomizer(node.Node):
    def __init__(self, range_lower=0., range_upper=1.,
                 name=None):
        node.Node.__init__(self, name=name)
        self._range_lower = range_lower
        self._range_upper = range_upper

    def input(self, context):
        pass

    def output(self):
        return random.uniform(self._range_lower, self._range_upper)


class GaussianRandomizer(node.Node):
    def __init__(self, mu=0., sigma=1., name=None):
        node.Node.__init__(self, name=name)
        self._mu = mu
        self._sigma = sigma

    def input(self, context):
        pass

    def output(self):
        return random.gauss(self._mu, self._sigma)