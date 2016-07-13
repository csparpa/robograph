from robograph.datamodel.nodes.lib import printer


def test_requirements():
    expected = ['message']
    instance = printer.ConsolePrinter()
    assert instance.requirements == expected


def test_input():
    msg = 'Hello world'
    instance = printer.ConsolePrinter()
    instance.input(dict(message=msg))
    instance.set_output_label('any')
    assert instance.output() == msg


def test_output():
    msg = 'Hello world'
    instance = printer.ConsolePrinter(message=msg)
    instance.set_output_label('any')
    assert instance.output() == msg

