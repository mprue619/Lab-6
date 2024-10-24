# decode() method for simple python encoder (Polina Antonenko)

def decode(password):
    decoded = ""

    for i in password:
        # convert to integer & shift down by 3
        num = (int(i) - 3) % 10
        password += str(num)

    return password