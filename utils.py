import os 

def gcd(a,b):
    if b==0:
        return a 
    return gcd(b,a%b)

def extended_gcd(a,b):
    if b==0:
        return a,1,0
    g,x0,y0 = extended_gcd(b,a%b)
    x = y0
    y = x0 - (a//b)*y0
    return g,x,y

def check_keys():
        
    is_key_exist = os.path.isfile('key.txt')

    status = ''

    if not is_key_exist:
        status = 'No key found! Generate a new one'

    file_lines = []
    if is_key_exist:
        with open('key.txt') as file:
            file_lines = [line.rstrip() for line in file]
    
    if len(file_lines)!=1:
        if is_key_exist:
            status = 'Corrupt key found! Generate a new one'
            is_key_exist=False
    else:
        file_lines = file_lines[0]
        if(len(file_lines)<=160):
            is_key_exist=False
            status = 'Corrupt key found! Generate a new one'
        else:
            
            if not file_lines.isdigit():
                status = 'Corrupt key found! Generate a new one'
                is_key_exist = False
                return [status,is_key_exist,None,None,None,None,None,None]
            
            p = int(file_lines[0:80])
            q = int(file_lines[80:160]) 
            e = int(file_lines[160:])
            phi = (p-1)*(q-1)
            n = p*q
            dummy1,d,dummy2 = extended_gcd(e,phi)
            if d<0:
                d+=phi

            if gcd(e,phi) != 1:
                status = 'Corrupt key found! Generate a new one'
                is_key_exist = False
            else:
                status = 'Keys fetched successfully'
    if is_key_exist and status=='Keys fetched successfully':
        return [status,is_key_exist,p,q,e,phi,d,n]
    return [status,is_key_exist,None,None,None,None,None,None]
        
def append_zeroes_till_7_bits(s):
    while(len(s)<7):
        s="0"+s
    return s 

def group_by_seven(monolith):
    groups = []
    s = ''
    for bit in monolith:
        s+=bit 
        if len(s)==(7*30):
            groups.append(int(s,2))
            s = ''
    if len(s)>0:
        groups.append(int(s,2))
    return groups

def plain_text_to_cipher_text(M,e,n):
    return pow(M,e,n)

def cipher_text_to_plain_text(M,d,n):
    return pow(M,d,n)

def get_seven_chars(s):

    while len(s)<210:
        s = '0'+s

    groups = []
    bits = ''
    for c in s:
        bits+=c 
        if len(bits) == 7:
            groups.append(bits)
            bits=''
    if len(bits)>0:
        groups.append(bits)
    res = ''
    for g in groups:
        c = chr(int(g,2))
        if ord(c) != 0:
            res += chr(int(g,2))
    return res