# Demonstrates how to compose graphs: given graph G that outputs [sum, product]
# create graph H that outputs max([sum, product])

from sum_and_product import sum_and_product
from datamodel.nodes import apply
from datamodel.lib import graph


def graph_concatenation(list_of_numbers):

    # Create graph G
    G = sum_and_product(list_of_numbers)

    # create graph H by appending a new node to G
    m = apply.Apply(lambda ints: max(*ints))
    H = graph.Graph('composite graph', [G, m])
    H.connect(m, G)

    return H

