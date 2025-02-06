MembershipType = [] 

members = []


def login():
    idNum = input("Please enter your member ID number")
    file = open("membersDatabase.txt","r")
    members = file.readlines() #["jane.smith.standard.25","robert.jones.premium.36",...]
    user = members[int(idNum)].split(".") #["jane","smith","standard","25"]
    print(f"Hello {user[0]} {user[1]}. Your membership type is {user[2]} for {user[3]} months")
    file.close()


def adddetails(): # add a new user

    firstname = str(input("enter your fist name:")) 

    lastname = str(input("Enter your last name: "))

    membershiptype = ["Basic", "Standard", "Premium"] 

    Prices = [29.99,49.99,69.99]

    print("Membership options: ") 

    for i in range(0,len(membershiptype)): 

      print(membershiptype[i] + " " + str(Prices[i])) 

    membership = str(input("enter your membership type:")) 

    duration = int(input("enter your membership duration:")) 



    totalprice = 0 

    if membership == "Basic": 

        totalprice = 29.99 * duration 

    elif membership == "Standard": 

        totalprice = 49.99 * duration 

    elif membership == "Premium": 

        totalprice = 69.99 * duration


    print(f"Your {membership} membership cost {totalprice}")



    member = (firstname +"."+ lastname +"."+ membership +"."+ str(duration))
    members.append(member)


def savedetails(): 

   # get the member variable from the end of the members list
   member = members[-1]
   # open the file in append mode
   file = open("membersDatabase.txt","a")
   # add the member variable to the file
   file.write(member+"\n")

   file.close()


print("Welcome to the GYM membership system")
choice = int(input("Would you like to 1.log in or 2.sign up?"))
if choice == 1:
    login()
elif choice == 2:
    adddetails()
    savedetails()
