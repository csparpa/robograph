import os

from datamodel.nodes.lib import files

FILEPATH = os.path.abspath('datamodel/tests/outputfile.txt')
EXPECTED_CONTENT = 'a\nb\nc'


def check_output_file():
    with open(FILEPATH, 'r') as of:
        result = of.read()
        assert EXPECTED_CONTENT == result


def test_requirements():
    expected = ['filepath', 'encoding', 'data']
    instance = files.TextFileWriter()
    assert instance.requirements == expected


def test_input():
    instance = files.TextFileWriter()
    instance.input(dict(filepath=FILEPATH, encoding='UTF-8', data=EXPECTED_CONTENT))
    instance.set_output_label('any')
    instance.output()
    check_output_file()


def test_output():
    instance = files.TextFileWriter(filepath=FILEPATH, encoding='UTF-8',
                                    data=EXPECTED_CONTENT)
    instance.set_output_label('any')
    instance.output()
    check_output_file()



