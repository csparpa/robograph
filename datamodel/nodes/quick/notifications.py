from datamodel.base import node


class SmtpEmail(node.Node):
    def __init__(self, server_hostname, server_port, username, password,
                 use_tls=True, name=None):
        node.Node.__init__(self, name=name)
        self._server_hostname = server_hostname
        self._server_port = server_port
        self._username = username
        self._password = password
        self._use_tls = use_tls

    def input(self, context):
        self._sender = context[0]
        self._recipients_list = context[1]
        self._subject = context[2]
        self._body = context[3]
        self._attachments_list = context[4]

    def output(self):
        raise NotImplementedError()

    def reset(self):
        del self._sender
        del self._recipients_list
        del self._subject
        del self._body
        del self._attachments_list
