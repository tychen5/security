#!/usr/bin/env python
import signal
import sys
import os
import time
import random
import string
 
from Crypto.Cipher import AES

import submit_flag as sf
import secret

FLAG = secret.FLAG
KEY = secret.KEY
IV = ''.join(random.choice(string.letters + string.digits) for _ in range(16))

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]

def alarm(time):
    def handler(signum, frame):
        print 'Timeout! QQ'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def check_pad(s):
    if len(s) % 16 != 0:
        return False

    N = ord(s[-1])
    if N > 16 or N < 1:
        return False

    padding = s[-N:]
    if padding != (N * chr(N)):
        return False

    return True

def AES_encrypt(m):
    global IV, KEY
 
    m = pad(m)
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    return aes.encrypt(m).encode('hex')

def encrypt_flag():
    global FLAG, IV

    print '\nIV:'
    print IV
    print 'Encrypted_FLAG:'
    print AES_encrypt(FLAG)

def decrypt():
    global KEY

    print '\nHow2decrypt? QQ\n'

    while True:
        c = raw_input().strip()

        try:
            s = c.decode('hex')

            if len(s) == 0:
                break
            elif len(s) < 16:
                print 'ValueError: IV must be 16 bytes long.'

            iv = s[:16]
            cipher = s[16:]

            aes = AES.new(KEY, AES.MODE_CBC, iv)
            plain = aes.decrypt(cipher)

            if check_pad(plain) == True:
                decrypt_flag = unpad(plain)
                print 'Success'
            else:
                print 'Fail'
        except:
            print 'Fail'

def menu():
    sf.count_solved()
    print '---------------'
    print '[1] Decrypt'
    print '[2] Submit Flag'
    print '[3] Hint'
    print '---------------'

    choice = int(raw_input('> ').strip())

    if choice == 1:
        encrypt_flag()
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
    alarm(60)
 
    menu()
 
if __name__ == '__main__':
    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
 
    main()
