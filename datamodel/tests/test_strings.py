from datamodel.nodes.lib import strings


def test_templated_string():
    expected_requirements = ['template', 'parameters']
    expected_output = 'After 1 comes 2 but then there is three'
    instance = strings.TemplatedString(
        template='After {p1} comes {p2} but then there is {p3}')
    instance.input(dict(parameters=dict(p1=1, p2=2, p3='three')))
    assert instance.requirements == expected_requirements
    assert instance.output() == expected_output