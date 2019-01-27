
# coding: utf-8

# In[47]:


from tqdm import tqdm


# In[23]:


from Crypto.Cipher import AES


# In[86]:


class DoubleAES():
    def __init__(self, key0, key1):
        self.aes128_0 = AES.new(key=key0, mode=AES.MODE_ECB)
        self.aes128_1 = AES.new(key=key1, mode=AES.MODE_ECB)

    def encrypt(self, s):
        return self.aes128_1.encrypt(self.aes128_0.encrypt(s))

    def encrypt1(self, s):
        return self.aes128_0.encrypt(s)
    def encrypt2(self, s):
        return self.aes128_1.encrypt(s)


    def decrypt(self, data):
        return self.aes128_0.decrypt(self.aes128_1.decrypt(data))

    def decrypt1(self, data):
        return self.aes128_1.decrypt(data)
    def decrypt2(self, data):
        return self.aes128_0.decrypt(data)


# In[25]:


def int2bytes(n):
    return bytes.fromhex('{0:032x}'.format(n))


# In[136]:


plaintext = 'NoOneUses2AES_QQ' #16
ciphertext=bytes.fromhex('0e46d393fdfae760f9d4c7837f47ce51') #32
flag_en = bytes.fromhex('3e3a9839eb6331aa03f76e1a908d746bfccaf7acb22265b725a9f1fc0644cdda')


# In[128]:


len(plaintext)


# In[129]:


en_list=[]
de_list=[]
for i in tqdm(range(2**46//2**23)):
    aes2 = DoubleAES(key0=int2bytes(i),key1=int2bytes(i))
    encr = aes2.encrypt1(plaintext)
    en_list.append(encr)
    
# for i in range(2**46 % 2**23):
#     aes2 = DoubleAES(key0=int2bytes(i),key1=int2bytes(ii))
    decr = aes2.decrypt1(ciphertext)
    de_list.append(decr)
s = set(de_list)
for i,v in tqdm(enumerate(en_list)):
    if v in s:
        print(i,v)
        print('key0:',i,'key1:',(i*2**23)%2**23) #6298659 #4272711


# In[135]:


# (i*2**23)
[i for i,x in enumerate(de_list) if x == b'o\xa6\x00\x99I\xd6\xf580-\x85\x12M\x06X\xa7']
# %2**23
# de_list


# In[137]:


aes2 = DoubleAES(key0=int2bytes(6298659),key1=int2bytes(4272711))
flag = aes2.decrypt(flag_en)
flag


# In[115]:


# '7ec3469a104fc8316e0d88f19e715a0da1cde0fc0cf2f4fe78baed8c63ff47be0067a455' in s
# en_list


# In[103]:


# import numpy as np
# np.max(en_list)


# In[72]:


# decr


# In[67]:


# len(list(s)[10000])  #64
# # len(en_list[100000]) #32
# # len(plaintext)
# len(flag_en)


# In[88]:


# # encr
# goal = '0e46d393fdfae760f9d4c7837f47ce51'
# for key in tqdm(range(2**46)):
#     key0, key1 = key // (2**23), key % (2**23)
#     aes2 = DoubleAES(key0=int2bytes(key0), key1=int2bytes(key1))
#     plaintext = 'NoOneUses2AES_QQ'
#     ciphertext = aes2.encrypt(plaintext).hex()
#     if goal == str(ciphertext):
#         print(key)
# #     print(ciphertext)


# In[98]:


# ciphertext='e5332e136c3746cca93e662f66b905f5ee6ceff6247d4ec3a7ccd3c07eca1093'
# print(ciphertext,len(ciphertext))
# print(plaintext,len(plaintext))
# print(aes2.encrypt1(plaintext).hex())
# kk=aes2.encrypt1(plaintext)
# print(aes2.encrypt2(kk).hex())
# print(aes2.encrypt2(ciphertext).hex())
# mm =aes2.decrypt1(ciphertext)
# print(aes2.encrypt1(mm).hex())


# In[125]:


# key0= 2**24//2**23
# key1 = 2**24 %2**23

# aes2 = DoubleAES(key0=int2bytes(key0), key1=int2bytes(key1))
# # plaintext = bytes.fromhex('0e46d393fdfae760f9d4c7837f47ce51')
# plaintext = 'NoOneUses2AES_QQ'
# ciphertext = aes2.encrypt1(plaintext).hex()
# print(ciphertext)
# print(len(ciphertext))

