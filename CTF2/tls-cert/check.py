#!/usr/bin/env python3
# Python 3.6.4

import signal
from OpenSSL import crypto
from base64 import b64decode

def checkSubject(csie_cert, your_cert):
    csie_subject, your_subject = csie_cert.get_subject(), your_cert.get_subject()
    assert csie_subject.C == your_subject.C, '[X] Country'
    assert csie_subject.ST == your_subject.ST, '[X] Country'
    assert csie_subject.L == your_subject.L, '[X] Locality'
    assert csie_subject.O == your_subject.O, '[X] Organization'
    assert csie_subject.OU == your_subject.OU, '[X] Organization Unit'
    assert csie_subject.CN == your_subject.CN, '[X] Common Name'

def checkIssuer(root_cert, your_cert):
    store = crypto.X509Store()
    store.add_cert(root_cert)
    store_ctx = crypto.X509StoreContext(store, your_cert)
    assert store_ctx.verify_certificate() is None, '[X] Issuer'

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, lambda signal, frame: exit('[X] Timeout'))
    signal.alarm(30)

    with open('csie.pem', 'rb') as f:
        csie_cert = crypto.load_certificate(crypto.FILETYPE_PEM, f.read())
    with open('rootCA.crt', 'rb') as f:
        root_cert = crypto.load_certificate(crypto.FILETYPE_PEM, f.read())

    your_cert_raw = b64decode(input('Please give me the certificate encoded in base64 format:').strip())
    assert len(your_cert_raw) < 9453, '[X] Your certificate is too long'
    your_cert = crypto.load_certificate(crypto.FILETYPE_PEM, your_cert_raw)

    checkSubject(csie_cert, your_cert)
    checkIssuer(root_cert, your_cert)
    print('OK! You are one of balsn: ' + __import__("secret").flag)
