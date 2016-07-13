# Given a list of numbers, calculate its sum and product and print it on screen

import logging

from datamodel.base import graph
from datamodel.nodes.lib import apply, printer, value, buffers


def sum_and_product(list_of_numbers):
    v = value.Value(value=list_of_numbers)
    s = apply.Apply(function=sum)
    m = apply.Apply(function=lambda c: reduce(lambda x, y: x * y, c))
    b = buffers.Buffer()
    p = printer.ConsolePrinter()

    g = graph.Graph('sum_and_product', [v, s, m, p, b])

    g.connect(p, b, 'message')
    g.connect(b, s, 'sum value')
    g.connect(b, m, 'product value')
    g.connect(s, v, 'argument')
    g.connect(m, v, 'argument')

    return g


def logged_sum_and_product(list_of_numbers):
    v = value.Value(value=list_of_numbers)
    s = apply.Apply(function=sum)
    m = apply.Apply(function=lambda c: reduce(lambda x, y: x * y, c))
    b = buffers.Buffer()

    logging.basicConfig(level=logging.ERROR)
    p = printer.LogPrinter(logger=logging.getLogger(__name__),
                           loglevel=logging.ERROR)

    g = graph.Graph('logged_sum_and_product', [v, s, m, b, p])

    g.connect(p, b, 'message')
    g.connect(b, s, 'sum value')
    g.connect(b, m, 'product value')
    g.connect(s, v, 'argument')
    g.connect(m, v, 'argument')

    return g