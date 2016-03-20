import urllib2
import sys

""""Padding oracle attact to a website built for practice.

The data which we what to  decryt should be embeded in the URL, it is AES CBC
encrypted. In CBC, the last k bytes of the former block Xor right guessing bytes
of a block Xor k*chr(k) will form a valid byte and get a certain response from 
the server.

More information: http://www.iacr.org/archive/eurocrypt2002/23320530/cbc02_e02d.pdf
"""

def query(q):
    '''Send the query embeded hexadecimal encrypted data to the target website.
        
    Judge whether the encrypted data has valid padding.
    
    Args:
        q: a string of the hexadecimal encrypted data
        
    Returns:
        A boolean value. If get error code 404, which means good padding, return 
        True.Else return False.
    '''
    target = 'http://crypto-class.appspot.com/po?er='
    target = target + urllib2.quote(q) # Create query URL
    req = urllib2.Request(target) # Send HTTP request to server
    try:
        f = urllib2.urlopen(req)   # Wait for response
    except urllib2.HTTPError, e:          
        if e.code == 404:
            return True  # good padding 
        return False  # bad padding

        
def strxor(a, b):     #Xor two strings with equal length
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])
 
 
def drop_padding_bytes(last_block):
    '''Drop the padding bytes of the last block of decrypted data.
    
    The rule of padding: if the block has n empty bytes, fill the bytes
    with  chr(n). If the block do not obey the rule, we do not change it.
    
    Args:
        last_block: a string, the last block of the decrypted data.
        
    Returns: 
        last_block_new: a string, the last block without padding bytes.
    '''
    n_pad_bytes=ord(last_block[15])  # number of padding bytes
    drop_bytes=True
    last_block_new=last_block
    if n_pad_bytes in range(1,17):
        for i in range(15,15-n_pad_bytes,-1):
            if ord(last_block[i])!=n_pad_bytes :
                drop_bytes=False;  # padding format is not valid
                break
    if drop_bytes :
        last_block_new=last_block[:16-n_pad_bytes]  #drop padding bytes
    return last_block_new
 
 
def padding_oracle():
    """The main method for padding oracle attack.
    Print the result of decryption and save it in .txt file.
    """
    ciphertext=("f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd"
                "4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4")
    ciphertext=ciphertext.decode('hex')
    ct_blocks = list()
    plaintext=""
    guess_set=range(2,16)+range(32,128)+[1]  # the padding byte, space, puctuate, a-z, A-Z
                                             # Put '\x01' at last to avoid error in decrypt last byte.
    
    while ciphertext:
        ct_blocks.append(ciphertext[:16])  # divede ciphertext into blocks
        ciphertext = ciphertext[16:]
        
    print  "Block No.","|" ,"Block".center(16,' '), "|", "Byte", "|", "ASCII"
        
    for block_no in range(1,len(ct_blocks)):  #start from 1, the first block iv, do not need decrypt
        iv=ct_blocks[block_no-1]  #previous block
        block_in_decrypt=ct_blocks[block_no]
        pt_block=chr(0)*16 
        
        for byte_no in range(1,17):
            pad=chr(0)*(16-byte_no)+chr(byte_no)*byte_no #padding
            #guess the ascii value of one byte
            for asc_no in guess_set: 
                guess_byte=chr(asc_no)
                
                # alter the  value of the byte in guess
                if byte_no==1 :
                    pt_block=pt_block[:16-byte_no]+guess_byte
                else:
                    pt_block=pt_block[:16-byte_no]+guess_byte+pt_block[16-byte_no+1:]
                    
                iv_guess=strxor(iv,strxor(pt_block,pad))
                guess=(ciphertext[:(block_no-1)*16]+iv_guess+block_in_decrypt).encode('hex') 
                
                #send the previous blocks and the block in decryption to the website
                #if we get the true ascii vlue, the data will have valid padding
                if query(guess):
                    print ("%-9d | %-16s | %-4s | %-5d"%(block_no,pt_block, guess_byte, asc_no)) 
                    break
                    
        if block_no== len(ct_blocks)-1:    
            pt_block=drop_padding_bytes(pt_block) # drop padding bytes
            
        plaintext=plaintext+pt_block
        print "\nDecrypted plaintext:", plaintext, "\n"
        
    file=open("plaintext.txt",'w')
    file.write(plaintext)
    file.close()
 
 
if __name__ == '__main__':
    padding_oracle()
 
            
            
    
    
