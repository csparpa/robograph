import math

from robograph.datamodel.nodes.lib import branching


def test_requirements():
    expected = ['data', 'condition', 'function_true', 'function_false']
    instance = branching.IfThenApply()
    assert instance.requirements == expected

def test_input():
    data = 7
    condition = lambda x: x >= 0
    function_true = lambda x: math.sqrt(x)
    function_false = lambda x: 0
    instance = branching.IfThenApply()
    instance.input(dict(data=data,
                        condition=condition,
                        function_true=function_true,
                        function_false=function_false))
    instance.set_output_label('any')

    # case: true
    assert instance.output() == math.sqrt(data)

    # case: false
    data = -34
    instance.reset()
    instance.input(dict(data=data,
                        condition=condition,
                        function_true=function_true,
                        function_false=function_false))
    instance.set_output_label('any')
    assert instance.output() == 0


def test_output():
    data = 7
    condition = lambda x: x >= 0
    function_true = lambda x: math.sqrt(x)
    function_false = lambda x: 0
    instance = branching.IfThenApply(data=data,
                                     condition=condition,
                                     function_true=function_true,
                                     function_false=function_false)
    instance.set_output_label('any')

    # case: true
    assert instance.output() == math.sqrt(data)

    # case: false
    data = -34
    instance = branching.IfThenApply(data=data,
                                     condition=condition,
                                     function_true=function_true,
                                     function_false=function_false)
    instance.set_output_label('any')
    assert instance.output() == 0

