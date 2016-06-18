import json
from datamodel.base import node


class ToJSON(node.Node):

    def input(self, context):
        self._context = context

    def output(self):
        return json.dumps(self._context)

    def reset(self):
        del self._context