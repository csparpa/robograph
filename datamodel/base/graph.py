import logging
import traceback
import networkx as nx
from datamodel.base import exceptions

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

    @property
    def nodes(self):
        """
        Returns a list of nodes in this graph
        :return: list
        """
        return self._nxgraph.nodes()

    @property
    def edges(self):
        """
        Returns a list of dicts, each one describing a edge of the graph
        :return: list
        """
        nx_edges = self._nxgraph.edges(data=True)
        result = []
        for e in nx_edges:
            result.append(dict(node_from=e[0], node_to=e[1],
                               output_label=e[2]['name']))
        return result

    @property
    def nxgraph(self):
        return self._nxgraph

    @property
    def name(self):
        return self._name

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

    def remove_node(self, node):
        """
        Removes the specified node from the graph
        :param node: a datamodel.base.node.Node instance
        :return: None
        """
        if not self._nxgraph.has_node(node):
            raise exceptions.NodeDeletionError('Graph does not contain this node')
        self._nxgraph.remove_node(node)

    def remove_nodes(self, sequence_of_nodes):
        """
        Removes the specified collection of nodes from the graph
        :param sequence_of_nodes: collections of datamodel.base.node.Node instances
        :return: None
        """
        for node in sequence_of_nodes:
            self.remove_node(node)

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
            raise exceptions.NodeConnectionError('Graph does not contain '
                                                 'node_from: %s' % (node_from,))
        if not self._nxgraph.has_node(node_to):
            raise exceptions.NodeConnectionError('Graph does not contain '
                                                 'node_to: %s' % (node_to,))
        node_to.set_output_label(output_label)
        self._nxgraph.add_edge(node_from, node_to, name=output_label)

    def has_isles(self):
        """
        Tells if the graph has subgraphs. If so, it means that the graph has at
        least one node that is "isolated" from the bigger graph component.
        :return: bool
        """
        return len(nx.isolates(self._nxgraph)) != 0

    def execute(self, result_label="result"):
        """
        Starts from the leaf nodes, calculates their outputs and feeds them as
        inputs to their parent ones. The loop stops once the root node is reached.
        Optionally, you can assign a custom label to the output of the root node.
        :param result_label: str (optional)
        :return:
        """

        # Cannote execute graphs with isles
        if self.has_isles():
            raise exceptions.GraphExecutionError("Cannot execute graphs with "
                                                 "isolated nodes")

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
        except exceptions.StopGraphExecutionSignal as e:
            console.info(e.message)
            return None
        except Exception as e:
            console.error(traceback.format_exc())
            raise exceptions.GraphExecutionError(e.message)

    def reset(self):
        """
        Resets all the nodes in the current graph, thus making the graph ready
        for a new execution
        :return: None
        """
        for n in self._nxgraph.nodes():
            n.reset()

    def __repr__(self):
        return '<graph: %s instance of: %s>' % (self._name or '',
                                                str(self.__class__))

    def __len__(self):
        return self._nxgraph.number_of_nodes()
