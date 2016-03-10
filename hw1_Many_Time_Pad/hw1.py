import sys
import re
MSGS = open("ct.txt")
PT=open("pt.txt","w")
Indecies=open("index.txt","w")
Indecies2=open("index2.txt","w")
Indecies3=open("index3.txt","w")
IdxDict=dict()
IdxDict2=dict()
p1=""
target="32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"
target=target.decode('hex')
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


for msg in MSGS:
    if len(msg)%2==1:
        msg=msg[0:len(msg)-1]
    msg=msg.decode('hex')
    plaintext=strxor(target,msg)
    for i in range(0,len(plaintext)):
        if re.match("[A-Za-z]",plaintext[i]):
            #print i, plaintext[i]
            idx=str(i+1)
            word=idx+plaintext[i]+"\n"
            Indecies.write(word)
            if i+1 not in IdxDict:
                IdxDict[i+1]=plaintext[i]
                IdxDict2[i+1]=[plaintext[i]]
            else:
                IdxDict2[i+1].append(plaintext[i])
    Indecies.write("\n")        
    p=plaintext+"\n\n"
    PT.write(p)
    idxSort=sorted(IdxDict.items())
    idxSort2=sorted(IdxDict2.items())
for key,value in idxSort:
    p1=p1+value
    Indecies2.write(str(key)+value+"\n")
for key,values in idxSort2:
    Indecies3.write(str(key))
    for value in values:
        Indecies3.write(value)
    Indecies3.write("\n")
p1=p1.lower()
Indecies2.write(p)