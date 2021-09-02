
def pwchecker():
    mypwrd = str(input("Please insert your password:"))

    if  mypwrd.isalpha() and len(mypwrd) >= 8 and len(mypwrd) <= 14:

            print("Great, You have successfully inserted your password")
    else:
            print("Please insert a valid password")

            print("Hint: password must be alphabet characters only and btwn 8 and 14 characters, both incusive")
            pwchecker()

pwchecker()
