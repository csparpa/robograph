from lib import graph
from nodes import mapper, summer, multiplier, printer

a = mapper.Multimapper('A')
b = summer.Summer('B')
c = multiplier.Multiplier('C')
d = printer.Printer('D')

g = graph.Graph('example', [a, b, c, d])

g.connect(a, b, name='sum')
g.connect(a, c, name='multiplication')
g.connect(a, d, name='printing')
g.set_root_node(a)

input_list = [1, 2, 3, 4, 5]
output = g.execute(input_list)
print 'Output: %s' % (output,)



