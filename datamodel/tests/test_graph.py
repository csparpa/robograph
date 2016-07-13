import pytest
from datamodel.base import graph, node, exceptions

# Utilities


class Identity(node.Node):
    _reqs = []


class WithParameters(node.Node):
    _reqs = []

    def __init__(self, **args):
        node.Node.__init__(self, **args)
        self._params.update(args)


def make_a_graph_with_isles():
    root = Identity(name='root')
    med1 = Identity(name='med1')
    med2 = Identity(name='med2')
    leaf1 = Identity(name='leaf1')
    leaf2 = Identity(name='leaf2')
    g = graph.Graph('testgraph', [leaf1, med1, med2, leaf2, root])
    g.connect(root, med1, '1')
    g.connect(root, med2, '2')
    g.connect(med1, leaf1, '3')
    return g

# Tests


def test_get_nodes():
    n1 = Identity(name='testnode')
    n2 = Identity(name='testnode')
    instance = graph.Graph('testgraph', [n1, n2])
    nodes = instance.nodes
    assert len(nodes) == 2
    assert n1 in nodes
    assert n2 in nodes


def test_add_node():
    n = Identity(name='testnode')
    instance = graph.Graph('testgraph')
    assert len(instance.nodes) == 0
    instance.add_node(n)
    nodes = instance.nodes
    assert len(nodes) == 1
    assert n in nodes


def test_add_nodes():
    n1 = Identity(name='testnode')
    n2 = Identity(name='testnode')
    instance = graph.Graph('testgraph')
    assert len(instance.nodes) == 0
    instance.add_nodes([n1, n2])
    nodes = instance.nodes
    assert len(nodes) == 2
    assert n1 in nodes
    assert n2 in nodes


def test_root_node():
    root = Identity(name='root')
    leaf1 = Identity(name='leaf1')
    leaf2 = Identity(name='leaf2')
    instance = graph.Graph('testgraph', [leaf1, leaf2, root])
    instance.connect(root, leaf1, 'any1')
    instance.connect(root, leaf2, 'any2')
    result = instance.root_node
    assert result == root


def test_remove_node():
    root = Identity(name='root')
    leaf1 = Identity(name='leaf1')
    leaf2 = Identity(name='leaf2')
    instance = graph.Graph('testgraph', [leaf1, leaf2, root])
    instance.connect(root, leaf1, 'any1')
    instance.connect(root, leaf2, 'any2')
    assert len(instance.nodes) == 3
    instance.remove_node(leaf1)
    nodes = instance.nodes
    assert len(nodes) == 2
    assert root in nodes
    assert leaf2 in nodes
    assert not leaf1 in nodes


def test_remove_nodes():
    root = Identity(name='root')
    leaf1 = Identity(name='leaf1')
    leaf2 = Identity(name='leaf2')
    instance = graph.Graph('testgraph', [leaf1, leaf2, root])
    instance.connect(root, leaf1, 'any1')
    instance.connect(root, leaf2, 'any2')
    assert len(instance.nodes) == 3
    instance.remove_nodes([leaf1, leaf2])
    nodes = instance.nodes
    assert len(nodes) == 1
    assert root in nodes
    assert not leaf1 in nodes
    assert not leaf2 in nodes


def test_len():
    root = Identity(name='root')
    leaf1 = Identity(name='leaf1')
    leaf2 = Identity(name='leaf2')
    instance = graph.Graph('testgraph', [leaf1, leaf2, root])
    assert len(instance) == 3


def test_has_isles():
    root = Identity(name='root')
    med1 = Identity(name='med1')
    med2 = Identity(name='med2')
    leaf1 = Identity(name='leaf1')
    leaf2 = Identity(name='leaf2')
    g = graph.Graph('testgraph', [leaf1, med1, med2, leaf2, root])
    g.connect(root, med1, '1')
    g.connect(root, med2, '2')
    g.connect(med1, leaf1, '3')
    g.connect(med2, leaf2, '4')
    assert not g.has_isles()
    g.remove_node(med2)
    assert g.has_isles()


def test_reset():
    n1 = WithParameters(a=1, b=2)
    n2 = WithParameters(c=1, d=2)
    g = graph.Graph('testgraph', [n1, n2])
    for n in g.nodes:
        for p in n.parameters.values():
            assert p is not None
    g.reset()
    for n in g.nodes:
        for p in n.parameters.values():
            assert p is None


def test_connect():
    n1 = WithParameters(a=1, b=2)
    n2 = WithParameters(c=1, d=2)
    g = graph.Graph('testgraph', [n1, n2])
    not_included = WithParameters(e=1, f=2)

    # Errors when trying to link nodes coming from out of the graph
    with pytest.raises(exceptions.NodeConnectionError):
        g.connect(n1, not_included, 'blabla')
        pytest.fail()
    with pytest.raises(exceptions.NodeConnectionError):
        g.connect(not_included, n2, 'blabla')
        pytest.fail()

    # Now the correct procedure
    assert n2.output_label is None
    assert len(g.nxgraph.edges()) == 0
    g.connect(n1, n2, 'label')
    assert n2.output_label == 'label'
    assert len(g.nxgraph.edges()) == 1


def test_execute_fails_with_graphs_with_isles():
    g = make_a_graph_with_isles()
    with pytest.raises(exceptions.GraphExecutionError):
        g.execute()
        pytest.fail()


def test_get_edges():
    n1 = WithParameters(a=1, b=2)
    n2 = WithParameters(c=1, d=2)
    root = WithParameters(x='x')
    g = graph.Graph('testgraph', [n1, n2, root])
    assert len(g.edges) == 0
    g.connect(root, n1, 'child_1')
    g.connect(root, n2, 'child_2')
    result = g.edges
    assert len(result) == 2
    assert dict(node_from=root, node_to=n1, output_label='child_1') in result
    assert dict(node_from=root, node_to=n2, output_label='child_2') in result
