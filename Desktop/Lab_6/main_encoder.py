#python encoder / decoder (Matthew Prue)

from encode import encode
from decode import decode


while True:
    #print menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    
    #get user input
    menuOption = int(input("Please enter an option: "))
    
    if menuOption == 1:
        newPass = input("Please enter your password to encode:")
        
        encodedPass = encode(newPass)
        
        print("Your password has been encoded and stored!")
        
    if menuOption == 2:
        
        decodedPass = decode(encodedPass)    
        print("The encoded password is " + (encodedPass) + " and the original password is " + (decodedPass) + ".")
        
    if menuOption == 3:
        break
    
    print()