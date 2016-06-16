class GraphError(Exception):
    pass


class StopGraphExecutionSignal(Exception):
    """
    This is to notify termination of graph execution due to ordinary reasons.
    """
    pass


class GraphExecutionError(Exception):
    pass