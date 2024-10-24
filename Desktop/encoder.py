#python encoder / decoder (Matthew Prue)

encodedPass = ""
decodedPass = ""

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
        
        for i in newPass:
            j = (int(i) + 3) % 10
            encodedPass += str(j)
                
        print("Your password has been encoded and stored!")
        
    if menuOption == 2:
        for i in newPass:
            k = (int(i) -3) % 10
            decodedPass += str(k)
            
        print("The encoded password is " + (encodedPass) + " and the original password is " + (decodedPass) + ".")
        
    if menuOption == 3:
        break
    
    print()