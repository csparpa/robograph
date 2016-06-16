class GraphError(Exception):
    pass


class StopGraphExecutionError(Exception):
    """
    This is to notify termination of graph execution due to ordinary reasons.
    """
    pass
