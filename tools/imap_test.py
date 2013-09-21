#!/usr/bin/python

## quick check imap configuration
                       
PORT = 443
IMAP_SERV = "testmail.domain.com"
USERNAME = "testowe@testmail.domain.com"
PASSWORD = "test_pass"

import imaplib
from tlslite.api import *
p = IMAP4_TLS(POP3_SERV)
print p.sock.session.serverCertChain.getFingerprint()
p.user(USERNAME)
p.pass_(PASSWORD)
print p.list()
p.quit()
