import json
import cloudpickle
import jsonpickle
from datamodel.base import graph


class NodeDeserializationException(Exception):
    """
    Marks an error in deserializing a node string representation
    """
    pass


class NodeSerializer:

    """
    Python-dependent representations of a Node
    """

    @classmethod
    def to_dict(cls, node):
        """
        Creates a dict representation of a node
        :param node: datamodel.base.node.Node instance
        :return: dict
        """
        params = dict()
        for name, value in node._params.items():
            if callable(value):
                params[name] = jsonpickle.dumps(cloudpickle.dumps(value))
            else:
                params[name] = value
        return {'class': str(node.__class__),
                'name': node._name,
                'params': params,
                'output_label': node._output_label}

    @classmethod
    def from_dict(cls, node_dict):
        """
        Creates a node from a dict representation
        :param node_dict: dict
        :return: datamodel.base.node.Node
        """
        # import classes, so we can instantiate them at need
        import datamodel

        # retrieve the class object so we can instantiate the node
        klass = eval(node_dict['class'])
        node = klass(name=node_dict['name'])

        # now retrieve the parameters
        parameters = dict()
        for p in node_dict['params']:
            parameters[p] = node_dict['params'][p]

            # are we deserializing a pickled function?
            if isinstance(node_dict['params'][p], unicode):
                if "py/bytes" in node_dict['params'][p]:
                    parameters[p] = cloudpickle.loads(jsonpickle.loads(node_dict['params'][p]))

        node.input(parameters)
        node.set_output_label(node_dict['output_label'])
        return node

    @classmethod
    def serialize(cls, node):
        """
        Creates a JSON representation of a node
        :param node: datamodel.base.node.Node instance
        :return: str
        """
        return json.dumps(cls.to_dict(node))

    @classmethod
    def deserialize(cls, json_string):
        """
        Builds a Node from a JSON representation
        :param json_string: JSON str
        :return: datamodel.base.node.Node instance
        """
        try:
            node_dict = json.loads(json_string)
            return NodeSerializer.from_dict(node_dict)
        except Exception as e:
            raise NodeDeserializationException(e.message)


class GraphDeserializationException(Exception):
    """
    Marks an error in deserializing a graph string representation
    """
    pass


class GraphSerializer:

    """
    Python-dependent representations of a Graph
    """

    @classmethod
    def to_dict(cls, graph):
        """
        Creates a dict representation of a graph
        :param node: datamodel.base.graph.Graph instance
        :return: dict
        """
        def _get_id(seq, node):
            for item in seq:
                if item['data'] == NodeSerializer.to_dict(node):
                    return item['id']
            return None

        result = dict(name=graph.name)
        result['nodes'] = [dict(id=i, data=NodeSerializer.to_dict(node)) for i, node in enumerate(graph.nodes)]
        result['edges'] = []
        for edge in graph.edges:
            id_node_from = _get_id(result['nodes'], edge['node_from'])
            id_node_to = _get_id(result['nodes'], edge['node_to'])
            result['edges'].append(dict(id_node_from=id_node_from,
                                        id_node_to=id_node_to,
                                        output_label=edge['output_label']))
        return result

    @classmethod
    def serialize(cls, graph):
        """
        Creates a JSON representation of a graph
        :param node: datamodel.base.graph.Graph instance
        :return: str
        """
        return json.dumps(cls.to_dict(graph))

    @classmethod
    def deserialize(cls, json_string):
        """
        Builds a Graph from a JSON representation
        :param json_string: JSON str
        :return: datamodel.base.graph.Graph instance
        """
        try:
            graph_dict = json.loads(json_string)
            result = graph.Graph(name=graph_dict['name'])
            nodes = dict()
            for item in graph_dict['nodes']:
                nodes[item['id']] = NodeSerializer.from_dict(item['data'])
            result.add_nodes(nodes.values())
            for e in graph_dict['edges']:
                result.connect(nodes[e['id_node_from']],
                               nodes[e['id_node_to']],
                               e['output_label'])
            return result
        except Exception as e:
            raise
            #raise GraphDeserializationException(e.message)
