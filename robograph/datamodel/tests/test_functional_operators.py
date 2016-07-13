from robograph.datamodel.nodes.lib import functional_operators as fo


def sorting_function(x, y):
    if x['a'] > y['a']:
        return 1
    elif x['a'] < y['a']:
        return -1
    else:
        return 0


def reverse_sorting_function(x, y):
    if x['a'] > y['a']:
        return -1
    elif x['a'] < y['a']:
        return 1
    else:
        return 0


def test_mapper():
    seq = [1, 2, 3, 4]
    expected_seq = [1, 4, 9, 16]
    expected_reqs = ['mapping_function', 'sequence']
    instance = fo.Mapper()
    assert instance.requirements == expected_reqs
    instance.input(dict(mapping_function=lambda x: x**2, sequence=seq))
    instance.set_output_label('any')
    assert instance.output() == expected_seq


def test_reducer():
    seq = [1, 2, 3, 4]
    expected_result = -24
    expected_reqs = ['reducing_function', 'sequence']
    instance = fo.Reducer()
    assert instance.requirements == expected_reqs
    instance.input(dict(reducing_function=lambda x, y: -x*y, sequence=seq))
    instance.set_output_label('any')
    assert instance.output() == expected_result


def test_filter():
    seq = [1, 2, 3, 4]
    expected_seq = [2, 4]
    expected_reqs = ['filtering_function', 'sequence']
    instance = fo.Filter()
    assert instance.requirements == expected_reqs
    instance.input(dict(filtering_function=lambda x: x % 2 == 0, sequence=seq))
    instance.set_output_label('any')
    assert instance.output() == expected_seq


def test_sorter():
    d1 = dict(a=7, b=9)
    d2 = dict(a=0, b=5)
    d3 = dict(a=2, b=15)
    seq = [d1, d2, d3]
    expected_seq = [d2, d3, d1]
    expected_reqs = ['sorting_function', 'sequence']
    instance = fo.Sorter()
    assert instance.requirements == expected_reqs
    instance.input(dict(sorting_function=sorting_function, sequence=seq))
    instance.set_output_label('any')
    assert instance.output() == expected_seq


def test_reverse_sorter():
    d1 = dict(a=7, b=9)
    d2 = dict(a=0, b=5)
    d3 = dict(a=2, b=15)
    seq = [d1, d2, d3]
    expected_seq = [d1, d3, d2]
    expected_reqs = ['reverse_sorting_function', 'sequence']
    instance = fo.ReverseSorter()
    assert instance.requirements == expected_reqs
    instance.input(dict(reverse_sorting_function=reverse_sorting_function,
                        sequence=seq))
    instance.set_output_label('any')
    assert instance.output() == expected_seq


def test_uniquer():
    seq = [1, 1, 6, 'x', 'x', 1, 9]
    expected_reqs = ['sequence']
    instance = fo.Uniquer()
    assert instance.requirements == expected_reqs
    instance.input(dict(sequence=seq))
    instance.set_output_label('any')
    output = instance.output()
    assert 1 in output
    assert 6 in output
    assert 'x' in output
    assert 9 in output
