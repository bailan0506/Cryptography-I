from Crypto.Cipher import AES


def decrypt(key,cipherText,file):
    iv = cipherText[0:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    msg = cipher.decrypt(cipherText[16:])
    print msg
    f.write(msg+'\n')
f=open("plaintext.txt",'w')
key_1= '140b41b22a29beb4061bda66b6747e14'.decode('hex')
cipherText_1='4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode('hex')
key_2='140b41b22a29beb4061bda66b6747e14'.decode('hex')
cipherText_2='5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode('hex')

decrypt(key_1,cipherText_1,f)
decrypt(key_2,cipherText_2,f)
print len(cipherText_1)