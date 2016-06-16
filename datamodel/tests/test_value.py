from datamodel.nodes import value


def test_output():
    expected = '1234'
    instance = value.Value(expected)
    instance.input('any')
    assert instance.output() == expected