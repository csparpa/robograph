from datamodel.nodes import buffer


def test_requirements():
    expected = []
    instance = buffer.Buffer
    assert instance.requirements == expected


def test_input():
    expected = dict(a=1, b=2, c=3)
    instance = buffer.Buffer()
    instance.input(expected)
    assert instance.output() == expected


def test_output():
    expected = dict(a=1, b=2, c=3)
    instance = buffer.Buffer(**expected)
    assert instance.output() == expected

