# Given a text, replace occurrences of the word "hello" with "ciao" - if any.
# If no occurrence is found, replace all whitespaces with "_" instead

from datamodel.base import graph
from datamodel.nodes.lib import printer, branching, value


def replace_word(text):
    t = value.Value(value=text, name="text")
    s = branching.IfThenApply(condition=lambda x: "hello" in x,
                              function_true=lambda x: x.replace("hello", "ciao"),
                              function_false=lambda x: x.replace(" ", "_"),
                              name="if")
    p = printer.ConsolePrinter()
    g = graph.Graph('replace_word', [t, s, p])

    g.connect(p, s, 'message')
    g.connect(s, t, 'data')

    return g
