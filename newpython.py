#draw write a function that check password
#password string, not less than 8 and greater than 14
pwd=(input("enter a password:"))
def my_password(pwd):
        if len(pwd)>=8 and len(pwd)<14 and not pwd.isdigit():
                        print("congradulation you have entered a correct password")
        
        else:
                print("please enter a correct password")
                print("password hint:password must be greater than 8 or <14 characters and can't be digit only")
        
        
        

print(my_password(pwd))
