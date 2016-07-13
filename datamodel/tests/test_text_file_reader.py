import os

from datamodel.nodes.lib import files

FILEPATH = os.path.abspath('datamodel/tests/file.txt')


def test_requirements():
    expected = ['filepath', 'encoding']
    instance = files.TextFileReader()
    assert instance.requirements == expected


def test_input():
    expected = 'one\ntwo\nthree'
    instance = files.TextFileReader()
    instance.input(dict(filepath=FILEPATH, encoding='UTF-8'))
    instance.set_output_label('any')
    assert instance.output() == expected


def test_output():
    expected = 'one\ntwo\nthree'
    instance = files.TextFileReader(filepath=FILEPATH, encoding='UTF-8')
    instance.set_output_label('any')
    assert instance.output() == expected



