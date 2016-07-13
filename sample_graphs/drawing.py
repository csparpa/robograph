from datamodel.base import graph
from datamodel.nodes import plotter
from datamodel.nodes.lib import value, printer, maths, buffers


def plot():
    v1 = value.Value(value=[9, -3, 8.7], name='v1')
    v2 = value.Value(value=[86, -0.43], name='v2')
    s = maths.Sum(name='sum')
    m = maths.Product(name='product')
    b = buffers.Buffer(name='buffer')
    p = printer.ConsolePrinter(name='printer')

    g = graph.Graph('sum_and_product', [v1, v2, s, m, p, b])

    g.connect(p, b, 'message')
    g.connect(b, s, 'sum of v1')
    g.connect(b, m, 'product of v2')
    g.connect(s, v1, 'argument')
    g.connect(m, v2, 'argument')

    plotter.show_plot(g)


def plot_to_file(outputfile):
    v1 = value.Value(value=[9, -3, 8.7], name='v1')
    v2 = value.Value(value=[86, -0.43], name='v2')
    s = maths.Sum(name='sum')
    m = maths.Product(name='product')
    b = buffers.Buffer(name='buffer')
    p = printer.ConsolePrinter(name='printer')

    g = graph.Graph('sum_and_product', [v1, v2, s, m, p, b])

    g.connect(p, b, 'message')
    g.connect(b, s, 'sum of v1')
    g.connect(b, m, 'product of v2')
    g.connect(s, v1, 'argument')
    g.connect(m, v2, 'argument')

    plotter.save_plot(outputfile)