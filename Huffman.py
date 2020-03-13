# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:34:20 2020

@author: Seif ElSaeed
"""
import HuffmanCodes as code
import os
def main():
    
    inputfile = 'test.txt'
    binaryfile = 'test.bin'
    decodefile = 'decodedtest.txt'
    ###ENCODING
    
    #open file and put it in a string
    with open(inputfile, 'r') as myfile:
        string = myfile.read()
    
    #Create Dictionary of Code
    dict = code.saad_please_i_need_the_codes(string)
    
    #Encode string to byte array using Code Dictionary
    bitstring = ''
    for c in string:
        bitstring += dict[c]
    bytestring = toBytes(bitstring)
    
    #write to binary file the encoded version
    with open(binaryfile,'wb') as file:
        file.write(bytestring)
    
    
    
    
    ###DECODING
    
    #read the data from file as bytes
    with open(binaryfile,'rb') as file:
        encodeddata =  file.read()
    decodedbits = toBits(encodeddata)
    
    #made decode dict
    decodedict = {}
    for key in dict:
        decodedict[dict[key]] = key
    
    #decoding bitstring
    result = ''
    result = huffmanDecode(decodedict, decodedbits)
    
    #write to decoded file
    with open(decodefile,'w') as file:
        file.write(result)
        
    #print ratio of compression    
    ratio(inputfile,binaryfile)
    
    
def toBytes(bstring):
    b = bytearray()
    for i in range(0,len(bstring),8):
        b.append( int(bstring[i:i+8] , 2) )
    #last byte for number of none trash chars
    b.append(len(bstring)%8)
    return bytes(b)

def toBits(bytestring):
    b = ''
    lastbyte = ''
    temp = ''
    for i in range(0,len(bytestring)-2):
        for j in range(7,-1,-1):
            b += str( (int(bytestring[i]) >> j ) & 1 )
            
    #last byte to be correct
    for j in range (0,bytestring[ len(bytestring)-1 ],1):
        lastbyte = str( (int( bytestring[ len(bytestring)-2 ] ) >> j ) & 1 )
        temp += lastbyte
    temp = temp[::-1] 
    b+=temp
    return b

def huffmanDecode (dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return res

def ratio(inputfile,binaryfile):
    old = os.path.getsize(inputfile)
    new = os.path.getsize(binaryfile)
    print(f'Original file: {old} bytes')
    print(f'Compressed file: {new} bytes')
    print('Compressed file to about {}% of original'.format( round( (((old-new)/old)*100), 0)) )
    
main()
        
    