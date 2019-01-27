#!/usr/bin/env python
import signal
import sys
import os
import time
 
from Crypto.Cipher import AES

import submit_flag as sf
import secret

KEY = IV = secret.FLAG
assert len(KEY) == 16

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]

def alarm(time):
    def handler(signum, frame):
        print 'Timeout! QQ'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def AES_encrypt(m):
    global IV, KEY
 
    m = pad(m)
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    return aes.encrypt(m).encode('hex')

def AES_decrypt(m):
    global IV, KEY

    m = m.decode('hex')
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    return unpad(aes.decrypt(m))
 
def test_aes():
    m = 'QQ Homework is too hard, how2decrypt QQ'
    expected_c = '296e12d608ad04bd3a10b71b9eef4bb6ae1d697d1495595a5f5b98e409d7a7c437f24e69feb250b347db0877a40085a9'

    assert AES_encrypt(m) == expected_c
    assert AES_decrypt(AES_encrypt(m)) == m
 
def decrypt():
    print '\nGive me a ciphertext, I will decrypt for you.'
    
    c = raw_input('Ciphertext: ').strip()
    m = AES_decrypt(c)

    print m

def menu():
    sf.count_solved()
    print '---------------'
    print '[1] Decrypt'
    print '[2] Submit Flag'
    print '[3] Hint'
    print '---------------'

    choice = int(raw_input('> ').strip())

    if choice == 1:
        decrypt()
    elif choice == 2:
        sf.verify_flag()
    elif choice == 3:
        sf.show_hint()
    else:
        print '1'
        time.sleep(1)
        print '2'
        time.sleep(1)
        print '3'
        time.sleep(1)
        print 'and...'
        time.sleep(1)
        print 'Bye!'
 
def main():
    time.sleep(1)
    alarm(30)
 
    test_aes()
    menu()
 
if __name__ == '__main__':
    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
 
    main()
