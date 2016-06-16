import logging
import networkx as nx
from datamodel.base.exceptions import GraphError, StopGraphExecutionSignal, \
    GraphExecutionError

logging.basicConfig(level=logging.DEBUG)
console = logging.getLogger(__name__)


class Graph:

    def __init__(self, name, nodes=None):
        self._name = name
        self._nxgraph = nx.DiGraph()
        if nodes is not None:
            self.add_nodes(nodes)

    @property
    def root_node(self):
        return nx.topological_sort(self._nxgraph, reverse=True)[-1]

    def add_node(self, node):
        self._nxgraph.add_node(node)

    def add_nodes(self, sequence_of_nodes):
        for node in sequence_of_nodes:
            self.add_node(node)

    def connect(self, node_from, node_to, name=None):
        if not self._nxgraph.has_node(node_from):
            raise GraphError('Graph does not contain this node')
        if not self._nxgraph.has_node(node_to):
            raise GraphError('Graph does not contain this node')
        self._nxgraph.add_edge(node_from, node_to, dict(name=name))

    def execute(self):
        # Sort post-order (leaf nodes before, root node at then end)
        ordered_nodes = nx.topological_sort(self._nxgraph, reverse=True)

        # Output of node N is input for its parent
        try:
            for n in ordered_nodes:
                output = n.output()
                predecessors = self._nxgraph.predecessors(n)
                if not predecessors:
                    return output
                for parent in predecessors:
                    parent.input(output)
        except StopGraphExecutionSignal as e:
            console.info(e.message)
            return None
        except Exception as e:
            console.error(e.message)
            raise GraphExecutionError(e.message)

    def reset(self):
        for n in self._nxgraph.nodes():
            n.reset()

    def __unicode__(self):
        return unicode(self.__class__) + u' - %s' % (self._name,)
