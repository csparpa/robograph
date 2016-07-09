from datamodel.nodes import serializer
from datamodel.base import graph
from datamodel.nodes.lib import apply, value, buffers


def test_node_serializer():
    instance = apply.Apply(function=lambda x: x+2, argument=3, name='test')
    serialized = serializer.NodeSerializer.serialize(instance)
    deserialized = serializer.NodeSerializer.deserialize(serialized)
    assert instance.name == deserialized.name
    assert instance.output_label == deserialized.output_label
    assert instance.output() == deserialized.output()


def test_graph_serializer():
    a = value.Value(value=1, name='val_a')
    b = value.Value(value=2, name='val_b')
    s = buffers.Buffer(name='buffer')
    g = graph.Graph('test', [a, b, s])
    g.connect(s, a, 'val_a')
    g.connect(s, b, 'val_b')
    serialized = serializer.GraphSerializer.serialize(g)
    deserialized = serializer.GraphSerializer.deserialize(serialized)
    assert g.name == deserialized.name
    assert g.nxgraph == g.nxgraph


