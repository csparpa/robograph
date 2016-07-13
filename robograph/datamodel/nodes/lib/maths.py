import math

from robograph.datamodel.base.node import Node
from robograph.datamodel.nodes.lib import value, apply


# Constants
class Pi(value.Value):
    """
    This node returns Greek Pi
    """
    def __init__(self, **args):
        value.Value.__init__(
            self,
            value=3.14159265358979323846264338327950288419716939937,
            name=args.get('name', None))


class E(value.Value):
    """
    This node returns Euler Number
    """
    def __init__(self, **args):
        value.Value.__init__(
            self,
            value=2.71828182845904523536028747135266249775724709369,
            name=args.get('name', None))


# Algebraic

class Sum(apply.Apply):
    def __init__(self, **args):
        """
        This node sums the items of the argument sequence
        """
        apply.Apply.__init__(self,
                             function=sum,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Product(apply.Apply):
    """
    This node multiplies the items of the argument sequence
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=lambda c: reduce(lambda x, y: x * y, c),
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Floor(apply.Apply):
    """
    This node rounds the argument value to the next integer
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.floor,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Ceil(apply.Apply):
    """
    This node rounds the argument value to the previous integer
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.ceil,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Sqrt(apply.Apply):
    """
    This node calculates the square root of the argument value
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.sqrt,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


# Extrema

class Max(apply.Apply):
    """
    This node extracts the biggest item in the argument sequence
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=max,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Min(apply.Apply):
    """
    This node extracts the smallest item in the argument sequence
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=min,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


# Trigonometrical

class Sin(apply.Apply):
    """
    This node calculates the sine of the argument value
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.sin,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Cos(apply.Apply):
    """
    This node calculates the cosine of the argument value
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.cos,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Abs(apply.Apply):
    """
    This node calculates the absolute value of the argument value
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.fabs,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


# Exponentations

class Exp(apply.Apply):
    """
    This node raises E to the argument value
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.exp,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Power(Node):
    """
    This node raises a base by an exponent
    Requirements:
      base --> float
      exponent --> float
    Eg:
      Power(base=2., exponent=12.)
      Power(base=-9.32, exponent=2.3)
    """

    _reqs = ['base', 'exponent']

    def output(self):
        return math.pow(self._params['base'], self._params['exponent'])


# Logarithms
class Log(apply.Apply):
    """
    This node calculates the natural logarithm of the argument value
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.log,
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Log10(apply.Apply):
    """
    This node calculates the logarithm of the argument value in base 10
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=math.log10,
                             argument=args.get('argument', None),
                             name=args.get('name', None))
