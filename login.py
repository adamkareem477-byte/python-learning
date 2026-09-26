username = "admin"
password= "12345678"

username1= input ("Enter your username:")
password1= input ("Enter your password:")

if username1 ==username and password1 != password:
    print ("wrong password")
elif username1==username and password1 == password :
    print ("login successful")
else: 
    print (" wrong username and password")