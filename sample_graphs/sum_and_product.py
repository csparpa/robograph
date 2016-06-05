# Given a list of numbers, calculate its sum and product and print it on screen

from lib import graph
from nodes import printer, summer, multiplier, value, filter


def sum_and_product(list_of_numbers):
    v = value.Value(list_of_numbers)
    s = summer.Summer()
    m = multiplier.Multiplier()
    c = filter.InputCombiner()
    p = printer.ConsolePrinter()

    g = graph.Graph('sum_and_product', [v, s, m, c, p])

    g.connect(p, c)
    g.connect(c, m)
    g.connect(c, s)
    g.connect(s, v)
    g.connect(m, v)

    return g