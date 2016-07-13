# Read from an input file a list of strings, remove duplicates, sort remaining
# items and then write them back to a different file

from robograph.datamodel.base import graph
from robograph.datamodel.nodes.lib import files, apply


def sort_and_unique(input_file_path, output_file_path):
    file_reader = files.TextFileReader(filepath=input_file_path,
                                       encoding='UTF-8',
                                       name="file_reader")
    to_string_list = apply.Apply(function=lambda c: c.split('\n'),
                                 name="to_string_list")

    def remove_duplicates_from(collection):
        coll_type = type(collection)
        items = set(collection)
        return coll_type(items)

    uniquer = apply.Apply(function=remove_duplicates_from,
                          name='uniquer')
    sorter = apply.Apply(function=lambda unsorted: sorted(unsorted),
                         name="sorter")
    to_string = apply.Apply(function=lambda token_list: '\n'.join(token_list),
                            name='to_string')
    file_writer = files.TextFileWriter(filepath=output_file_path,
                                       encoding='UTF-8',
                                       name='file_writer')

    g = graph.Graph('sort_and_unique', [file_reader, to_string_list, sorter,
                                        uniquer, to_string, file_writer])

    g.connect(file_writer, to_string, 'data')
    g.connect(to_string, sorter, 'argument')
    g.connect(sorter, uniquer, 'argument')
    g.connect(uniquer, to_string_list, 'argument')
    g.connect(to_string_list, file_reader, 'argument')

    return g