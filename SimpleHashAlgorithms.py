def Hash(S):
    hash = 5381
    for c in S:
        hash = hash*33+ord(c)
    return hex(hash)
    
    
def Hash_(S):
    hash = 0
    for c in S:
        hash = hash+ord(c)
    return hex(hash)
    
    
S = "The red fox went over the bricks"
print(Hash(S))
print(Hash_(S))

S = "The red fox went oer the bricks"
print(Hash(S))
print(Hash_(S))


import hashlib

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()
    
def computeSHA2hash(my_string):
    m = hashlib.sha224()
    m.update(my_string.encode('utf-8'))
    
    return m.hexdigest()
    
    
print('SHA2', computeSHA2hash('abcd'))