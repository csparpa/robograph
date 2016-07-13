import logging

from robograph.datamodel.nodes.lib import printer

log_level = logging.INFO
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)


def test_requirements():
    expected = ['message', 'logger', 'loglevel']
    instance = printer.LogPrinter()
    instance.set_output_label('any')
    assert instance.requirements == expected


def test_input():
    msg = 'Hello world'
    instance = printer.LogPrinter()
    instance.input(dict(message=msg, logger=logger, loglevel=log_level))
    instance.set_output_label('any')
    assert instance.output() == msg


def test_output():
    msg = 'Hello world'
    instance = printer.LogPrinter(message=msg, logger=logger, loglevel=log_level)
    instance.set_output_label('any')
    assert instance.output() == msg

