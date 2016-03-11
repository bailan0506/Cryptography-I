from Crypto.Hash import SHA256
f=open("6_1.mp4",'rb')
v=f.read(1024)
vBytes=list()
while v:
    vBytes.append(v)
    v=f.read(1024)
l=len(vBytes)-1
x=vBytes[l]
h=SHA256.new(x).digest()
while l>1:
    l=l-1
    x=vBytes[l]+h
    h=SHA256.new(x).digest()
l=l-1
x=vBytes[l]+h
h=SHA256.new(x).hexdigest()
fw=open('hash.txt','w')
fw.write(h)