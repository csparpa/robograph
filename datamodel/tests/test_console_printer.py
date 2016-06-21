from datamodel.nodes import printer


def test_requirements():
    expected = ['message']
    instance = printer.ConsolePrinter()
    assert instance.requirements == expected


def test_input():
    msg = 'Hello world'
    instance = printer.ConsolePrinter()
    instance.input(dict(message=msg))
    assert instance.output() == msg


def test_output():
    msg = 'Hello world'
    instance = printer.ConsolePrinter(message=msg)
    assert instance.output() == msg

