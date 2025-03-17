age = int (input ("Enter your age") )
ticket = str(input ("Do you have a ticket?") )

print ("Welcome to the cinema")
print ( "This movie is rated 15")
print ("")

if age >= 15 and ticket == "y":
     print ("Please find your seat")
else:
     print ("You are not allowed this time")
