def encode(newPass):
    encodedPass = ""
    
    for i in newPass:
        j = (int(i) + 3) % 10
        encodedPass += str(j)
        
        
    return encodedPass