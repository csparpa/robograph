import random
import uuid

from robograph.datamodel.base import node


class IntegerRandomizer(node.Node):
    """
    This node gives a random integer from the specified range. Randomization
    has a uniform pdd and range defaults to: [0-10)
    Requirements:
      range_lower --> lower boundary or randomization range
      range_upper --> upper boundary or randomization range
    Eg:
      IntegerRandomizer(range_lower=3, range_upper=45)
    """

    _reqs = ['range_lower', 'range_upper']

    DEFAULT_RANGE_LOWER = 0
    DEFAULT_RANGE_UPPER = 10

    def output(self):
        if self._params['range_lower'] is None:
            lo = self.DEFAULT_RANGE_LOWER
        else:
            lo = self._params['range_lower']
        if self._params['range_upper'] is None:
            hi = self.DEFAULT_RANGE_UPPER
        else:
            hi = self._params['range_upper']
        return random.randint(lo, hi)


class FloatRandomizer(node.Node):
    """
    This node gives a random float from the specified range. Randomization
    has a uniform pdd and range defaults to: [0.0-1.0)
    Requirements:
      range_lower --> lower boundary or randomization range
      range_upper --> upper boundary or randomization range
    Eg:
      FloatRandomizer(range_lower=2.2, range_upper=3.6)
    """

    _reqs = ['range_lower', 'range_upper']

    DEFAULT_RANGE_LOWER = 0.
    DEFAULT_RANGE_UPPER = 1.

    def output(self):
        if self._params['range_lower'] is None:
            lo = self.DEFAULT_RANGE_LOWER
        else:
            lo = self._params['range_lower']
        if self._params['range_upper'] is None:
            hi = self.DEFAULT_RANGE_UPPER
        else:
            hi = self._params['range_upper']
        return random.uniform(lo, hi)


class GaussianRandomizer(node.Node):
    """
    This node gives a random float sampled with a Gaussian pdd of the given
    expected value mu and standard deviation sigma. Mu and sigma default to 0.0
    and 1.0 respectively.
    Requirements:
      mu --> expected value of the Gaussian pdd
      sigma --> standard deviation value of the Gaussian pdd
    Eg:
      GaussianRandomizer(mu=4.7, sigma=8.68)
    """

    _reqs = ['mu', 'sigma']

    DEFAULT_MU = 0.0
    DEFAULT_SIGMA = 1.0

    def output(self):
        if self._params['mu'] is None:
            mu = self.DEFAULT_MU
        else:
            mu = self._params['mu']

        if self._params['sigma'] is None:
            sigma = self.DEFAULT_SIGMA
        else:
            sigma = self._params['sigma']
        return random.gauss(mu, sigma)


class Uuid4Randomizer(node.Node):
    """
    This node gives a random UUID4 value.
    Requirements: none
    Eg:
      Uuid4(mu=4.7, sigma=8.68)
    """

    _reqs = []

    def output(self):
        return uuid.uuid4()
