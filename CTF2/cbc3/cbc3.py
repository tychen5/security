#!/usr/bin/env python
import signal
import sys
import os
import time
import hmac
 
from Crypto.Cipher import AES

import submit_flag as sf
import secret

FLAG = secret.FLAG
KEY = secret.KEY

def alarm(time):
    def handler(signum, frame):
        print 'Timeout! QQ'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def pad(data, N=16):
    last = N - (len(data) % N) - 1
    data += os.urandom(last)
    data += chr(last)
    return data

def unpad(data, N=16):
    padding_len = ord(data[-1]) + 1
    return data[:-padding_len]

def AES_encrypt(m):
    global KEY

    IV = os.urandom(16)

    mac = hmac.new(KEY)
    mac.update(IV)
    mac.update(m)

    aes = AES.new(KEY, AES.MODE_CBC, IV)
    pad_m_mac = pad(m + mac.digest())

    enc_msg = IV + aes.encrypt(pad_m_mac)

    return enc_msg.encode('hex')

def AES_decrypt(m):
    global KEY

    m = m.decode('hex')

    IV = m[:16]
    m = m[16:]

    aes = AES.new(KEY, AES.MODE_CBC, IV)
    plain = aes.decrypt(m)
    unpad_p = unpad(plain)

    data = unpad_p[:-16]
    data_mac = unpad_p[-16:]

    mac = hmac.new(KEY)
    mac.update(IV)
    mac.update(data)
    if mac.digest() != data_mac:
        return False

    return data

def encrypt():
    m1 = raw_input('m1: ').strip()
    m2 = raw_input('m2: ').strip()

    print 'Encrypted_message:'
    print AES_encrypt(m1 + FLAG + m2)

def decrypt():
    m = raw_input('m: ').strip()

    try:
        data = AES_decrypt(m)
        if data == False:
            print 'MAC not match'
        elif FLAG in data:
            print 'Success'
        else:
            print 'Fail'
    except:
        print 'Error'

def menu():
    sf.count_solved()
    while True:
        print '---------------'
        print '[1] Encrypt'
        print '[2] Decrypt'
        print '[3] Submit Flag'
        print '[4] Hint'
        print '---------------'

        choice = int(raw_input('> ').strip())

        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            sf.verify_flag()
        elif choice == 4:
            sf.show_hint()
        else:
            print '1'
            time.sleep(1)
            print '2'
            time.sleep(1)
            print '3'
            time.sleep(1)
            print '4'
            time.sleep(1)
            print 'and...'
            time.sleep(1)
            print 'Bye!'
            exit()
 
def main():
    time.sleep(1)
    alarm(60)
 
    menu()
 
if __name__ == '__main__':
    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
 
    main()
