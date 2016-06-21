import logging
import traceback
import networkx as nx
from datamodel.base.exceptions import NodeConnectionError, \
    StopGraphExecutionSignal, GraphExecutionError

logging.basicConfig(level=logging.ERROR)
console = logging.getLogger(__name__)


class Graph:
    """
    A graph, composed of nodes and edges. Leverages the Networkx library to
    efficiently store graph components and perform graph traversals.
    """

    def __init__(self, name, nodes=None):
        self._name = name
        self._nxgraph = nx.DiGraph()
        if nodes is not None:
            self.add_nodes(nodes)

    @property
    def root_node(self):
        """
        Gives the root node of this graph.
        :return: datamodel.base.node.Node instance
        """
        return nx.topological_sort(self._nxgraph, reverse=True)[-1]

    def add_node(self, node):
        """
        Adds the specified node to the graph
        :param node: datamodel.base.node.Node instance
        :return: None
        """
        self._nxgraph.add_node(node)

    def add_nodes(self, sequence_of_nodes):
        """
        Adds the specified collection of nodes to the graph
        :param sequence_of_nodes: collections of datamodel.base.node.Node instances
        :return: None
        """
        for node in sequence_of_nodes:
            self.add_node(node)

    def connect(self, node_from, node_to, output_label):
        """
        Connects node_from to node_to on the underlying graph model and states
        that the output of node_from will be injected as labeled input into
        node_to using the specified label.
        :param node_from: datamodel.base.Node instance
        :param node_to: datamodel.base.Node instance
        :param output_label: str
        :return: None
        """
        if not self._nxgraph.has_node(node_from):
            raise NodeConnectionError('Graph does not contain this node')
        if not self._nxgraph.has_node(node_to):
            raise NodeConnectionError('Graph does not contain this node')
        node_to.set_output_label(output_label)
        self._nxgraph.add_edge(node_from, node_to)

    def execute(self, result_label="result"):
        """
        Starts from the leaf nodes, calculates their outputs and feeds them as
        inputs to their parent ones. The loop stops once the root node is reached.
        Optionally, you can assign a custom label to the output of the root node.
        :param result_label: str (optional)
        :return:
        """

        # Sort post-order (leaf nodes before, root node at then end)
        ordered_nodes = nx.topological_sort(self._nxgraph, reverse=True)

        # Assign a label to the output of the very last node to be executed:
        # the root node!
        self.root_node.set_output_label(result_label)

        # Output of node N is input for its parent
        try:
            for n in ordered_nodes:
                output = n.execute()
                predecessors = self._nxgraph.predecessors(n)
                if not predecessors:
                    return output
                for parent in predecessors:
                    parent.input(output)
        except StopGraphExecutionSignal as e:
            console.info(e.message)
            return None
        except Exception as e:
            console.error(traceback.format_exc())
            raise GraphExecutionError(e.message)

    def reset(self):
        """
        Resets all the nodes in the current graph, thus making the graph ready
        for a new execution
        :return: None
        """
        for n in self._nxgraph.nodes():
            n.reset()

    def __unicode__(self):
        return unicode(self.__class__) + u' - %s' % (self._name,)
