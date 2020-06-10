id=int(1010)        """Database"""
pa=int(125143)      """Database"""
while True:
    i=int(input("ID : "))
    p=int(input("Password : "))
    if i == id:
        if p == pa:
            print("Welcome User")
            break
        else:
            print("Your Password is Incorrect")
    elif p != pa and i != id:
        print("Your ID And Password Both Are Incorrect")