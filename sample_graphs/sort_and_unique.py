# Read from an input file a list of strings, remove duplicates, sort remaining
# items and then write them back to a different file

from datamodel.base import graph
from datamodel.nodes import files, apply


def sort_and_unique(input_file_path, output_file_path):
    file_reader = files.FileReader(input_file_path, name="file_reader")
    to_string_list = apply.ApplyStatic(lambda c: c.split('\n'), name="to_string_list")

    def remove_duplicates_from(collection):
        coll_type = type(collection)
        items = set(collection)
        return coll_type(items)

    uniquer = apply.ApplyStatic(remove_duplicates_from, name='uniquer')
    sorter = apply.ApplyStatic(lambda unsorted: sorted(unsorted), name="sorter")
    to_string = apply.ApplyStatic(lambda token_list: '\n'.join(token_list),
                                  name='to_string')
    file_writer = files.FileWriter(output_file_path, name='file_writer')

    g = graph.Graph('sort_and_unique', [file_reader, to_string_list, sorter,
                                        uniquer, to_string, file_writer])

    g.connect(file_writer, to_string)
    g.connect(to_string, sorter)
    g.connect(sorter, uniquer)
    g.connect(uniquer, to_string_list)
    g.connect(to_string_list, file_reader)

    return g