# Given a list of numbers, calculate its sum and product and print it on screen

from datamodel.lib import graph
from datamodel.nodes import printer, value, filter

from datamodel.nodes import apply


def sum_and_product(list_of_numbers):
    v = value.Value(list_of_numbers)
    s = apply.Apply(lambda c: sum(c))
    m = apply.Apply(lambda c: reduce(lambda x, y: x * y, c))
    c = filter.InputCombiner()
    p = printer.ConsolePrinter()

    g = graph.Graph('sum_and_product', [v, s, m, c, p])

    g.connect(p, c)
    g.connect(c, m)
    g.connect(c, s)
    g.connect(s, v)
    g.connect(m, v)

    return g