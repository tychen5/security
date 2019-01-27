#!/usr/bin/env python3
# Python 3.6.4

from Crypto.Cipher import AES

flag = ????????????????????????????????
assert len(flag) == 32

class DoubleAES():
    def __init__(self, key0, key1):
        self.aes128_0 = AES.new(key=key0, mode=AES.MODE_ECB)
        self.aes128_1 = AES.new(key=key1, mode=AES.MODE_ECB)

    def encrypt(self, s):
        return self.aes128_1.encrypt(self.aes128_0.encrypt(s))

    def decrypt(self, data):
        return self.aes128_0.decrypt(self.aes128_1.decrypt(data))

def int2bytes(n):
    return bytes.fromhex('{0:032x}'.format(n))

key = ?????????????
assert key < 2**46
key0, key1 = key // (2**23), key % (2**23)
assert key0 < 2**23 and key1 < 2**23

aes2 = DoubleAES(key0=int2bytes(key0), key1=int2bytes(key1))

plaintext = 'NoOneUses2AES_QQ'
ciphertext = aes2.encrypt(plaintext).hex()
print(plaintext, '->', ciphertext)
flag_enc = aes2.encrypt(flag).hex()
print('???', '->', flag_enc)
