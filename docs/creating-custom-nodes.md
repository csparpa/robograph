# How to create custom nodes

## TL;DR
Extending Robograph and creating new custom nodes is easy: you only need to
subclass the `robograph.datamodel.base.node.Node` class and comply with its contract.

The contract is simple: *just state what the required parameters for your custom
node are and provide an implementation for the `output()` method*

## A quick example
Say you want to implement a custom node that joins a string A to a string B.
The inputs for the node would be, eg:

```
a = 'hello'
b = 'world'
```

and the expected output in this case would be the string: `helloworld`

Your custom node will then require 2 parameters: the input strings.
You can name those parameters as you like: only, keep in mind that you will need
to use these labels when you will link your custom node instances to other nodes
in graph edges (more on that below)

The actual joining of the strings will be performed in the `output()` method
and will return the output string.

The full implementation of your custom node would simply be:

```python
from robograph.datamodel.base import node

class MyCustomNode(node.Node):

    _reqs = ['string_a', 'string_b']

    def output(self):
        return string_a + string_b
```

and you can now create graphs that use the node:

```python

from robograph.datamodel.base import graph
from robograph.datamodel.nodes.lib import value
# <import your node here>

first_input = value.Value(value='hello')
second_input = value.Value(value='world')
custom_node = MyCustomNode()

g = graph.Graph('my_graph', [first_input, second_input, custom_node])

# here you must use the label you set for the first input of the custom node
g.connect(custom_node, first_input, 'string_a')

# here you must use the label you set for the second input of the custom node
g.connect(custom_node, second_input, 'string_b')

print g.execute()
```

## How this works in details

### Node requirements
Each states a *list of required parameters* (stored in the `_reqs` list)
that are needed in order to obtain output from the node.

These parameters can be provided:

  - *statically*, that is: by instantiating the node passing the parameters as
    kwargs
  - *dynamically*, that is: by invoking the `input()` method by passing a `dict`
    containing the parameter key/value pairs

Therefore in our custom node example, these two cases:
```python
# case A
node = MyCustomNode(string_a='hello', string_b='world')

# case B
node = MyCustomNode()
node.input({'string_a': 'hello', 'string_b': 'world'})
```
have the same effect: they both create a node with valorized required parameters.

### Node output and node connections
Each node has at most one output, and that value comes from the `output()` method.

When your node is part of a graph, you need to give it an *output_label*: that
is the name associated to the output value. This will be used when connecting
your node to another node, as the output of your node will be injected as
input value into the end node with the label that you specified as `output_label`
Eg:

```python
g.connect(custom_node, second_input, 'string_b')
```

this tells Robograph to take the output of the node `second_input`, give it
the name `string_b` and pass it as an input to the node `custom_node`.

Of course we are expecting that node `custom_node` accepts the parameter
`string_b`: if during graph execution this promise is not fulfilled, then an
exception is raised

*Watch out*: as you may have noticed when connecting nodes, the "direction of
data flow" is the opposite of the order of declarations of the nodes!


### Node execution
When a graph is executed containing the node, the `input()` method is called by
passing in values bound to the node's required parameters, and those values
are outputs of the nodes that connect to our node.
