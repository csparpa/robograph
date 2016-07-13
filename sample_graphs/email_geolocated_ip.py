# Given an IP address, geolocate it and send the result over via e-mail

from datamodel.base import graph
from datamodel.nodes.lib import value, http, email


def email_geolocated_ip(recipients_list, smtp_server_params, ip_addr):
    subject = value.Value(value='Test mail')

    smtp_server_params['sender'] = 'test@test.com'
    smtp_server_params['mime_type'] = 'text/html'
    smtp_server_params['recipients_list'] = recipients_list
    sendmail = email.SmtpEmail(**smtp_server_params)

    http_params = dict(url='https://api.ip2country.info/ip?'+ip_addr,
                       mime_type='application/json')
    geolocate = http.Get(**http_params)

    g = graph.Graph('email_geolocated_ip', [subject, geolocate, sendmail])

    g.connect(sendmail, geolocate, 'body')
    g.connect(sendmail, subject, 'subject')

    return g

