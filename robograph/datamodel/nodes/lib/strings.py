from robograph.datamodel.base import node


class TemplatedString(node.Node):
    """
    This node returns a string by filling a string template with named parameters
    Requirements:
      template --> a str template, containing named labels. Format is
      parameters --> dict with named parameters to be replaced into the template
    Eg:
      TemplatedString(template='After {p1} comes {p2}', parameters=dict(p1='one', p2='two'))
    """

    _reqs = ['template', 'parameters']

    def output(self):
        return self._params['template'].format(**self._params['parameters'])
