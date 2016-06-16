# Various HTTP calls against HTTPBin

from datamodel.base import graph
from datamodel.nodes import value, printer
from datamodel.nodes.quick import http


def test_get_graph(url, query_params):
    http_params = dict(url=url, query=query_params, output_encoding='json')
    v = value.Value(http_params)
    h = http.Get()
    p = printer.ConsolePrinter()

    g = graph.Graph('test_get_graph', [v, h, p])

    g.connect(p, h)
    g.connect(h, v)

    return g


def test_post_graph(url, post_data):
    http_params = dict(url=url, post_data=post_data, output_encoding='json')
    v = value.Value(http_params)
    h = http.Post()
    p = printer.ConsolePrinter()

    g = graph.Graph('test_post_graph', [v, h, p])

    g.connect(p, h)
    g.connect(h, v)

    return g


def test_put_graph(url, put_data):
    http_params = dict(url=url, post_data=put_data, output_encoding='json')
    v = value.Value(http_params)
    h = http.Put()
    p = printer.ConsolePrinter()

    g = graph.Graph('test_put_graph', [v, h, p])

    g.connect(p, h)
    g.connect(h, v)

    return g


def test_delete_graph(url):
    http_params = dict(url=url, output_encoding='raw')
    v = value.Value(http_params)
    h = http.Delete()
    p = printer.ConsolePrinter()

    g = graph.Graph('test_delete_graph', [v, h, p])

    g.connect(p, h)
    g.connect(h, v)

    return g