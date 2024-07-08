x=True
def function():
    while(x==True):
        int(input("How old are you?"))
        if(age>=20):
            print("You are an adult")
        elif(age<=19):
            print("You are a teen")
        elif(age<=11):
            print("Your a child")
        ans = input("Are you done?")
        if ans == "yes":
            print("You are done!!!")
            break

function()