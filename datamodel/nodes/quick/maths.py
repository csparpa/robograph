import math

from datamodel.lib.node import Node
from ..apply import ApplyStatic
from ..value import Value


# Constants
class Pi(Value):
    def __init__(self, name=None):
        Value.__init__(self, 3.14159265358979323846264338327950288419716939937,
                       name=name)


class E(Value):
    def __init__(self, name=None):
        Value.__init__(self, 2.71828182845904523536028747135266249775724709369,
                       name=name)


# Algebraic

class Sum(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, lambda c: sum(c), name=name)


class Product(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self,
                             lambda c: reduce(lambda x, y: x * y, c),
                             name=name)


class Floor(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.floor, name=name)


class Ceil(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.ceil, name=name)


class Sqrt(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.sqrt, name=name)


# Extrema

class Max(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, max, name=name)


class Min(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, min, name=name)


# Trigonometrical

class Sin(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.sin, name=name)


class Cos(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.cos, name=name)


class Abs(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.fabs, name=name)


# Exponentations

class Exp(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.exp, name=name)


class Power(Node):
    def __init__(self, base, name=None):
        Node.__init__(self, name=name)
        self._base = base

    def input(self, exponent):
        self._exponent = exponent

    def output(self):
        return math.pow(self._base, self._exponent)


# Logs
class Log(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.log, name=name)


class Log10(ApplyStatic):
    def __init__(self, name=None):
        ApplyStatic.__init__(self, math.log10, name=name)

