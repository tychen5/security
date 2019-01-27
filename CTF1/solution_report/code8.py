
# coding: utf-8

# In[51]:


import sys
from hashlib import sha1
from PIL import Image
from Crypto.Util.number import bytes_to_long as b2l
from Crypto.Util.number import long_to_bytes as l2b
import command
import socket
from subprocess import *
import subprocess
import time


# In[52]:


pdf_header = l2b(0x255044462D312E330A25E2E3CFD30A0A0A312030206F626A0A3C3C2F57696474682032203020522F4865696768742033203020522F547970652034203020522F537562747970652035203020522F46696C7465722036203020522F436F6C6F7253706163652037203020522F4C656E6774682038203020522F42697473506572436F6D706F6E656E7420383E3E0A73747265616D0A)
jpg_header = l2b(0xFFD8FFFE00245348412D3120697320646561642121212121852FEC092339759C39B1A1C63C4C97E1FFFE01)

# Collision blocks (This is the only part of the files which is different)
collision_block1 = l2b(0x7F46DC93A6B67E013B029AAA1DB2560B45CA67D688C7F84B8C4C791FE02B3DF614F86DB1690901C56B45C1530AFEDFB76038E972722FE7AD728F0E4904E046C230570FE9D41398ABE12EF5BC942BE33542A4802D98B5D70F2A332EC37FAC3514E74DDC0F2CC1A874CD0C78305A21566461309789606BD0BF3F98CDA8044629A1)
collision_block2 = l2b(0x7346DC9166B67E118F029AB621B2560FF9CA67CCA8C7F85BA84C79030C2B3DE218F86DB3A90901D5DF45C14F26FEDFB3DC38E96AC22FE7BD728F0E45BCE046D23C570FEB141398BB552EF5A0A82BE331FEA48037B8B5D71F0E332EDF93AC3500EB4DDC0DECC1A864790C782C76215660DD309791D06BD0AF3F98CDA4BC4629B1)


# In[53]:


s = socket.create_connection(('140.112.31.96', 10121))
time.sleep(1)
strs1 = s.recv(1000000)
strs11 = str(strs1).split('?')[-1].split(':')[0]
strs11


# In[54]:


for i in range(99999999):
    data = l2b(0x00+i)
    prefix1 = pdf_header + jpg_header + collision_block1+data
    kk = sha1(prefix1).hexdigest()
    if kk[-6:] == strs11:
        print(prefix1) #X
        print(kk) #sha(Y)
        break
#     print(data)

# prefix1 = pdf_header + jpg_header + collision_block1+data
prefix2 = pdf_header + jpg_header + collision_block2+data


# In[55]:


s.send(prefix1.hex().encode()+b'\n')
time.sleep(1)
strs2 = s.recv(1000000)
strs2


# In[56]:


prefix2 = pdf_header + jpg_header + collision_block2+data
s.send(prefix2.hex().encode()+b'\n')
time.sleep(1)
strs3 = s.recv(1000000)
strs3


# ***

# In[21]:


# kk = sha1(prefix1).hexdigest()
# kk[-6:]
# # kk


# In[12]:


# sha1(prefix1).hexdigest()


# In[32]:


# strs1


# In[33]:


# prefix1

