import os
from hashlib import sha512
from binascii import hexlify
texts = ['8921bc663b8bdfc7bd15ac57d6d04d8d60358c98b09519ac18f8dc19ac6325c2b1ffa013b619f38904ba2f3dc292f5b91eff03fcc819e9602e8b98f9ba1aab12e7890bbb6031c289f9b01eb004b4c603e9563397abe5b61ef357fdc74dbe67358197b0980eb610fd890fac6e288b91f7f41fb611f2cc1fac6128c292f9ba12f210f5c408ba2f3a9090fdf40fb712b4e704a77b398c9bfff408ba05fdcc1ee9423d9096fff42bbe05e0d041e96e7c918ff9ba56b011f28902af2f288a9ab0870eaf12e68920a87d358ddff6a61ab114fcc01eac217cb690b09d15ab12e6d91fac7b7c9697f9a75bb212f9cc41e96628c28df5a50eb605f1da4dbd6739c28bf8b15baf1bf5d008bb2f288ddff2b15b9302fdce04e96e3286dfe4bc1eff05f1da19e9603ac28bf8b15b9c27c18e1ee97b33c29df5f408ba03b4dd02e96a3d9186b0bb15ff16fad04d846e2e8b90b0841aad03ed890aa86239c290fef41ab10eb4e704a77b398c9bfff418b019e7c601ac217ca38bb0a013ba57f1c709e9603ac29eb0b912b11eb9ce0ca46a70c2d7f9b25bbb18facc4daa602e909af3a017a65eb4e518a06835c288f9b817ff00fdc74dab767c888ae3a05bac03f5c709a0613bc28ce4bd17b357f5c709e96b338b91f7f415b003fcc003ae237c8789f5ba5bb611b4dd05ac2f318b91f9f91cbe1af1891fac7e298b8df5a75bb218e2cc00ac6128ccdfddb509b618b4f90cbb7b25c2cdbcf40cbe04b4c84dae6e3187dfe4bc1aab57e3c81ee96935908ce4f409ba1bf1c81eac6b7c8d91b0a013ba57dac003bd6a328690b0e24fff1efa8923a67d288adfd1b91ead1ef7c84da6617ca89efea11aad0eb49b59bd6770c2cda0e44bff16facd4da07c7c9697f5f408ba06e1cc01e97b33c28bf8b15bb005fdce04a76e30c298f1b91eff05f1c508a87c3986dfffba5bab1ff1891ea86239c29cffba08b01bf18904a72f6ddbc6a9fa5b8b1ff1890aa86239c296e3f408ba03b4c618bd2f308b94f5f41aff15fbc81fad2f3b8392f5f85ba81ee0c14db9633d9b9ae2a75bab16ffc003ae2f3596dff9ba5bab02e6c71ee97b33c292ffa21eff05fbdc03ad2f288a9ab0b614be05f0890ca76b7c8190fcb81ebc03b4da19a87d2fccdfd1b20fba05b4cc1bac7d258d91f5f413be04b4c10cad2f6dc298fff85b9e57e6c803ad6031c292f9ba12f210f5c408e9662fc28cf5b81ebc03f1cd4dbe66288adfe4bc1eff00fdc703ac7d7c909af3b112a91eface4da82f3f8d96fef419b019e1da43e94628c288f1a75bab1ff1da08e962358c96bdb31ab212e7854dbd673d96dff1a61eff02e7cc09e96632c28bf8b15bb005fdce04a76e30c289f9b01eb059b4eb2c855c1299b1f5821ead28c19c08963f3287a0a7bd16ba28c4e80996382bab9cd5a95b8b1ff18902bb663b8b91f1b85ba91ef0cc02e9783d91dfe5a417b016f0cc09e97b33c2a6ffa12faa15f1890fb02f178e86f4b128ab18e6c44da6617cad9ce4bb19ba05b4985cbd6770c2cda0e442f157c0c108e97935869afff408b718e3da4d857a358596b0b21abc1eface4dfa2f1fb2aae3f414b957d9c81fa06070c2aff5b518b757f5c709e9583d9096fff85bbe1bf8891eac7b7c9690b0b11aac0eb8891aa1663087dfdca112b81eb4c318ba7b7c918bf1ba1fac57e0c108bb6a7c9597f9b81eff03fccc4d8a5f09c58cb0b01eb912f5dd4dbd67398f8cf5b80dba04ba89']
def genTables(seed="Well one day i'll be a big boy just like manhell"):
    fSub={}
    gSub={}
    i=0
    prng=sha512()
    prng.update(seed)
    seed=prng.digest()
    for el in xrange(256):
        cSeed=""
        for x in xrange(4):
            cSeed+=prng.digest()
            prng.update(str(x))
        prng.update(cSeed)
        fCharSub=[0]*256
        gCharSub=[0]*256
        unused=range(256)
        for toUpdate in xrange(256):
            i+=1
            curInd=ord(cSeed[toUpdate])%len(unused)
            toDo=unused[curInd]
            del unused[curInd]
            fSub[(el,toUpdate)]=toDo
            gSub[(el,toDo )]=toUpdate
    return fSub,gSub
f,g=genTables()


def encrypt(pad, ptext):
    assert(len(ptext)<=len(pad))#if pad < plaintext bail
    ctext = []
    if type(ptext)==type(""):
        ptext=map(ord,ptext)
    if type(pad)==type(""):
        pad=map(ord,pad)
    for padByte,ptextByte in zip(pad,ptext):
        ctext.append(f[padByte,ptextByte])
    return  "".join(map(chr,ctext))
def decrypt(pad, ciphertext):
    assert(len(ciphertext)<=len(pad))#if pad < ciphertext bail
    ptext = []
    if type(ciphertext)==type(""):
        ciphertext=map(ord,ciphertext)
    if type(pad)==type(""):
        pad=map(ord,pad)
    for padByte,ctextByte in zip(pad,ciphertext):
        ptext.append(g[padByte,ctextByte])

    return "".join(map(chr,ptext))


# For the first 70 columns
for b in xrange(0, 70):
    # The column we're on
    print "== Index is: %d ==" % b

    # Build a ciphertext from the nth character of every ciphertext
    new_ctext = ""
    for i in texts:
        new_ctext += i.decode("hex")[b:b+1]

    # Attempt to decrypt the ciphertext with every possible key byte (256 possibilities)
    for i in xrange(256):
      print "%d: %s" % (i, decrypt(chr(i)*len(new_ctext), new_ctext))