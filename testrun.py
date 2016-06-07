from sample_graphs import sum_and_product, sort_and_unique

g = sum_and_product.sum_and_product([1, 2, 3, 4])
output = g.execute()


h = sort_and_unique.sort_and_unique('sample_graphs/testinput.txt',
                                    'sample_graphs/testoutput.txt')
h.execute()
