from datamodel.nodes.lib import transcoders

DATA_MATRIX = [[1,2,3],[4,5,6],[7,8,9]]
HEADER = ['one', 'two', 'three']
DELIMITER = ','
LINESEP = '\n'
EXPECTED = 'one,two,three\n1,2,3\n4,5,6\n7,8,9'


def test_requirements():
    expected = ['data_matrix', 'header_list', 'delimiter', 'linesep']
    instance = transcoders.ToCSV()
    assert instance.requirements == expected


def test_input():
    instance = transcoders.ToCSV()
    instance.input(dict(data_matrix=DATA_MATRIX,
                        header_list=HEADER,
                        delimiter=DELIMITER,
                        linesep=LINESEP))
    instance.set_output_label('any')
    assert instance.output() == EXPECTED


def test_output():
    instance = transcoders.ToCSV(data_matrix=DATA_MATRIX,
                                 header_list=HEADER,
                                 delimiter=DELIMITER,
                                 linesep=LINESEP)
    instance.set_output_label('any')
    assert instance.output() == EXPECTED
