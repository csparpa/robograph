from datamodel.nodes import buffers


def test_buffer():
    instance = buffers.Buffer()
    assert instance.requirements == []
    expected = dict(a=1, b=2, c=3)
    instance.input(expected)
    instance.set_output_label('any')
    assert instance.output() == expected


