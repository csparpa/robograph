from robograph.datamodel.nodes.lib import transcoders

DATA = dict(x=[1, 2, 3])
EXPECTED = '{"x": [1, 2, 3]}'


def test_requirements():
    expected = ['data']
    instance = transcoders.ToJSON()
    assert instance.requirements == expected


def test_input():
    instance = transcoders.ToJSON()
    instance.input(dict(data=DATA))
    instance.set_output_label('any')
    assert instance.output() == EXPECTED


def test_output():
    instance = transcoders.ToJSON(data=DATA)
    instance.set_output_label('any')
    assert instance.output() == EXPECTED
