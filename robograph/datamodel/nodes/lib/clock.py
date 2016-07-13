import datetime

from robograph.datamodel.base import node


class Date(node.Node):

    _reqs = []
    DEFAULT_DATE_FORMAT = '%Y-%m-%d'

    def output(self):
        return datetime.datetime.today().strftime(self.DEFAULT_DATE_FORMAT)


class FormattedDate(Date):

    _reqs = ['format']

    def output(self):
        if self._params['format'] is None:
            fmt = self.DEFAULT_DATE_FORMAT
        else:
            fmt = self._params['format']
        return datetime.datetime.today().strftime(fmt)


class Now(node.Node):

    _reqs = []
    DEFAULT_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

    def output(self):
        return datetime.datetime.now().strftime(self.DEFAULT_DATETIME_FORMAT)


class UtcNow(Now):

    def output(self):
        return datetime.datetime.utcnow().strftime(self.DEFAULT_DATETIME_FORMAT)