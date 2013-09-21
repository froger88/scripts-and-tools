#!/usr/bin/python

## quick check pop3 configuration
                       
PORT = 443
POP3_SERV = "testmail.domain.com"
USERNAME = "testowe@testmail.domain.com"
PASSWORD = "test_pass"

import poplib
from tlslite.api import *
p = POP3_TLS(POP3_SERV, port=995)
print p.sock.session.serverCertChain.getFingerprint()
p.user(USERNAME)
p.pass_(PASSWORD)
print p.list()
p.quit()
