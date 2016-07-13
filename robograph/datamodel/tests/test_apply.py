from robograph.datamodel.nodes.lib import apply


def test_requirements():
    expected = ['function', 'argument']
    instance = apply.Apply()
    assert instance.requirements == expected


def test_input():
    method = lambda x: x+1
    data = 7
    instance = apply.Apply()
    instance.input(dict(function=method, argument=data))
    instance.set_output_label('any')
    assert instance.output() == 8


def test_output():
    data = [4, 6, 9]
    instance = apply.Apply(function=sum, argument=data)
    instance.set_output_label('any')
    assert instance.output() == 19

