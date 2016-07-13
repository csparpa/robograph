# Robograph

## What is Robograph?
Robograph is a *graph-oriented algorithmic engine*.

It is a platform that you can use to describe your algorithms as *computational graphs*.
Once you've defined the graph, you can *execute* that graph as if it was a SW
program and get the expected outputs.

As each algorithm is composed by steps, each graph is composed by *nodes*, each
one being a step of the bigger calculation. Each graph can accept any number of
inputs and give at maximum one output.

You can create your own graphs either by *connecting any of the predefined
basic nodes shipped with Robograph* or by *coding your custom nodes*

Robograph contains basic nodes that:

  - perform mathematical and logical operations
  - read/write local files
  - talk to HTTP APIs
  - log data to console and loggers
  - read/write data from/to databases
  - apply functional operators on data collections
  - dump data to common formats such as JSON
  - send e-mails
  - save data to Amazon S3
  - ...

The list is increasing and is only limited by imagination!


## Why describe algorithms as graphs?
It is a very convenient way of representing computing problems, as it forces
you to approach the solution using a bottom-up approach, requires
very few coding skills and results in a problem modelization that is easily
and automatically runnable.

The main advantages are:
  - if you use basic nodes shipped with Robograph, you don't really need to code: it's just
    a matter of creating nodes and connecting them together!
  - the more the basic nodes in the library, the easier it is to create new graphs
  - each node has a single responsibility, which favours composability and testability
  - you can save your graphs and run them whenever you want
  - you can plot your algorithms once you've created the graphs
  - ... and you can actually also visually draw the graphs themselves using GUIs
    on the top of Robograph.

Of course using graphs to model problems also poses [a few limitations](https://github.com/csparpa/robograph/blob/master/docs/graph-abstraction.md), above all
the fact that we can only represent synchronous coding tasks with it.


## Why should I use this instead of implementing my algorithms in code?
Because graphs can be understood and managed also by people that don't have
coding skills. And also because you can benefit from the basic nodes library.
Moreover, single nodes and subgraphs can be reused over different algorithms
without the need to change them. And finally, because it's fun!

## Installing Robograph

As simple as:

    sudo pip install robograph


## Graph examples
There are lots of graph samples in the `sample_graphs` folders: each module over
there is a graph factory that you can use to instantiate a graph. Eg:

```python
from sample_graphs import sum_and_product
graph = sum_and_product.sum_and_product([3, 4, 5])
output = graph.execute()  # {'sum value': 12, 'product value': 60}
```

## Let's build a graph
What if you want to build your own graph? Say that you want to accomplish this
task: you want to save an online image to a local file.

Creating a graph is easy:

  1. define the *inputs for the calculation, each one being a leaf node in the
     graph*. In our case, the URL of the remote image and the file system path of
     the target file are both inputs, so we'll create 2 nodes.
  2. create as many higher level nodes as you want. Remember: each node accepts
     *multiple labeled input values* and returns only one output value or none.
     In our case, the only intermediate node will be an HTTP client that will
     fetch the image data.
  3. define the root node of the graph, that will perform the very last operation
     and give an - optional - output. In our case, the output is not a value
     returned in code but will be the writing of image data to the target file.

Let's do it:

```python
from datamodel.base import graph
from datamodel.nodes.lib import files, value, http

# Create the leaf nodes
url = value.Value(value='http://httpbin.org/image/png', name='url')
filepath = value.Value(value='/tmp/target.png', name='filepath')

# Create the intermediate node
http_client = http.Get(mime_type='image/png', name='http_client')

# Create the root node
file_writer = files.BinaryFileWriter(filepath=filepaht, name='file_writer')

# Create an empty graph
g = graph.Graph('my_graph')

# Add all nodes, that still are unconnected
g.add_nodes([url, filepath, http_client, file_writer])

# Connect nodes
# first, tell the http_client node the URL to GET..
g.connect(client, url, 'url')

# ..then tell the file_writer what is the target file path..
g.connect(file_writer, filepath, 'filepath')

# ..then tell the file_writer to write the output of http_client to the target file
g.connect(file_writer, client, 'data')

# You're ready to run the graph and admire /tmp/target.png !
g.execute()
```

Did you notice? All connections must have a *label*.
Say we make this connection:

```python
g.connect(B, A, 'xyz')
```
it means that we connect node B to node A, and the output of node A will be
injected as input for node B with the label `xyz`

This is because data flow from the "outer" (leaf) nodes of the graph towards
its root node, which gives the overall output of the computation.


## Drawing graphs
You can visualize your graphs very easily:

```python
from datamodel.nodes.lib import plotter

# g is your graph
plotter.show_plot(g)               # show it
plotter.save_plot(g, 'graph.png')  # save it to file 'graph.png'
```

## Writing your custom nodes
Extending Robograph and creating new custom nodes is easy: you only need to
subclass the `datamodel.base.node.Node` class and comply with its contract.

[Full details in the docs](https://github.com/csparpa/robograph/blob/master/docs/creating-custom-nodes.md)

Enough to say that each node must expose a list of *requirements* (the named
inputs that we need in order to execute the node) and you must write what
actually the node does with its inputs: that code you need to put into the
`output` function.


## Contributing/testing

**Contributions are welcome!**

In order to get started, please install also the development dependencies with:

    sudo pip install -r dev-requirements.txt

The unit tests suite leverages `py.test` and can be run with:

    bash runtests.sh

