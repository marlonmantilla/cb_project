#!/usr/bin/env python2.5
import xmlrpclib

# EDIT: webfaction credentials
username = "cittybox"
password = "7dfb3352"

# no need to edit below this line
server = xmlrpclib.Server('https://api.webfaction.com/')
session_id, account = server.login(username, password)

domain = raw_input("Please enter your domain name (no www, etc): ")
mail = raw_input("Please enter the mail subdomain (mail): ")
cal = raw_input("Please enter the mail subdomain (calendar): ")
doc = raw_input("Please enter the mail subdomain (docs): ")
start = raw_input("Please enter the mail subdomain (start): ")

# mx info
mx_info = (
            ('ASPMX.L.GOOGLE.COM','10'),
            ('ALT1.ASPMX.L.GOOGLE.COM','20'),
            ('ALT2.ASPMX.L.GOOGLE.COM','20'),
            ('ASPMX2.GOOGLEMAIL.COM','30'),
            ('ASPMX3.GOOGLEMAIL.COM','30'),
            ('ASPMX4.GOOGLEMAIL.COM','30'),
            ('ASPMX5.GOOGLEMAIL.COM','30'),
          )

# create mx records
for mx in mx_info:
    server.create_dns_override(session_id,
                               domain,
                               '',
                               '',
                               mx[0],
                               mx[1],
                               '')

# create CNAME record
try:
    server.create_domain(session_id, domain, mail)
except:
    pass

server.create_dns_override(session_id,
                           mail + "." + domain,
                           '',
                           'ghs.google.com',
                           '',
                           '',
                           '')

if cal:
    try:
        server.create_domain(session_id, domain, cal)
    except:
        pass

    server.create_dns_override(session_id,
                           cal + "." + domain,
                           '',
                           'ghs.google.com',
                           '',
                           '',
                           '')

if doc:
    try:
        server.create_domain(session_id, domain, doc)
    except:
        pass

    server.create_dns_override(session_id,
                           doc + "." + domain,
                           '',
                           'ghs.google.com',
                           '',
                           '',
                           '')

if start:
    try:
        server.create_domain(session_id, domain, start)
    except:
        pass

    server.create_dns_override(session_id,
                           start + "." + domain,
                           '',
                           'ghs.google.com',
                           '',
                           '',
                           '')