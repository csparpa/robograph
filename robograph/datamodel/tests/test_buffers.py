import time

from robograph.datamodel.nodes.lib import buffers


def test_buffer():
    instance = buffers.Buffer()
    assert instance.requirements == []
    expected = dict(a=1, b=2, c=3)
    instance.input(expected)
    instance.set_output_label('any')
    assert instance.output() == expected


def test_detlayed_buffer():
    delay = 2.5
    instance = buffers.DelayedBuffer(seconds=delay)
    assert instance.requirements == ['seconds']
    expected = dict(a=1, b=2, c=3)
    instance.input(expected)
    instance.set_output_label('any')
    start_time = time.time()
    result = instance.output()
    end_time = time.time()
    assert result == expected
    assert end_time - start_time >= delay
