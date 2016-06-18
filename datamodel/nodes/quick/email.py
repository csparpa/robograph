from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datamodel.base import node


class SmtpClient:
    def __init__(self, server_hostname, server_port, username, password,
                 use_tls=True):
        self._server_hostname = server_hostname
        self._server_port = server_port
        self._username = username
        self._password = password
        self._use_tls = use_tls

    def send(self, subject, body, recipients_list, sender, mime='html'):
        if mime == 'text':
            msg = MIMEText(body)
        else:
            msg = MIMEMultipart('alternative')
            msg.attach(MIMEText(body, 'html'))
        msg['Subject'] = subject

        # Send
        server = SMTP(self._server_hostname + ':' + str(self._server_port))
        if self._use_tls:
            server.starttls()
        server.login(self._username, self._password)
        server.sendmail(sender, recipients_list, msg.as_string())
        server.quit()


class SmtpEmail(node.Node):
    def __init__(self, server_hostname, server_port, username, password,
                 sender, recipients_list, use_tls=True, name=None):
        node.Node.__init__(self, name=name)
        self._smtp_client = SmtpClient(server_hostname, server_port,
                                       username, password, use_tls)
        self._sender = sender
        self._recipients_list = recipients_list

    def input(self, context):
        print context
        self._subject = context[0]
        self._body = context[1]

    def output(self):
        self._smtp_client.send(self._subject, self._body, self._recipients_list,
                               self._sender, 'html')

    def reset(self):
        del self._subject
        del self._body

