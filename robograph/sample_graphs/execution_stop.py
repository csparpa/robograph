# Demo on how to stop a graph execution

from robograph.datamodel.base import graph, exceptions
from robograph.datamodel.nodes.lib import value, apply


def execution_stop(number):

    def stop_here(value):
        if value >= 0:
            raise exceptions.StopGraphExecutionSignal('arg is positive')
        raise exceptions.StopGraphExecutionSignal('arg is negative')

    v = value.Value(value=number)
    a = apply.Apply(function=stop_here)

    g = graph.Graph('execution_stop', [a, v])

    g.connect(a, v, 'argument')

    return g