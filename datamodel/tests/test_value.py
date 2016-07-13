from datamodel.nodes.lib import value


def test_requirements():
    expected = ['value']
    instance = value.Value()
    assert instance.requirements == expected


def test_input():
    expected = '1234'
    instance = value.Value()
    instance.input(dict(value=expected))
    instance.set_output_label('any')
    assert instance.output() == expected


def test_output():
    expected = dict(expected='1234')
    instance = value.Value(value=expected)
    instance.set_output_label('any')
    assert instance.output() == expected
