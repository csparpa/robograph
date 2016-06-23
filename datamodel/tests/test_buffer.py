from datamodel.nodes import buffer


def test_requirements():
    expected = []
    instance = buffer.Buffer()
    assert instance.requirements == expected


def test_input():
    expected = dict(a=1, b=2, c=3)
    instance = buffer.Buffer()
    instance.input(expected)
    instance.set_output_label('any')
    assert instance.output() == expected


def test_output():
    expected = dict(a=1, b=2, c=3)
    instance = buffer.Buffer(**expected)
    instance.set_output_label('any')
    assert instance.output() == expected

