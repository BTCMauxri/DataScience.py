# if = do some set of instructions IF some condition is True
# Else do something else

experience = int(input("How many years have you traded the market?: "))

if(experience <= 3):
    print("You are a fairly new trader")
elif(experience <= 6):
    print("You have some familiarity with the market")
else: print("You are a well seasoned trader!")
