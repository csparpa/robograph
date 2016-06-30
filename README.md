# Robograph

## What is Robograph?
Robograph is a *graph-oriented algorithmic engine*.

It is a platform where you can programmatically describe your calculations as
*computational graphs* - each algorithmic step being *a node* of a graph: once
you've defined all the inputs for a graph, then you can *execute* that graph as
if it was a SW black-box and get the expected outputs.

You can create your own graphs either *by connecting any of the predefined
*basic nodes* shipped with Robograph* or by *extending the library and
coding your custome nodes*

The Robograph node library contains nodes that:

  - perform mathematical and logical operations
  - read/write local files
  - talk to HTTP APIs
  - log data to console and loggers
  - read/write data from/to databases
  - apply functional operators on data collections
  - dump data to common formats such as JSON
  - send e-mails
  - ...

The list is only limited by imagination... The more basic nodes, the less the
need to code custom ones.


## Why describe algorithms as graphs?
It is a very convenient way of representing computing problems, as it forces
you to approach the solution using a modular bottom-up approach and requires
very few coding skills.

The main advantages are:
  - if you use basic nodes shipped with Robograph, you don't really need to code: it's just
    a matter of creating and connecting nodes together!
  - each node has a single responsibility, which favours composability and testability
  - you can save your graphs and run them whenever you want
  - you can actually plot your algorithms once you've created the graphs!
  - ... and you can actually also visually draw the graphs themselves using GUIs
    on the top of Robograph.

Robograph uses directed acyclic graphs to represent your algorithms.


## Why should I use this instead of writing a code module that does the trick?
Because graphs can be understood and managed also by people that don't have
coding skills. And also because single nodes and subgraphs can be reused over
different algorithms, without the need to changing them.
And finally, because it's fun!

## Graph examples
There are lots of graph samples in the `sample_graphs` folders: each module over
there is a graph factory that you can use to instantiate a graph. Eg:

```
from sample_graphs import sum_and_product
graph = sum_and_product.sum_and_product([3, 4, 5])
output = graph.execute()  # {'sum value': 12, 'product value': 60}
```

What if you want to build your own graph? Say that you want to save an online
image to a local file:

```
from datamodel.base import graph
from datamodel.nodes.lib import files, value, http

# Create the nodes
url = value.Value(value='http://httpbin.org/image/png', name='url')
http_client = http.Get(mime_type='image/png', name='http_client')
file_writer = files.BinaryFileWriter(filepath='/tmp/target.png')

# Create an empty graph
g = graph.Graph('my_graph')

# Add nodes
g.add_nodes([url, http_client, file_writer])

# Connect nodes:
# first, tell the http_client node the URL to GET..
g.connect(client, url, 'url')

# ..then tell the file_writer node what data write to the output file
g.connect(writer, client, 'data')

# You're ready to run the graph and admire /tmp/target.png !
g.execute()
```


## Installation

Install the package with:

    sudo pip install robogaph

or clone this repository if you prefer.


## Writing your custom nodes
**TBD**


## Drawing graphs
```
from datamodel.nodes import plotter

# g is your graph
plotter.show_plot(g)               # show it
plotter.save_plot(g, 'graph.png')  # save it to file 'graph.png'
```

## Contributing/testing

Install the development dependencies with:

    sudo pip install -r dev-requirements.txt

The unit tests suite leverages `py.test` and can be run with:

    bash runtests.sh

**Contributions are welcome!** The more basic nodes we build, the more useful
Robograph becomes to the community.
