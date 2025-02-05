MembershipType = []
members = []

def adddetails():
  firstname = str(input("enter your fist name:"))
  lastname = str(input("Enter your last name: "))
  membership = str(input("enter your membership type:"))
  duration = int(input("enter your membership duration:"))

  totalprice = 0
  if membership == "Basic":
    totalprice = 29.99 * duration
  elif membership == "Standard":
    totalprice = 49.99 * duration
  elif membership == "Premium":
    totalprice = 69.99 * duration

  MembershipType.append([membership, totalprice])
  members.append([firstname, lastname, MembershipType, duration])

def savedetails():
  with open (
  


