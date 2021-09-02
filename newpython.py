#draw write a function that check password
#password string, not less than 8 and greater than 14
pwd=str(input("enter a password:"))
def my_password(pwd):
        if len(pwd)>=8 and len(pwd)<14:
                if type(pwd)==str:
                        print("congradulation you have entered a correct password")
        # elif len(pwd)<=8:
        #                   print("passord must be above 8 character")
        # elif len(pwd)>14:
        #                   print("password must be less than 14 character")                 
        # elif pwd != "ilovepython" :
        #                  print("please enter another pwd")
        else:
                print("please enter a correct password")
                print("password hint:password must be greater than 8 or <14 characters")
        
        
        

print(my_password(pwd))