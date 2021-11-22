userstring = input("Which floor do you work on?")
usernum = int(userstring)

while usernum > 20:
    print("You entered: "+str(usernum)+"but there are only 20 floors in this building. Try again...")
    userstring = input("Which floor do yoou work on?")
    usernum = int(userstring);

  
print("Congrats! You work on floor:" + str(usernum))
