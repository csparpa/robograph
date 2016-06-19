# Given an IP address, geolocate it and send the result over via e-mail

from datamodel.base import graph
from datamodel.nodes import value, apply, transcoders
from datamodel.nodes.quick import email, http


def email_geolocated_ip(recipients_list, smtp_params_list, ip_addr):
    email_params_list = list(smtp_params_list)
    email_params_list.append('test@test.com')
    email_params_list.append(recipients_list)

    http_params = dict(url='https://api.ip2country.info/ip?'+ip_addr,
                       output_encoding='json')
    v = value.Value(http_params)
    geolocate = http.Get()
    add_subject = apply.ApplyStatic(lambda body: ['testmail', body])
    to_json = transcoders.ToJSON()
    sendmail = email.SmtpEmail(*email_params_list)

    g = graph.Graph('email_geolocated_ip', [v, geolocate, add_subject, to_json,
                                            sendmail])

    g.connect(sendmail, add_subject)
    g.connect(add_subject, to_json)
    g.connect(to_json, geolocate)
    g.connect(geolocate, v)

    return g

