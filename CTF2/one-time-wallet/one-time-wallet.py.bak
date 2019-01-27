import random
import signal
import sys
import os
import flag

def alarm(time):
    def handler(signum, frame):
        print 'Timeout'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def genHexString(byte):
    s = ''
    for i in range(byte / 4):
        r = random.getrandbits(32)
        s += '{0:0{1}x}'.format(r, 8)
    return s

def genAddress():
    return genHexString(12) 

def genPassword():
    return genHexString(20) 
    
def printWallet(i, address, balance, password):
    print 'Wallet', i    
    print 'Address:', address
    print 'Balance:', balance, 'BTC'
    print 'Password:', password
    print ''

if __name__ == '__main__':
    alarm(60)
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)

    for i in range(1, 101):
        printWallet(i, genAddress(), 0, genPassword())

    print 'Can you steal bitcoin from the next wallet?'
    address = genAddress()
    password = genPassword()
    printWallet(101, address, 100, '?')

    inputPassword = raw_input()
    if inputPassword == password:
        print 'You just got 100 BTC!'
        print flag.FLAG
    else:
        print 'No bitcoin for you...'
