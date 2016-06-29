class NodeOutputLabelUndefinedError(Exception):
    """
    Marks that the label for a node's output is still not specified
    """
    pass


class GraphError(Exception):
    """
    Base class for Graph errors
    """
    pass


class NodeConnectionError(GraphError):
    """
    This is to mark an error in connecting nodes of a graph
    """
    pass


class NodeDeletionError(GraphError):
    """
    This is to mark an error in deleting nodes of a graph
    """


class StopGraphExecutionSignal(Exception):
    """
    This is to notify termination of graph execution due to ordinary reasons.
    """
    pass


class GraphExecutionError(GraphError):
    """
    This is to mark an unexpected error in graph execution.
    """
    pass