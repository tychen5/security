import cryptanalib as ca

with open('otp.txt', 'r') as f:
    ciphertext = f.read().translate(None, ' \n').decode('hex')

output = ca.break_multi_byte_xor(ciphertext,verbose=True)
print(output[0])

#flag = ''
#for x in range(len(ciphertext)):
#    flag += chr(ord(ciphertext[x]) ^ ord(output[0][x]))

#print(flag)
