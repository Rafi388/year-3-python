1)

password = ""
while password != "kebab":
  password = input('Please enter a password: ')
  print ("correct password accepted")


2)

answer = "N"
print("Yay! We are there!!")
while answer != "Y":
  answer = str(input("Please respond, y or n: ").upper())
  print("Are we there yet?")


3)
StayInLoop = 1
while StayInLoop != 2:
    print("Press 1 for  choice or 2 to exit")
    StayInLoop = int(input("Please respond, 1 or 2: "))
  
 print("Exited")


 4)
 loopCount = 1
while loopCount < 11:
  print("Loop", loopCount)
  loopCount = loopCount + 1

print("End")


5)
username = ""
while not username:
    username = str(input("Enter username: "))

print("your username,",username,"has been accepted")


6)
import random

number=random.randint(1,10)
userGuess=int(input("Guess the number between 1-10"))

# Add one line of code here to allow the user to
#..guess the random number multiple times
# Hint: You might need to indent some code
if number < userGuess:
    userGuess=int(input("Guess to High, try again: "))
else:
    userGuess=int(input("Guess to Low, try again: "))

print("Yay! You got it correct!!!")


7)
timesTable = 0
UserChoice = int(input("Enter a times-ta: "))

while timesTable < 13:
    print(timesTable *UserChoice)
    timesTable+=1
