#this is static code and we can also make it dynamic by storing data in DATABASE
id=int(1010)        """Database"""
pa=int(125143)      """Database"""

#Main Logic
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
