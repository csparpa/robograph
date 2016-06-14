# Given a text, replace occurrences of the word "hello" with "ciao" - if any.
# If no occurrence is found, replace all whitespaces with "_" instead

from datamodel.lib import graph
from datamodel.nodes import printer, value
from datamodel.nodes import switcher
from datamodel.nodes import apply


def replace_word(text):
    t = value.Value(text, name="text")
    s = switcher.If(lambda x: "hello" in x,
                    lambda x: x.replace("hello", "ciao"),
                    lambda x: x.replace(" ", "_"),
                    name="if")
    a = apply.ApplyDynamic(name="apply")
    p = printer.ConsolePrinter()

    g = graph.Graph('replace_word', [t, s, a, p])

    g.connect(p, a)
    g.connect(a, s)
    g.connect(s, t)

    return g
