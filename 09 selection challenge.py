print ("Welcome to the Nightclub")
print ("Entry Rules: You must be at least 18")
print ("and either a member, have an invitation, ")
print ("or be on the VIP list")

age = int (input ( "Enter your age: ") )
member = input ( "Are you a club member? (y/n) : ")
invitation = input ("Do you have an invitation? (y/n): ")

if age >= 18 and (member == "y" or invitation == "y") :
    print ("Access granted! Enjoy your night.")
else:
    print ("Sorry, you must be at least 18 to enter.")
