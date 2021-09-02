#

print("Hello")

def pwchecker():

    mypwrd = str(input("Please insert your password:"))
    # inpt = int(input(" Enter") )
    print(type(mypwrd))


    if  mypwrd.isalpha() and len(mypwrd) >= 8 and len(mypwrd) <= 14:
            print("Great, You have successfully inserted your password")
    else:
            print("Please insert a valid password")
            print("""Password hint:
                     password should be characters only and
                     number of characters should not be less than 8 and should not
                        be greater than 14""")
            pwchecker()

pwchecker()
