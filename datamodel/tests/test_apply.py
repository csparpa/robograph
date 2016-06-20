from datamodel.nodes import apply


def test_requirements():
    expected = ['function', 'argument']
    instance = apply.Apply()
    assert instance.requirements == expected


def test_input():
    method = lambda x: x+1
    data = 7
    instance = apply.Apply()
    instance.input(dict(function=method, argument=data))
    assert instance.output() == 8


def test_output():
    data = [4, 6, 9]
    instance = apply.Apply(function=sum, argument=data)
    assert instance.output() == 19

