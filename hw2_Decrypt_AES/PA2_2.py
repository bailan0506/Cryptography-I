from Crypto.Cipher import AES
from Crypto.Util import Counter


def decrypt(key,cipherText,file):
    iv = cipherText[0:16].encode('hex')
    iv=int(iv,16)  
    ctr = Counter.new(nbits=128,initial_value=iv)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    msg = cipher.decrypt(cipherText[16:])
    print msg
    f.write(msg+'\n')
f=open("plaintext2.txt",'w')
key_1='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
cipherText_1='69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.decode('hex')
key_2='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
cipherText_2='770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.decode('hex')

decrypt(key_1,cipherText_1,f)
decrypt(key_2,cipherText_2,f)
