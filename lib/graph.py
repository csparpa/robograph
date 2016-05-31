import networkx as nx
from exceptions import GraphError


class Graph:

    _nxgraph = None
    _root_node = None
    _context = None

    def __init__(self, name, nodes=None):
        self._name = name
        self._nxgraph = nx.DiGraph()
        if nodes is not None:
            self.add_nodes(nodes)

    @property
    def name(self):
        return self._name

    @property
    def root_node(self):
        return self._root_node

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

    def set_root_node(self, root_node):
        if not self._nxgraph.has_node(root_node):
            raise GraphError('Graph does not contain this root node')
        self._root_node = root_node

    # Righthand
    def inject(self, context):
        self._context = context

    def execute(self, context):
        # inject context into root node
        self._root_node.inject(context)

        # postorder traversal of the NX graph (last item is the root node)
        postorder_nodes = nx.topological_sort(self._nxgraph, reverse=True)

        # evaluate all nodes but the root one, following order
        value = [node.obtain() for node in postorder_nodes[:-1]]

        # evaluate root node
        return self._root_node.obtain(value)

    def __unicode__(self):
        return unicode(self.__class__) + u' - %s' % (self._name,)
