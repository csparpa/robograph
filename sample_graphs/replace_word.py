# Given a text, replace occurrences of the word "hello" with "ciao" - if any.
# If no occurrence is found, replace all whitespaces with "_" instead

from datamodel.base import graph
from datamodel.nodes import printer, value
from datamodel.nodes.quick import branching


def replace_word(text):
    t = value.Value(text, name="text")
    s = branching.If(lambda x: "hello" in x,
                     lambda x: x.replace("hello", "ciao"),
                     lambda x: x.replace(" ", "_"),
                     name="if")
    p = printer.ConsolePrinter()

    g = graph.Graph('replace_word', [t, s, p])

    g.connect(p, s)
    g.connect(s, t)

    return g
